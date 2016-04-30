---
layout: post
comments: true
title: 'Design Pattern Examples: Object Pool'
date: 2013-04-23 06:30:18 -06:00
categories:
- coding
- professional
tags:
- design patterns
- object-pool
- approaches
---
After giving my talk at [MHA 2013](http://milehighagile2013.agiledenver.org), I wanted to explore some of the examples the group came up with. Today, let's talk about the Object Pool design pattern. Here's a link to the [Object Pool](http://sourcemaking.com/design_patterns/object_pool) pattern on SourceMaking, in case you want to read up on the pattern before diving into this article.

In software, it's more common that an object or container can create whatever dependencies it needs. In real life, this is a more common design pattern, because there are many situations that fit the criteria for considering it:

*   you have a finite set of items
*   each client needs a subset of those items
*   the items are too expensive for everyone to have one of their own
*   they can be re-used

To implement this pattern, you need three components:

*   a reusable _resource_
*   a _pool_ that holds and releases the resources
*   a number of _clients_, who consume the items

In the Object Pool pattern, the resource pool has some responsibilities:

*   add a resource
*   remove a resource
*   set resource limit

**Straightforward Examples**

<table>

<tbody>

<tr>

<th>Example</th>

<th>Resource</th>

<th>Pool</th>

<th>Client</th>

</tr>

<tr>

<td>thread pool</td>

<td>thread</td>

<td>the thread pool itself</td>

<td>programs</td>

</tr>

<tr>

<td>database connections</td>

<td>connection</td>

<td>connection pool</td>

<td>clients needing to connect</td>

</tr>

<tr>

<td>bowling shoes</td>

<td>pair of shoes</td>

<td>shoe caddy behind the counter</td>

<td>casual bowlers</td>

</tr>

<tr>

<td>library</td>

<td>book</td>

<td>general circulation</td>

<td>library patrons</td>

</tr>

<tr>

<td>video store</td>

<td>DVD</td>

<td>shelves</td>

<td>store patrons</td>

</tr>

<tr>

<td>ski rentals</td>

<td>skis</td>

<td>ski shop</td>

<td>casual skiiers</td>

</tr>

</tbody>

</table>

In these cases, it seems evident to me how the pool can manage the resources. The following examples bear closer examination.

**Bank Loan**

Resource: lending money  
Pool: the bank's lending pool  
Client: people wanting a loan

A bank loan is different from the other examples, in that in a sense, the bank can't produce more money. it can, however, limit the amount of money it loans out to clients. It can adjust that amount to fulfill the contract for being a resource pool.

**Technical Debt, team's capacity**

Resource: work capacity  
Pool: gap between ideal software and working software  
Client: features

Technical debt is a tougher example. How do you measure technical debt? One imperfect way, perhaps, is in man-hours of effort. Once you find a currency for technical debt, you can see that it is analogous to the bank loan example. Think of the team producing software as a software factory. You can add extra work capacity to the factory by taking on technical debt -- that is, adding it to the system. You can release technical debt by addressing the shortcomings of the software, though it reduces work capacity. And technical debt is limited in nature; too much technical debt can destabilize the software to the point where it is too fragile to handle normal operational conditions. Smart teams place a technical debt limit lower than the degenerate level I just described.

The team's capacity can be thought of the same way. A team's capacity is regulated in part by how much time is allocated to a project. This is why many teams who use ideal man hours to measure capacity do not use 8 hours a day. There are inevitably interruptions, meetings chief among them. This reduces the figure to maybe 6 ideal hours a day of productive work. Capacity can be added through people or more work time, and can be reduced through the same means. It's easy to see how capacity can be limited by taking the example to extremes.

For example, if you reduce the capacity to absurd levels, the waste inherent in spinning up -- that is, figuring out how to begin the next unit of work -- will consume all of the team's available bandwidth. On projects where the code is not touched for long periods, this effect is very pronounced.

**Scrum coach, friends of the team, consulting firm**

Resource: people with expertise  
Pool: a group of those people  
Client: teams needing their expertise

Here, the currency is expertise. Companies can add and remove coaches through hiring, firing and of course transition to other job responsibilities. They limit the number of coaches through the number of positions they maintain. The same approach can be used with database administrators or user experience designers.

Consulting firms help companies staff using the same paradigm. Unlike the other examples, consultants don't work for the same company as the teams who need them. Said in reserve, this pattern doesn't require the clients to own access to the resource. Although, if you look at the early examples, it's clear that in the library and bowling shoes cases, the patrons don't own the shoes or the books.

**Farm league**

Resource: minor league players  
Pool: the teams comprising the minor leagues  
Client: major league teams

This is perhaps my favorite example, because I hadn't thought of farm leagues this way. Players are added to farm teams though the draft. They are released through training and though players being "called up" to the majors, as well as through players being released from the farm teams themselves. There are a limited number of teams with set numbers of players on the roster, so there is an inherent limit to the system.

You can extend this line of reasoning to any apprenticeship program. And, taking the analogy further, perhaps you can think of a high school or university in the same way.

<hr width="50%" />

Being the first write-up, please let me know what you like about this write-up, as well as ideas to make it more interesting or useful. For example, would a diagram be helpful?
