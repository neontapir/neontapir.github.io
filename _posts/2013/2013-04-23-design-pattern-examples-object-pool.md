---
layout: post
comments: true
title: 'Design Pattern Examples: Object Pool'
date: 2013-04-23 06:30:18.000000000 -06:00
categories:
- coding
- professional
tags:
- design patterns
status: publish
type: post
published: true
meta:
  _yoast_wpseo_linkdex: '78'
  _edit_last: '5'
  _wpas_done_all: '1'
  _yoast_wpseo_focuskw: design pattern
  _wpas_skip_28796: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1437586727;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1065;}i:1;a:1:{s:2:"id";i:1064;}i:2;a:1:{s:2:"id";i:36;}}}}
author:
  login: Chuck
  email: neontapir@gmail.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
excerpt: !ruby/object:Hpricot::Doc
  options: {}
---
<p>After giving my talk at <a href="http://milehighagile2013.agiledenver.org">MHA 2013</a>, I wanted to explore some of the examples the group came up with. Today, let's talk about the Object Pool design pattern. Here's a link to the <a href="http://sourcemaking.com/design_patterns/object_pool">Object Pool</a> pattern on SourceMaking, in case you want to read up on the pattern before diving into this article.</p>
<p>In software, it's more common that an object or container can create whatever dependencies it needs. In real life, this is a more common design pattern, because there are many situations that fit the criteria for considering it:</p>
<ul>
<li>you have a finite set of items</li>
<li>each client needs a subset of those items</li>
<li>the items are too expensive for everyone to have one of their own</li>
<li>they can be re-used</li>
</ul>
<p>To implement this pattern, you need three components:</p>
<ul>
<li>a reusable <em>resource</em></li>
<li>a <em>pool</em> that holds and releases the resources </li>
<li>a number of <em>clients</em>, who consume the items</li>
</ul>
<p>In the Object Pool pattern, the resource pool has some responsibilities:</p>
<ul>
<li>add a resource</li>
<li>remove a resource</li>
<li>set resource limit</li>
</ul>
<p><strong>Straightforward Examples</strong></p>
<table>
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
</table>
<p>In these cases, it seems evident to me how the pool can manage the resources. The following examples bear closer examination.</p>
<p><strong>Bank Loan</strong></p>
<p>Resource: lending money<br />
Pool: the bank's lending pool<br />
Client: people wanting a loan</p>
<p>A bank loan is different from the other examples, in that in a sense, the bank can't produce more money. it can, however, limit the amount of money it loans out to clients. It can adjust that amount to fulfill the contract for being a resource pool.</p>
<p><strong>Technical Debt, team's capacity</strong></p>
<p>Resource: work capacity<br />
Pool: gap between ideal software and working software<br />
Client: features</p>
<p>Technical debt is a tougher example. How do you measure technical debt? One imperfect way, perhaps, is in man-hours of effort. Once you find a currency for technical debt, you can see that it is analogous to the bank loan example. Think of the team producing software as a software factory. You can add extra work capacity to the factory by taking on technical debt -- that is, adding it to the system. You can release technical debt by addressing the shortcomings of the software, though it reduces work capacity. And technical debt is limited in nature; too much technical debt can destabilize the software to the point where it is too fragile to handle normal operational conditions. Smart teams place a technical debt limit lower than the degenerate level I just described.</p>
<p>The team's capacity can be thought of the same way. A team's capacity is regulated in part by how much time is allocated to a project. This is why many teams who use ideal man hours to measure capacity do not use 8 hours a day. There are inevitably interruptions, meetings chief among them. This reduces the figure to maybe 6 ideal hours a day of productive work. Capacity can be added through people or more work time, and can be reduced through the same means. It's easy to see how capacity can be limited by taking the example to extremes.</p>
<p>For example, if you reduce the capacity to absurd levels, the waste inherent in spinning up -- that is, figuring out how to begin the next unit of work -- will consume all of the team's available bandwidth. On projects where the code is not touched for long periods, this effect is very pronounced.</p>
<p><strong>Scrum coach, friends of the team, consulting firm</strong></p>
<p>Resource: people with expertise<br />
Pool: a group of those people<br />
Client: teams needing their expertise</p>
<p>Here, the currency is expertise. Companies can add and remove coaches through hiring, firing and of course transition to other job responsibilities. They limit the number of coaches through the number of positions they maintain. The same approach can be used with database administrators or user experience designers.</p>
<p>Consulting firms help companies staff using the same paradigm. Unlike the other examples, consultants don't work for the same company as the teams who need them. Said in reserve, this pattern doesn't require the clients to own access to the resource. Although, if you look at the early examples, it's clear that in the library and bowling shoes cases, the patrons don't own the shoes or the books.</p>
<p><strong>Farm league</strong></p>
<p>Resource: minor league players<br />
Pool: the teams comprising the minor leagues<br />
Client: major league teams</p>
<p>This is perhaps my favorite example, because I hadn't thought of farm leagues this way. Players are added to farm teams though the draft. They are released through training and though players being "called up" to the majors, as well as through players being released from the farm teams themselves. There are a limited number of teams with set numbers of players on the roster, so there is an inherent limit to the system.</p>
<p>You can extend this line of reasoning to any apprenticeship program. And, taking the analogy further, perhaps you can think of a high school or university in the same way.</p>
<hr width="50%" />
<p>Being the first write-up, please let me know what you like about this write-up, as well as ideas to make it more interesting or useful. For example, would a diagram be helpful?</p>