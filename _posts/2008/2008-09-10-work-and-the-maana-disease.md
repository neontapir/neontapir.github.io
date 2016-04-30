---
layout: post
comments: true
title: Work and the Mañana Disease
date: 2008-09-10 09:48:57 -06:00
categories:
- professional
tags:
- management
- risk
- refactoring
---
I am an advocate of change and refactoring at work, and I was disheartened to receive an email today asking that no one check files into source control unless they are directly related to their sprint, especially the functional requirements.

I found this missive chilling. I find several examples a day of code that could be improved with simple, well-known refactorings, but now I have a mandate not to! To me, doing preventative maintenance is responsible craft-work, and I'm [not alone](http://blog.codinghorror.com/mort-elvis-einstein-and-you/) in believing that.

I believe the intent of the policy is to lessen our exposure to risk. We had several merge issues recently, probably due to the Herculean task of merging a handful of code streams into a single integration candidate. In addition, our QA resources are spread very thin. With the last few releases sporting slight flaws, I think the concern is that we'll miss something bigger, something critical.

I agree. We will miss something critical. We'll miss an opportunity to wrestle this alligator to the ground while it's still an adolescent! Every new feature we add gets harder and longer, because the structural changes we need today were put off until later. And, "later often means never", as [Ed Hird says](http://edhird.blogspot.com/2007/11/conquering-manana-disease.html).

In the beginning, I kept hearing we'll focus on technical initiatives "once [the big roll-out] is complete". Now, it's "once the big roll-out is complete and [this other custom work] is done". My boss cautioned me early on that this stream of work never stops. I'm very worried that my workplace is fast succumbing to the "mañana disease".

When I was hired, I was told there wasn't enough time. So I rewrote a library in the course of adding functionality. I wrote unit tests to ensure I didn't break anything. And things were looking up. As time has passed, I've found there are some forces in play in the larger game that I'm not sure how to handle. That library I updated was isolated and my project introduced no breaking changes, which is the opposite of the fragile ball of mud that is the main code. However, these issues can be resolved with baby steps and careful testing.

What I can't solve with design principles and unit testing is aversion to change. We have been conducting Lunch and Learn sessions for months, and we get the same quarter of the developers -- the Early Adopters. We taught ourselves LINQ, fluent interface design, functional programming, and the like. But how do we get the Late Bloomers to where we are, when they don't seem to want to come? Any ideas?
