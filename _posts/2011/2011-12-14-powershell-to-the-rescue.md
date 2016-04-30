---
layout: post
comments: true
title: PowerShell to the rescue!
date: 2011-12-14 20:55:00 -07:00
categories:
- coding
- professional
tags:
- powershell
- troubleshooting
---

I encountered a situation today at work that lent itself to PowerShell. One of the developers asked for some information about the PowerShell line I wrote to diagnose this problem, and I thought it might make a good blog post.

There was a pipe-delimited file that was failing to import into a database via our program, and the QA person was having trouble figuring out why. The process yielded a stack trace, which pointed to a certain stored procedure and a SQL error:

> System.Data.SqlClient.SqlException: Error during [stored procedure]: [stored procedure]; 4;  
> String or binary data would be truncated. at System.Data.SqlClient.SqlConnection.OnError  
> (SqlException exception, Boolean breakConnection)

The stack trace clearly suggests that an input is exceeding a field length. Question was which one. As it turned out, there was only one column being inserted by this procedure. I did a quick schema lookup and found out that the column in question allows 50 characters.

So, I wrote:

{% highlight powershell %}
    gc failing_input_file.txt | % {$_.split("|")[4] } `
      | ? { $_.Length -gt 50 } | select –unique | measure –line
{% endhighlight %}

The query yielded 255 offending rows, and led to an alteration of the INSERT stored procedure to truncate the value from the flat file.

The rest of this post is copied wholesale from that email.

Let me restate it a command at a time, and expand the aliases.

Most common PowerShell commands have an alias, which you can look at via **Get-Alias**. In general, if you want to know about a command, you type “**Get-Help** command-name”. I put a backtick after each line to continue the line, as is the PowerShell custom.

Many cmdlets (read: “command-lets”) do pipeline processing, which if you haven’t seen it means that the previous command’s output is handed to the next piece as input. The special variable $_ is the current whatever — in this case, the current line. With most commands like with select and measure, $_ is inferred.

PowerShell offers full access to .NET. The strings it returns are .NET strings, which is why Split() just works.

{% highlight powershell %}
    Get-Content failing_input_file.txt `      
    | ForEach-Object {$_.split("|")[4] } `    
    | Where-Object { $_.Length -gt 50 } `     
    | Select-Object –unique `                 
    | Measure-Object –line                    
{% endhighlight %}

The first line with **Get-Content** reads in the contents of the file.  
For each line of the file, the second part with the **Foreach-Object** splits that line by “|” and grabs the 5th item.  
The **Select-Object** command omits duplicates.  
The **Measure-Object** command counts the number of lines.

If you want the contract names themselves, leave off the Measure-Object call:

{% highlight powershell %}
    gc failing_input_file.txt `
    | % {$_.split("|")[4] } `
    | ? { $_.Length -gt 50 } `                                                       
    | select –unique
{% endhighlight %}
