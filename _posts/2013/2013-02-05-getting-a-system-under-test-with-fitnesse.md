---
layout: post
comments: true
title: Getting a System Under Test with FitNesse
date: 2013-02-05 20:53:54 -07:00
categories:
- coding
- professional
tags:
- agile
- csharp
- fitnesse
- testing

---
Over the past week or so, I've become quite a fan of FitNesse. [FitNesse](http://fitnesse.org) is "a simple tool that allows non-technical users to specify and run acceptance tests for software systems."

Our situation is familiar to many programmers. We have some legacy code that we desperately need to refactor, but the code is not under test. It was written by a team of engineers that's no longer with the company. There's some documentation, but it's far from complete. The software is in production and is used by a number of clients who would be very upset if its behavior changed.

The piece of the system we want to rewrite is data-intensive. It's the part of the code that takes client data feeds and import them into our system. I'm sad to report that the logic is scattered between some C# libraries and SQL stored procedures. The previous team wrote ambitious integration tests in NUnit that tear down databases and rebuild them each test. While better than nothing, code coverage is low and the amount of SQL code coverage is uncertain.

What we need is a simple way to exercise the feed importer: give it some data and check that the data imports as expected. Some tables in, some tables out. Enter the FitNesse tests. When Michael Feathers wrote in his book [Working Effectively with Legacy Code](http://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052) that systems should be under test before refactoring, he did not say they had to be unit tests. Once we figured out some of the tricks to getting .NET fixtures working, it turns out it's quick to mock up a simple customer data feed and import it into the database with our FitNesse fixtures. For guidance, I suggest Gojko Adzic's e-book [Test Driven .NET Development With FitNesse](http://gojko.net/fitnesse/book/).

While these first tests were good, it wasn't clear that they offered many advantages over our existing tests. At first, there was a lot of repetition and I saw FitNesse as an inferior tool. As I started to learn about page includes and special pages like SetUp and TearDown, though, I started to see FitNesse pages as modular pieces of code like methods and classes, and I was able to refactor away the awkwardness of the early tests.

However, when we started loading multiple data feeds in succession, the advantages became crystal clear. To verify data in FitNesse, you write the expected data into a Wiki markup table. Because we were having trouble getting the FitNesse fixtures to work, we kept paring down the data feed until it was a single unit of work.

Seeing the expected data in a simple table on a web page made the relationships between the incoming tables clear, not only to us but to our product owner and QA engineer as well! Things we thought were bugs turned out to be good conversations with our product owner about tricky business rules. After the first dozen tests or so, the NUnit tests looked cumbersome and wordy in comparison.

Yesterday afternoon in a conference room, I got the whole team of developers writing FitNesse tests. To some, dissolving the barrier between development and QA is a cherished sceptre of agile software development power. For them, the light bulb came on. Everyone kept writing tests today, even though the training was over. Tomorrow, we'll get our QA engineer up to speed. He may not be writing his own fixtures right away, but he can certainly mock up new data conditions and write new test pages.

In retrospect, we could have achieved similar results if we'd stopped thinking of the NUnit tests as unit tests and started thinking of them as black-box integration tests, and if we'd simplified the data. In contrast, the NUnit tests took real customer data with multiple scenarios through the system at once and they verified the results at each intermediate step. Writing these NUnit tests required intimate knowledge of the data import process, which only one developer had taken the time to master.

With the FitNesse tests, I don't have to worry about the steps in between and there's only one effect happening at a time. And, the NUnit tests would have been a hinderance in our current project, whose goal is to replace the bulk of that code with a newer, faster implementation anyway. I can't imagine feeling confident in our redesign if we had to rewrite the tests to verify the design.

Have you been able to make use of FitNesse or another testing technology like Cucumber in your project? Please share your thoughts in the comments.
