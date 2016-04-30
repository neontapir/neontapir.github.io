---
layout: post
comments: true
title: 'Process Violations: a Kanban experience report'
date: 2014-06-26 07:55:37 -06:00
categories:
- process
- professional
tags:
- experience
- kanban
- pizza
- process
- step
- story
- violations
---
![violations](/assets/violations.jpeg)

This is the fourth in a series of blog posts about implementing Kanban on my current project. The first installment was about [establishing the flow](% post_url 2014-06-05-establishing-flow-kanban-experience-report %). The second described the [Rally data extract scripts](% post_url 2014-06-12-rally-data-extract-scripts-kanban-experience-report %) I wrote. The third about [my Excel spreadsheet](% post_url 2014-06-19-excel-spreadsheet-metrics %) that consumes the data. This post is about Kanban flow process violations.

I enter the number of state change violations that occurred, either by a story skipping a step or going backward across the board. I wish Rally had stronger means to discourage people from these kinds of violations! For me, simply marking a nonconforming column red is not strong enough.

During the first milestones, I took an approach of education. Now that we've been using the board consistently for a few months, I am stricter about process violations. I've pointed out there's a strong correlation between stories that skip steps in the process and the amount of time stories stay blocked.

I want to share with you the contents of an email I wrote about these process violations. I think it gives you an example of my style, as well as being a useful analogy. Without further ado:

<div style="background:#DDDDDD;padding:1em">
<p>I’ve noticed an increase in state change violations. These fall into a few categories:</p>

<ul>
<li>Story skips steps without meeting exit criteria</li>
<li>Story goes backward across the board</li>
<li>Story “pushed” into next step instead of being marked ready</li>
</ul>

<p>Let me use an analogy that is hopefully familiar to all of us, ordering pizza for delivery. (Of course, it doesn’t look like your city has a lot of pizza delivery, so you might have to work with me a little bit.)</p>

<p>Here’s a screenshot from Domino’s Pizza’s web site, that shows a Kanban flow for a single work item (that is, your pizza).</p>

<p><img src="/assets/dominos-kanban-flow-300x129.png" alt="dominos-kanban-flow" title="" /></p>

<p>This closes matches the backend flow:</p>

<table>

<tbody>

<tr>

<td>Backend Step</td>

<td>Domino’s Step</td>

</tr>

<tr>

<td>Ready</td>

<td>Order Placed</td>

</tr>

<tr>

<td>Design</td>

<td>Prep</td>

</tr>

<tr>

<td>Development</td>

<td>Bake</td>

</tr>

<tr>

<td>Validation</td>

<td>Quality Check</td>

</tr>

<tr>

<td>Out for delivery</td>

</tr>

<tr>

<td>Accepted</td>

<td>(Delivered)</td>

</tr>

</tbody>

</table>

<p>Let’s talk about each of the violations above in turn.</p>

<p><strong>Skip steps</strong></p>

<p>An example of this would be if a pizza moved from step 2 (prep) to step 4 (quality check). In this case, the person putting the pizza in the box would notice that it isn’t cooked. They would walk back to the prep station and have a discussion with the prep person. While they are talking, no pizzas are moving through the oven, which slows the delivery of all the pizzas in the line.</p>

<p>The most common violation I see in our current flow is that a story is created and is immediately put in Development. In doing so, the Ready and Design steps are skipped. Those stories don’t have many details and no testing criteria. This causes problems in the Validation step, since the person doing QA is left wondering what changed and what should be tested.</p>

<p><strong>Moving backwards</strong></p>

<p>An example would be if a pizza moved from step 3 (bake) to step 2 (prep). Once a pizza is baked, it doesn’t go back through prep. If a topping is missed, the pizza is rejected and a new one is made. You can’t re-bake a pizza and still have it taste good.</p>

<p>Rather than thinking of a story’s column as its current state, think of it as being the most advanced state a story has achieved. If a story needs rework, just get the proper resources involved and do the missing work. If there’s a problem or the story needs attention, use blocking as a signal.</p>

<p><strong>Story is “pushed” instead of marked ready</strong></p>

<p>Let’s say our pizza just finished baking (step 3). Who takes the pizza out of the oven? There’s a gap between when the pizza leaves the oven and when the quality check begins. Usually, it’s the QA person and the time between the oven and the quality check station is negligible. In this situation, it doesn’t seem like there would be any harm in marking the pizza as being in step 4 when it comes out of the oven.</p>

<p>Now let’s imagine that pizzas go through the oven twice as fast. Now the manager is having to remove pizzas from the oven before they burn, but QA hasn’t started yet. If the pizza goes into step 4 immediately, it looks like the QA station is doing twice the amount of work it’s doing. This is a false signal. Really, the QA station isn’t twice as good, it needs help!</p>

<p>When a story has met the exit criteria for a step, it should be marked ready. When someone is ready to do that work, they move the story into the next column. Because the work is done by the same person in many of the columns , sometimes this step is forgotten.</p>

<p>In fact, the procedure really looks like this:</p>

<ol>
<li>Finish getting story ready for next step</li>
<li>Check board from right to left for work that is ready to move to the next step</li>
<li>Take the furthest right, top-most item and go to step 1</li>
</ol>

<p>I see that step 2 is often neglected, and that people look for stories that are in their area of expertise first. I would challenge each of you to go through this exercise and see whether you end up on the story you expected to. I think you’ll find there are a number of times when you would end up arriving at a different story — validating a story instead of beginning design work, for example. If we were to do this more strictly, we’d eventually find that we gained a base comfort level in all areas of the application, which is a better position to be in that a group of specialists.</p>

<p><strong>Conclusion</strong></p>

<p>Consider this email <em>food for thought</em>. During Beta, I’ll continue to point out process violations and work with team leads to resolve them.</p>

<p>Regards, <br />
Chuck</p>

</div>

There are a couple of things to mention about this. I think this email was effective, because I overheard people using this analogy to explain problems. I really like to connect abstract flows like software delivery to everyday experiences.

Also, there are exceptions to the advice given above. For example, some stories of certain classes of service like defects may not follow the same workflow as a standard story. Also, in certain edge cases, it might make sense to move a story backward across the Kanban board. But, for this audience, I didn't want to go that deep. I'll introduce those subtle nuances later.

This is the last post in this initial run of posts. I do intend to delve deeper into certain metrics and charts I'm producing as the project progresses.
