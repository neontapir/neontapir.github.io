---
layout: post
comments: true
title: Converting a PowerShell script into a pipeline processor
categories:
- coding
- professional
tags:
- pipeline
- powershell
- approaches
---
Ever had a situation where you write a program or script, but it takes forever to execute because of the size of the data set? That happened to me recently.

At work, we work with fixed-delimited files on occasion. These files represent all the relevant contract data for a company, so they can grow quite large. The one I'm working with today is 1.4 GB in size.

I already had a PowerShell script that would parse the file, but run against this file, it reduced my machine to a crawl eating up memory before it finished executing 2.5 hours later.

{% highlight powershell %}
 param($file = (Read-Host "Header file"))

$lines = @()

gc $file | select -skip 1 | % {  
 $contractId = $_.substring(6,6).trim()  
 $endDate = $_.substring(12,10).trim()  
 $startDate = $_.substring(22,10).trim()  
 $description = $_.substring(156,80).trim()

$data = New-Object PSObject -Property @{  
 ContractID = $contractId  
 StartDate = $startDate  
 EndDate = $endDate  
 Description = $description  
 }

$lines += $data  
 }

$lines  
{% endhighlight %}

Here's the command line I used:

<pre>PS> .\Parse-ContractHeader.ps1 HEADER.file</pre>

As you can see, this script reads the file line by line (after skipping the header row), creates an object for each line, puts the object into an array, and then returns the array. This approach works with the data set is small, but it breaks down at some point when the data becomes large.

What I needed was a script that would input and output to a pipeline, so I'd get the results one line at a time instead of all at once.

In PowerShell, there's a BEGIN-PROCESS-END structure you can use to handle pipeline input and output. Since my script doesn't need to do anything before or after processing the stream, all I need is a PROCESS block:

{% highlight powershell %}
 PROCESS {  
 $mfgId = $_.substring(0,6).trim()  
 $contractId = $_.substring(6,6).trim()  
 $endDate = $_.substring(12,10).trim()  
 $startDate = $_.substring(22,10).trim()  
 $cc = $_.substring(127,2).trim()  
 $description = $_.substring(156,80).trim()

$data = New-Object PSObject -Property @{  
 ContractID = $contractId  
 StartDate = $startDate  
 EndDate = $endDate  
 Description = $description  
 }

$data  
 }  
{% endhighlight %}

The command line is a little different now. I could have put these parts into a BEGIN block, but I wanted the additional versatility of being able to change the input stream.

<pre>PS> gc HEADER.file | select -skip 1 | .\Parse-ContractHeader.ps1</pre>

By the way, I also recently learned that if you have a script like `Parse-ContractHeader.ps1` in your path, you can just refer to it like a built-in cmdlet, like so:

<pre>PS> gc HEADER.file | select -skip 1 | Parse-ContractHeader</pre>

After I wrote the second version of this script, I found [a PowerShell pipeline script template](http://huddledmasses.org/writing-better-script-functions-for-the-powershell-pipeline/), which offers the added advantage of being able to elegantly handle both pipeline and parameter input. If I need to do more with this script, I'll give the template a shot.
