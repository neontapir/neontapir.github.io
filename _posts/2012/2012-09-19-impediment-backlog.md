---
layout: post
comments: true
title: Impediment Backlog
date: 2012-09-19 09:47:43 -06:00
categories:
- process
- professional
tags:
- agile
- impediments
- project-management
---

Look, I get it. You have a boss that hasn't coded in five years and doesn't remember that the path from idea to code isn't a straight line. You have a product owner that expects a miracle a day or the product won't ship on time. And the fridge has a stale batch of Mountain Dew that tastes like beer from an archaeological site.

Todays, let's talk about impediments.

![Impediments](/assets/IMG_0131.png)

### Cost Cutting Measures

Process deficiencies aren't the same as technical debt. Technical debt is accumulated over time and is ultimately the result of not knowing the future. People make design decisions that turn out to be wrong. The product changes focus, some assumptions change and it invalidates the design.

Because time to market is finite, though, some technical debt is inevitable. Good teams try to avoid creating technical debt through supple designs that can bend to meet future requirements. The ideal is a team that can pay technical debt faster than it accumulates.

When I say process deficiencies, I'm talking about the gap between an ideal process where there is zero waste and the actual process that's in use. There will always be gaps, places that could be improved. People are fallable. And, again, the future is unknown, so there will always exceptions to be handled.

To further the economic analogy of technical debt, process deficiencies represent the cost of doing business. In the recession, talk of cutting costs is inevitable. In agile, this talk takes the form of an impediment backlog.

### The Impediment Backlog

Part of the point of an agile retrospective is to challenge the status quo and to continue to strive to improve. Team members suggest ways to cut costs. An impediment backlog is a way to capture that information.

When coming up with the impediment backlog, the team doesn’t sit at my conference table and ask themselves, “why does our work life suck?”. They ask, “what is holding this great team back from cranking out features?” For more on this topic, take a look at Jean McLendon and Jerry Weinberg's article, [Beyond Blaming](http://www.ayeconference.com/beyondblaming/).

Some teams don't want to do this introspection. The list is long and daunting. Some of the items are outside the control of the team. However, when I hear a team say, “let’s ignore impediments”, I hear, “let’s stick our heads in the sand and pretend that our practices and our company’s practices don’t impact our efficiency”. It contradicts the "art of the possible" spirit inherent in agile. My advice: Dream big.

When creating an impediment backlog, I intend to be honest, maybe brutally honest, about the state of our practices. It’s our duty as agile team members to identify and address the things that stand in our way.

An impediment backlog is about naming the beast. An impediment backlog is about empowerment. It's about turning a "can't" into a "choose not to address right now", or just maybe, into a "choose to do something about it".

My impediment backlog has three columns:

<table style="border: 1px solid black; text-align: left;">

<tbody>

<tr style="border: 1px solid black; background-color: silver; text-align: left;">

<th style="border: 1px solid black; text-align: left;">Impediment</th>

<th style="border: 1px solid black; text-align: left;">Impact</th>

<th style="border: 1px solid black; text-align: left;">Potential Solutions</th>

</tr>

<tr style="border: 1px solid black; text-align: left;">

<td style="border: 1px solid black; text-align: left;">The team manages its own TeamCity installation</td>

<td style="border: 1px solid black; text-align: left;">· Team troubleshoots failed builds
· Team upgrades software and maintains Team City server</td>

<td style="border: 1px solid black; text-align: left;">· Don't do continuous integration to Dev
· Hire a support engineer to maintain development environments
· Transition the responsibility of building and deploying to Dev to SCM
· Have the SCM team take over support of Team City
· Transition the maintenance duties to Support
· Work with another team to share the burden of maintaining Team City</td>

</tr>

</tbody>

</table>

This example comes from a company where the SCM team does not manage changes to the development environment, just integration and production. Development teams maintain their own development environments, which takes time and effort that could be spent creating features.

I encourage teams to brainstorm potential solutions, that no idea is too wacky to be included. Some of the solution ideas like hiring a new person may be impractical.

### The Value of Identifying Impediments

Management needs to know when there are practices and environmental conditions that slow the team. The team needs to accept that management won't always choose to address them.

As with cost cutting measures, with every potential process improvement, there is a cost. Going back to the [Iron Triangle](http://en.wikipedia.org/wiki/Project_triangle), maybe the tradeoff is in quality. For example, perhaps the team identifies that the regression test suite takes a long time to execute and isn't finding as many defects as they had hoped. They pitch the idea of doing a random sampling of the tests. The risk is an increased chance that a defect slips through.

Maybe it costs scope. Maybe defects escape into production that would have been caught by regression testing. The team decides that the regression test suite should cover more functionality. The cost comes in the time spent doing additional testing instead of developing new features. The risk is that the additional testing won't find new defects.

Maybe the cost is in time. Instead of releasing less work on the same schedule, the team decides to increase the time between releases. The risk there is in marketing. Can the product continue to be competitive if features get to customers more slowly?

Maybe the cost is in quality. Maybe Product and Development together decide that the number of defects going into production is acceptable compared to the demands of the customers and needs of the product, so no change is made. The benefits outweigh the risk.

### Conclusion

There are no easy answers to these questions. However, in my experience, oftentimes these questions aren't even asked. Items in an impediment backlog start conversations, and they make invisible costs visible. Impediments might just get the CTO's mind thinking about ways to help the company self-organize, and suddenly the "impossible" becomes reality.

How have you used an impediment backlog in your work? Do you have different ways to do it?
