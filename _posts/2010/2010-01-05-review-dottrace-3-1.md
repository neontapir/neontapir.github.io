---
layout: post
comments: true
title: 'Review: dotTrace 3.1'
date: 2010-01-05 13:31:13 -07:00
categories:
- professional
tags:
- ANTS Profiler
- dotTrace
- object mapper
- performance
- ReSharper
- review
- tweaking
- unit testing
---
When running some unit tests for the Object Mapper project, I found the test suite's execution time had slowed down noticably. I had been spoiled at my previous employer, where I had access to ANTS Profiler. So, I set about finding a performance profiling tool.

While there are some free profilers out there, the reviews on the web led me to believe they wouldn't be up to the task. I was drawn to dotTrace because of its ReSharper integration. I decided to give it a go with their 30-day trial.

What you will read in forums is absolutely true: ANTS provides more data, with ReSharper, dotTrace is much easier to use. And, I have learned that more data is not necessarily better.

It seemed that dotTrace could not trace the code execution once it had been loaded into ReSharper's test runner thread, so I had to write a quick console app to exercise the code I wanted to check.  
dotTrace was able to pinpoint the area of code that plagued me, where I was doing some repetitive MethodInfo lookups. Some caching brought the performance back in line with what it had been.

During this tweaking process, I found dotTrace's capability to compare test runs to be invaluable! I was able to see in percentage terms how much things improved with the caching. I also removed the caching and saw the performance degrade as expected, so I could be sure it wasn't coincidence. And, I am happy to report that the Console.WriteLine statements in the console app were the most time-consuming piece of the process, so my engine ought be able to withstand the load I understand it will receive in production.

I strongly considering buying dotTrace when my trial expires. It's a good tool to have in the toolbelt.
