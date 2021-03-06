---
layout: post
comments: true
title: 'Case Study: Release Planning in Agile'
date: 2012-02-18 12:32:46 -07:00
categories:
- process
- professional
tags:
- agile
- epic
- project-management
- scrum
- t-shirt sizing
- theme
- user story

---
This is a story about how I applied my CSM experience and training to help a mid-sized project get off the ground.

# Beginnings

When I came onto the project, the company was struggling with agile. They had been doing software engineering for a while, but in the context of controlling hardware. This project, an item state management system, was a departure for them. They already had a product in this space which they were essentially reselling from a consulting firm. The existing product was awkward to use, its feature set was limited, and the consulting firm did not wish to re-write the product to scale.

So, the company decided to write a replacement. They chose C# and .NET as the language. “Mason”, the principal engineer on the project, was a Java programmer by trade, so they needed some help. I was hired onto the team as a senior .NET engineer who could help mature Mason’s technical capabilities in .NET, and they had already hired a mid-level .NET engineer who started a few weeks before I did. It quickly became apparent that my CSM knowledge would be just as valuable.

The team had the desire but not the field experience. Mason had written a prototype, and after quick examination of the code, it was clear that his architecture would not support the ambition of the product.

The project manager, “Jason”, had chosen Scrum as the delivery methodology, yet he had no experience with it. He was on the right track with sprint-level work management, but he was having trouble with release-level planning. he asked me if I could help get the project back on track. The product owner, “Kathy”, already had a comprehensive set of use cases outlined. While they were not fully-baked, they contained enough meat to discuss in detail what the project is trying to accomplish.

# Theme Sizing

I introduced the idea of themes. Kathy had already grouped the use cases into broad categories, so it seemed natural to think of these categories as themes. Jason and the product owner went off and grouped the use cases. They did it more fine-grained than I’d anticipated, putting them into a couple dozen smaller categories that I’d call epics.

I then introduced the idea of T-shirt sizing for themes. The goal of this was to talk about which parts of the application contained the greatest effort. Some use cases have some risk — we as a team aren’t sure how we’ll tackle them. Others don’t have enough definition. Still others represent a lot of work.

Over the course of a couple of afternoons, the team got them sized. The challenge remained, how do you use T-shirt sizes to create something that resembles the Gantt chart the project sponsors were comfortable with?

# Theme Points

It hit me, these T-shirt sizes were a scale, just not a numeric scale. I needed to quantify T-shirt sizes.

Mike Cohn has an article about [relating story points to hours](http://www.mountaingoatsoftware.com:80/blog/how-do-story-points-relate-to-hours) in which he shows story points graphed as Bell curves. So I wrote a scale like this on the whiteboard:

<pre>
Onesie  |  Small  |  Medium  |   Large  |     XL
</pre>

I picked an arbitrary number to represent a Medium. I wanted it to be on a scale that couldn’t be mistaken for user story points, so I chose 500.

<pre>
Onesie  |  Small  |  Medium  |   Large  |     XL
                      500    
</pre>

Of course, a Medium is not exactly 500 points. These represent a broad range, so I declared that a Medium was 500±50%, or 250-750.

<pre>
Onesie  |  Small  |  Medium  |   Large  |     XL
                  |   500    |
                 250        750
</pre>

I extrapolated to determine the rest of the scale.

<pre>
Onesie  |  Small  |  Medium  |   Large  |     XL
  60    |   180   |   500    |   1500   |    5000
       125       250        750        2500
</pre>

This worked out to roughly powers of 3.

<pre>
Onesie  |  Small  |  Medium  |   Large  |     XL
   1        x3         x8         x25        x83
</pre>

Jason took these ranges and our commentary during sizing that Theme X seemed bigger than Y and assigned values to each theme.

# So When Will That Be Ready Again?

By this time, we had already completed a sprint or two, enough that we had an idea that our velocity was going to be somewhere near 30\. We had enough information to try to correlate these themes against a calendar. Projecting when we’d complete the epic’s functionality and armed with our velocity, Jason threw the numbers into a spreadsheet and started trying out numbers.

Our current epic was rated at 800 theme points. We thought we’d be done with it in 6-7 ideal days, which means 3 developers can get through about 750 theme points in an ideal week. This became 250 points/dev/week, a velocity of sorts.

Thanks to the spreadsheet, we were immediately able to see that calculated out to about 12 months to write the application.

Better yet, we were able to forecast what general area of the application we’d be working on months from now, which allowed us to project some milestones. We need to have this epic done by Halloween to be on track, that set of themes by Thanksgiving, and so on.

Of course, these numbers had a high margin of error. We communicated it would be more like 6-18 months to write it. We reasoned that as the team got a epic or two under our belts, Jason and I should have been able to refine the conversion rate and get a more realistic idea.

# What If…

The real fruits of this exercise were that we now had a few variables that we could experiment with.

For example, that velocity of 30 was measured while we were storming as a team and 2/3 of us were new to the domain. Maybe we could expect the work would get easier as we learned the domain. This would be expressed as an increased velocity. If you increase the conversion rate from 250 to 300 after a month, you gain about a month over the life of the project.

A similar gain would be realized if a 4th developer is added after a couple of months. Other projections were made about the impact of adding a QA engineer early, which the project didn't have until much later.

# Course Correction

Of course, the project sponsors wanted it faster. To them, time to market was crucial. The company saw a dwindling market for their current offerings and were looking for ways to increase their reach. Their goals were compelling — it seemed like a good opportunity. This product would do things that others don’t.

Management needed a product that was feature-compatible with its competitors in the marketplace before the venture capital expired, so we were asked to come up with a plan that might possibly work.

We were able to use the spreadsheet to estimate how much of the application we’d have to de-scope to get it done in the timeframe we want, and Kathy was able to identify several themes as not mission critical to beta testing. The idea was that development would continue while the product was in beta, which I had discarded as too risky but Jason felt was viable.

# Presentation

We presented the plan. It was, in the parlance of a senior company executive, a “success-oriented plan”. No one was comfortable with it, so some difficult conversations followed. The project was in a bad position.

There were two senior executives who vied for control of the project. One felt that the company should continue to sell their poor solution until the new one was ready. The other felt that the poor solution could not be maintained, should not be sold, and the new one needed to be rushed to market.

The second executive won and demanded a crushing work pace, complete with extended work hours. I knew from experience that such a pace was not sustainable and was prone to error on a product whose core had to be solid the first time. The customers in that market would not forgive a poor first showing.

I could not in good conscience proceed with the project as outlined, so I left. I don’t know exactly how the story ends. The other experienced .NET engineer on the team left for similar reasons. I have spoken to Mason, and he told me the project is very behind the schedule Jason and I laid out.

# Conclusion

I think the exercise was worthwhile. Although the schedule Jason and I concocted was wildly speculative, it provided a frame of reference so that valuable conversations could take place. It got prompt and appropriate management attention to the project. The technique allowed us to do the analysis in a timeframe where its recommendations could be acted on.

Many of you reading this article have probably already formed opinions. It’s clear the project is in trouble. For me, it was that no project plan could overcome the fact that the delivery team did not have enough technical experience nor the business knowledge to rapidly develop such a complex product.

Without doing the analysis we did, I don’t think the errors in the original project plan would have surfaced until much later.
