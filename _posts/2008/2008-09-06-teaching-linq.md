---
layout: post
comments: true
title: Teaching LINQ
date: 2008-09-06 03:45:25 -06:00
categories:
- professional
tags:
- linq
- programming
---
At work, I'm involved in a few things:

* I'm the scrum master of one of our development squads  
* I'm a LINQ and functional programming evangelist  
* I'm a co-sponsor of the weekly development Lunch and Learn meetings  
* I'm moderating our software engineering book club

In this post, I'm going to talk a little about LINQ and the challenges I'm facing teaching LINQ to Objects to the team.

Our weekly Lunch and Learn sessions involve some preliminary discussion, then we turn the keyboard over to the audience. Our development staff consists of good programmers who largely learned the craft by rote, so few if any of us have formal computer science backgrounds. Hence, introductory sessions start at the very beginning.

The first LINQ session covered extension methods, because LINQ makes heavy use of them. We presented as an example nUnit's `Assert.AreEqual(expected, actual)` method. We showed how an extension method could make this read `expected.AreEqual(actual)`. Then, we had our volunteer do the same for strings.

We pointed out that this could get tedious, as `AreEqual` supports lots of types. So, we asked a volunteer to solve the problem in general. This proved challenging, and we discovered a hole in the team's collective knowledge base: generics.

Once we got that straight, we had a volunteer implement a generic extension method for nUnit's `IsInstanceOfType(type)` test method to illustrate type inference.

The remaining 20 minutes, we introduced the Select clause. Folks were confused about `Func<T, bool>`, and about lambdas. We didn't have enough time to cement the concepts, but we'll continue from there next week.
