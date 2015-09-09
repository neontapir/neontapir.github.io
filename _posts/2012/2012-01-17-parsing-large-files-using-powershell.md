---
layout: post
comments: true
title: Parsing large files using PowerShell
categories:
- coding
- professional
tags:
- powershell
status: publish
type: post
published: true
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
At work, I had the need to parse through a large pipe-delimited file to count the number of records whose 5th column meets and doesn’t meet my criteria.

{% highlight powershell %}  
 gc items.txt -readcount 1000 | `  
 ? { $_ -notlike "HEAD" } | `  
 % { foreach ($s in $_) { $s.split("|")[4] } } | `  
 group -property {$_ -ge 256} -noelement | `  
 ft -autosize  
{% endhighlight %}

This command does what I want, returning output like this:

<pre>  
Count   Name
-----   ----
1129339 True
2013703 False
</pre>

Here’s some explanation in English, for those of you who don’t know PowerShell.

The first command is **gc** (Get-Content), which reads the file in 1000 (readcount) lines at a time.

The second command is **?** (Where-Object), which filters out the HEAD row.

The next command **%** is an alias for Foreach-Object, where object in this case is a 1000-line chunk. The inner loop is another foreach loop, which is slightly different from Foreach-Object in ways that are unimportant to the matter at hand. Point is, you can’t nest % blocks. The block of the foreach loop splits each line by pipe delimiter and returns just the 5th column (first column is numbered 0).

The next command in the chain is **group**, an alias for Group-Object, in this case we’re grouping by a calculated property, whether the output of the previous command is greater than or equal to 256\. By saying “-noelement”, I’m saying I don’t need an enumerated list of the values, which in this case are unimportant.

Finally, we get to **ft** (Format-Table). It is necessary because the Count column may be over 99999, in which case the value is truncated. The option “-autosize” causes PowerShell to make it fit instead.

However, for a 500 MB test file, this command takes about 5.5 minutes to run as measured by Measure-Command. A typical file is over 2 GB, where waiting 20+ minutes is undesirably long.

I posted a query to StackOverflow for some ideas.

While I waited, I discovered that 2500 was the optimum value for -ReadCount, getting the command execution time down to about 3.5 minutes.

Within minutes, I got a helpful hint from Gisli to look into using the .NET StreamReader. Here’s what that Show-SourceCounts script looks like:

{% highlight powershell %}  
param($file = $(Read-Host -prompt "File"))  
$fullName = (Get-Item "$file").FullName  
$sr = New-Object System.IO.StreamReader("$fullName")  
$trueCount = 0;  
$falseCount = 0;  
while (($line = $sr.ReadLine()) -ne $null) {  
  if ($line -like 'HEAD|') { continue }  
  if ($line.split("|")[4] -ge 256) {  
    $trueCount++  
  }  
  else {  
    $falseCount++  
  }  
}  
$sr.Dispose()  
write "True count: $trueCount"  
write "False count: $falseCount"  
{% endhighlight %}

This script yields the same results as the first command, but in about a minute. Quite an improvement!
