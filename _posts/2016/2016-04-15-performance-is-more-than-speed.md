---
layout: post
title: Performance is More Than Speed
date: 2016-04-15 14:15:00
categories:
- professional
tags:
- performance
- throughput
- latency
- supersonic
- aircraft
---

{% include side-image.html image="boom-supersonic-aircraft.jpg" %}

Recently a company called Boom announced that they were creating a supersonic
aircraft to replace the Concorde, which hasn't been in regular use since 2003.
This called to mind a presentation [slide deck](http://www.tamps.cinvestav.mx/~adiaz/ArqComp/03-Performance.pdf) I read last year talking about
performance that referenced the Concorde.

The thrust of the presentation is that when we speak about performance, there
are really two metrics we are conflating. One is the time to do the task, which
is measured as execution time or response time. We'll call that one **latency**.

The other metric is the rate at which work is done, measured in terms of items
per time frame. Oranges eaten per hour, for example. This is often called
**throughput** or bandwidth.

It's often the case that latency and throughput are in opposition. Let's examine
the Boom, the Concorde, and the Boeing 747.

First, latency. Considering performance, we want latency to be as low as
possible. The Boom's top speed will be about 1,450 miles per hour, 100 miles per
hour faster than the Concorde. A Boeing 747 can only manage about 610 mph. That
makes the Boom 2.4 times faster than a 747 (1450/610) and 1.1 times faster than
a Concorde (1450/1350). Therefore, a Boeing 747 has much higher latency than its
supersonic competitors, taking roughly 6 hours to fly the 3,459 miles from New
York and London compared to 2.5 for the Concorde or Boom. (The Boom arrives
about 10 minutes ahead of the Concorde.)

However, let's now look at throughput. A Boeing 747 can hold 470 passengers.
That makes its throughput 286,700 people-miles per hour (pmph). A Concorde can
carry 132 passengers, so its throughput is only 178,200 pmph. In other words, it
would take a Concorde 9 trips to convey the same number of passengers as a
Boeing could in 5.

A Boom will seat 40 passengers, for a throughput of 58,000 pmph. It would take a
Boom 25 trips to carry the same number of passengers as the 5 Boeing flights.

As you can see, latency and throughput can be very different. So, even thought
the Boom will be an impressive technological achievement, don't look to the Boom
to replace regular commercial 747 flights in the near future. To understand why,
we need to look at money, specifically **operating costs**.

For ease of calculation, let's assume all other costs are equal except fuel. A
Boeing 747 can carry 48,445 gallons of fuel. It consumes about a gallon a second
of fuel, or 20,413 gallons from New York to London. The market rate for jet fuel
is $5.99 per gallon at John F. Kennedy International Airport in New York.
Therefore, it costs roughly $122,274 in fuel to fly a 747 from New York to
London. With 470 passengers, that amounts to about $260 per passenger.

For the Concorde, its tanks hold 26,286 gallons of fuel. It burns 5638 gallons
per hour, which equates to 1.57 gallons per second. But, because of its flight
speed, at the same $5.99 price, it only costs $55,252 to fuel a Concorde to fly
from New York to London. With fewer passengers, the cost is $460 per passenger.

It's hard to do the same calculation for the Boom, since its technical
specification aren't as well known. However, if it's fuel consumption is similar
to the Concorde, it would cost $51,441 to fuel it, or $1,285 per passenger.

Fare determination is complicated, so let's simplify and say it costs $750 to
fly from New York to London. One-way tickets on the Concorde were $1113 in 1980,
which is about $3,400 in today's dollars using an inflation calculator, although
people more knowledgable than me say $5,000 is probably more accurate. That
would make the cost of a Boom ticket at least $6,000 to account for the fuel
difference.

For most people, spending $5,250 to save 3.5 hours of travel is not worth it.
But for some people, it definitely might. It's worth noting here that the
40-passenger capacity works to the Boom's advantage here. It's a lot easier to
find 40 people willing to spend $6,000 to fly than 132 willing to spend $5,000.
The lack of demand is what ended the Concorde program. The economics of the Boom
could make operating the Boom profitable in the niche market of supersonic
travel.

In this post, I talked about two different metrics that measure performance:
latency and throughput. I also talked about the economics of a supersonic jet
and concluded that the Boom might succeed where the Concorde failed. If this
kind of math interests you, I recommend you have a look at the presentation that
inspired this post. It moves from airplanes to talk about computing power and
talks about Amdahl's law, which is a tool for measuring the impact of improving
performance of using parallel computer processing.
