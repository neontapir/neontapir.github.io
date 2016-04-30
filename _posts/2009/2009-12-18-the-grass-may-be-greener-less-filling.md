---
layout: post
comments: true
title: The Grass May Be Greener, Less Filling
date: 2009-12-18 00:24:52 -07:00
categories:
- professional
tags:
- architecture
- csharp
- composite
- consulting
- conversion
- corporate
- decorator
- design patterns
- mapper
- MbUnit
- middleware
- object mapper
- programming
- Reflection
- scrum
- Subversion
- Tortoise
- VSS
- agile
---

I embarked on an adventure last month, leaving my old job after eighteen months to re-enter the world of consulting.

When I started at the old firm, I thought of myself as just a computer programmer. I had reached a plateau at the home-building firm where I'd cut my teeth and had arrived at that position ready for a new challenge.

The first week, I was asked to add an enhancement to an application I hadn't seen before. They wanted the capability to alter an HTML control's text via an XML configuration file. I turned it around quickly, and developed a good reputation.

It turned out that the department had just started using agile and were having trouble getting over the hump. At my prior position, we'd been doing Scrum for a while and I said I could get it going there. They gave me a team of eager people and we were wildly successful. We got the rest of the department on Scrum, and our department managed to nearly double our output. I became a key part of the team, someone whom management and fellow developers looked to for leadership.

Sadly, it was not to last. We sold our product to a large customer overseas, and we were not ready to support that customer as though the product were a custom application. Meanwhile, the company I worked for had been acquired just as I hired on, and this overseas deployment brought scrutiny and change from the main office. As their culture and decisions supplanted our office, our agile ways and product vision met with more resistance.

I believe that friction led to some key leadership departures, and the magic that dwelt in that place dwindled away. I was even given the role of lead architect, but I quickly came to realize it was a quixotic quest and one not to be combined with a promotion. So, I sought my fortunes elsewhere.

My current position is a stark contrast to my architect position. My sphere of influence went from office-wide to cubicle-wide overnight. Most of my co-workers work in another state, and I feel isolated from the people I work beside.

The work is somewhat different from what I expected, too. I imagined technical challenges in decommissioning a certain piece of legacy middleware and replacing it with an adapter web service. We started by building a mapper service that can convert a type to an arbitrary type driven by an XML specification, for use on request and response objects.

A week in, I realized I was building something akin to ObjectBuilder or an IoC container. The constraints of the project hampered some tasks. For example, I had to fight to use unit tests, and I was asked to deliver a solution without any third-party libraries such as MbUnit. I was limited to VS 2005, C# 2.0, and ASMX web services.

I did have some latitude, though. I architected the whole solution. In the beginning, I though I was going to have to implement my own version of LinqBridge, but I found that the Composite and Decorator patterns led to some simple structures with powerful functionality.

I used TDD and ReSharper to amaze my co-worker with my quick delivery and robust code. My tests are in MbUnit, and I'm glad to report that during the development effort, the solution never dipped below 90% coverage as reported by PartCover. Initially, I didn't have access to their source control (VSS), so I installed Subversion locally and used Tortoise SVN to write to a repository on my network drive, which is where my tests still safely reside.

Sadly, though, I did not run into the kind of design challenges I was hungry for in building this component. However, I must say that I've leveraged the Reflection library much deeper than I had before. The most interesting piece was conditional mappings, which I implemented as delegates.

Going forward, it looks like I will be doing analysis of their legacy Java systems, detailing their old object and data models. Once done, systems analysts will be able to map the legacy application to the new infrastructure, and we can create an adapter web service with the help of that mapper component we wrote.
