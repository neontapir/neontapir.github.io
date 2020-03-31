---
layout: post
comments: true
title: 'Secret Santa Code Kata in Powershell'
categories:
- coding
- professional
tags:
- code exercise
- powershell

---
The team at work is doing a Code Kata, [the Secret Santa kata from Ruby Quiz](http://rubyquiz.com/quiz2.html). In it, you are given a list of names and emails and need to pair givers with receivers, with the only constraint being that a giver and receiver can’t have the same surname.

I wrote my solution in PowerShell. I wanted to use native PowerShell functionality, so I didn’t import any .NET libraries. I know this post is brief, but I wanted to get my solution posted with a little commentary while it was still fresh in my mind.

When run like this:

    PS> .santa.ps1 .names.txt

It gives output like:

    Giver                           Receiver
    -----                           ---------
    John Smith <jsmith@example.com> Jane Doe <jdoe@example.com>
    ...

Here’s the code:

{% highlight powershell %}  
param($file)

function ConvertTo-Array($hashtable)  
{  
  $result = @()  
  $hashtable.GetEnumerator() | % {  
    $object = New-Object PSObject  
    Add-Member -inputObject $object -memberType NoteProperty -name Giver -value $_.Name  
    Add-Member -inputObject $object -memberType NoteProperty -name Receiver -value $_.Value  
    $result += $object  
  }  
  $result  
}

$none = "NONE"  
$names = @{}  
gc $file | % { $names.Add($_, $none) }  
$namesToMatch = $names.Keys.Count  
if ($namesToMatch -lt 2) { throw "Need at least two names to match" }

while (($names.Keys | ? { $names.$_ -eq $none }).Length -gt 0)  
{  
  $from = $names.Keys | ? { $names.$_ -eq $none } | Get-Random  
  $to = $names.Keys | ? { $_ -ne $from -and $names.Values -notcontains $_ } | Get-Random  
  # "DEBUG: $from, $to"  
  if ($from -ne $null -and $to -ne $null -and $from.split()[1] -ne $to.split()[1])  
  {  
    $names.$from = $to  
  }  
  else  
  {  
    $undoMatch = $names.Keys | ? { $names.Values -ne $none `  
    -and $from.split()[1] -ne $_.split()[1]} | Get-Random  
    # "DEBUG: unset $undoMatch"  
    if ($undoMatch -ne $null)  
    {  
      $names.$undoMatch = $none  
    }  
  }  
  $percentComplete = 100 * ($names.Values | ? { $names.$_ -ne $none }).Length / $namesToMatch  
  Write-Progress -activity "Match in Progress" -status "% Complete:" -percentcomplete $percentComplete  
}  
$results = ConvertTo-Array $names  
$results | ft  
{% endhighlight %}

It reads the contents of the file and writes each line to a hash table, where all the receivers are $none (a special value I created which I used like $null).

As long as there are unmatched people, I go through an algorithm to select a random gift giver who doesn’t have a receiver ($from) and a receiver who doesn’t have a giver ($to). The `split(” “)[1]` yields a person’s surname.

I used a variant on the “Hill Climbing” algorithm mentioned on the site. If I run into a situation where there are no more matches, I take a random person who could have been a match and throw them back into the pool of candidates. In this way, the algorithm never gets stuck.

At the end, I call my `ConvertTo-Array` function to beautify the output. Without it, the hash table columns are labeled “Name” and “Value”, and that didn’t satisfy me. (I couldn’t get `Format-Table` to help.)

I added a progress bar to see how often this part of the code is invoked, and it gets called once or twice per run on average. However, the script itself has decent performance. It takes a second or so to match 40 names.

Please let me know what you think or ask questions. I’m happy to go into more detail.
