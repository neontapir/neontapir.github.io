---
layout: post
comments: true
title: Testability in Data-Driven Applications
date: 2012-09-05 08:36:47 -06:00
categories:
- coding
- professional
tags:
- testing

---
At work, there's a renewed interest in testability (_I've taken experience at a few positions and combine it into a narrative._)

![Testability](/assets/testability.png)

I'm a member of the third team to work on our project. The original team has left, the people who replaced them have moved on, and now we maintain and enhance this application. Often we find ourselves doing forensic analysis, trying to divine the reasoning behind some design choices.

For example, there was a case recently when we were looking into a defect and found that the logic causing the defective behavior was quite intentional. No one on the team nor the current product owner understands why anyone would ever have wanted the system to behave this way. When faced with a situation like this, tests are a saving grace.

Sadly, the previous teams made some different choices. This product began in a smaller, less structured organization. What we now think of as cowboy coding was _de rigueur_ back when this product was designed and first implemented. The second team, both to evolve with the company -- and for their own sanity, I'm sure -- implemented some automated testing and were faced with a challenge.

The application imports contracts and provides accurate price quotes. It is architected as an n-tier web application, but its purpose has evolved into a data warehouse. More and more business logic has moved into the database, yet the unit tests are written in NUnit and C#. As you have guessed, many of these tests are not unit tests in the common sense of the word. They are integration tests and rely heavily on having test data in certain conditions.

Consequently, the tests go through a Byzantine setup and teardown process that makes the tests very slow and brittle. A number of tests don't clean up properly after themselves, so the suite needs to be run in a certain order to ensure success. In short, adding new tests or changing the data access layer more time-consuming and complicated that it should be.

So, here we are, the third team. We experience a dynamic tension between two forces. One is Product, who wants to see competitive market features commensurate with a data warehouse solution -- faster processing of contract changes, better analytic reporting, and the like. The other is Development Management, who want to see industry-standard rigor around programming -- fewer defects, curtailed production access and automated testing that can plug into an end-to-end testing regimen of our integrated suite of products. Both groups want to see more predictable and faster feature delivery as we the third team learn about the software and the domain. Today, our most conservative estimates turn out to be optimistic.

## The Crux of the Matter

Looking at the situation, one can rightly say that the application's biggest issue is that it's hard to test. The application calculates correct pricing for supplies based on a number of applicable contracts. As you can imagine, the intersection of these contracts can be complicated, so there are a variety of factors and adjustments that need to be considered. Each one of these data scenarios should be tested before releasing a new feature.

Let's take unit of measure for example. Let's say I'm buying gum. Gum could be sold in individual pieces (known in UOM terms as an "each"), in packs which I'll call packages, and packages are often shrink-wrapped and bundled into what I'll call sets. As a glimpse into how varied item packaging can be, please consider looking at the 55-page [GS1-compliant brand label placement guide](http://www.gs1.org/docs/gsmp/gdsn/GDSN_Package_Measurement_Rules.pdf) PDF for consumable goods found in grocery stores.

Let's say as a buyer, I want to know the least expensive way I can get 17 sticks of Yummy-Yummy Bubble-Gummy Gum. I have a few avenues to pursue. I can get Yummy-Yummy:

*   directly from the manufacturer Gobstobbers International,

*   from the Save-A-Lot wholesaler,

*   the convenience store Quik-Bite, or

*   my local grocery store Groceries eXtreme

Some of them stock 3-pack sets of gum. Others stock 5-packs. At Quik-Bite, I can get individual packages. And, it turns out Gobstobbers International has a deal where they will create custom-size and branded packages like 17 Yummy-Yummy sticks to the package, but only if you order a large enough quantity of them.

To further complicate matters, depending on how many 17-stick units I need, I might be better off buying a box or a case and splitting it myself. And, now that we've discussed quantities, it's worth mentioning that all of these outlets sometimes offer sales, volume pricing, and special discounts to select customers.

Imagine writing an application that decides who to order gum from. There are a lot of data scenarios to consider!

It's like that with our application. We need a way to run a myriad of data scenarios through our pricing service to make sure we get the expected results.

Next time, I'll talk about techniques I've used to improve the testability of applications.
