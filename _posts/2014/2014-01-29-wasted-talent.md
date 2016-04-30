---
layout: post
comments: true
title: 'Lean Wastes and Software Delivery: Wasted Talent'
categories:
- process
- professional
tags:
- lean
- talent
- waste
---
[![talent](/assets/talent-300x200.jpg)](/assets/talent-300x200.jpg)

It’s easy to find examples of wasted talent, which comes from not making   full
use of a person’s talent, skill or knowledge.

I’ve also seen this in firms where work assignments are not fungible.   For
example, imagine a shop where most of the software is written in   Java, but
some is written in Ruby from an acquisition. Let’s say there   are 15 Java
programmers and 5 Ruby programmers, and neither group is   particularly familiar
with the other language.

One day, the company publishes its quarterly roadmap. On it, there is a   single
feature for a Ruby product and ten features for Java products.   The Ruby
developers are left with a choice of learning Java or lying   fallow. Either
choice leads to individuals not utilizing their Ruby   skills, which is a waste.

One technique that can help with wasted talent is **paired   programming**. The
effect of pairing is skills or knowledge transfer, so   use of paired
programming can help the Ruby programmer learn Java and   those Java products
more quickly. While pairing is often slower than   solo programming, it does
leads to fewer defects and allows both   programmers' talents to be used —
albeit at a lesser capacity at first.

I saw this waste occur when a firm hired a quality engineer who is   skilled at
test automation, but was instead tasked with manual execution   of test cases.
In particular, the regression suite of the legacy product   took days to walk
through, and the test teams received code too late to   have adequate time to
execute the full suite.

Test automation is an investment in the product, and it’s not free. Even   for a
greenfield application, it will often take more time to write an   automated
test than to execute it manually. Of course, once the test is   automated, it
can be executed in a fraction of the time, which pays   dividends.

Pairing in this case was challenging because many of the manual testers   did
not know how to program. And automation of the regression test   scripts right
before a release is not an ideal classroom setting. A   coding dojo would be a
better environment to convey the power of test   automation.

 **Coding dojos** are collaborative learning environments where people   can
 acquire new skills. For example, there is an exercise ("kata")   called the
 Bowling Game that’s used to teach test-first development   (TDD). Participants
 in the kata, even ones who haven’t programmed   before, learn the exercise by
 rote to start with. Questions leads to   learning programming concepts as
 students are ready. There are different   katas and sample applications
 available on the internet that would make   a suitable subject for test
 automation.

Sadly in this case, the firm did not want to make that investment.
Predictably, the test automation engineer found a position elsewhere   because
he found the work unsatisfying.

Next time, we'll look at wasted inventory.
