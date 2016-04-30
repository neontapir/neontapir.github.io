---
layout: post
comments: true
title: 'Excel spreadsheet for metrics: a Kanban experience report'
date: 2014-06-19 07:44:40 -06:00
categories:
- process
- professional
tags:
- chart
- day
- kanban
- lead
- story
- week
status: publish
type: post
published: true

---
This is the third in a series of blog posts about implementing Kanban on my current project. The first installment was about [establishing the flow](% post_url 2014-06-05-establishing-flow-kanban-experience-report %). The second described the [Rally data extract scripts](% post_url 2014-06-12-rally-data-extract-scripts-kanban-experience-report %) I wrote. In this post, I talk about my Excel spreadsheet that consumes the data.

![abacus](/assets/abacus-300x300.jpg)

All of the data exists on a "Stories" tab. I collect the formatted ID, the date the story first entered each state, and the lead developer and quality engineer. When a story is Accepted or Rejected, I run the story query script and input that data.

I also do some data normalization. For example, my story query script does not take weekends and holidays into account, but the spreadsheet does. Neither team currently does story size estimation, but I derive a story's size by taking the total number of hours the story was being worked and apply each story to the typical story point Fibunacci sequence using a Bell curve. Values like holidays and the story point sequence exist on a Lookups sheet.

With this data, I can calculate a number of interesting metrics. The data from the Stories worksheet is aggregated onto the Days worksheet, and Days onto both the Weeks and Days of Week worksheet. These populate charts like the [Continuous Flow Diagram](http://brodzinski.com/2013/07/cumulative-flow-diagram.html). I took the Accepted stories data from the CFD and some [Takt time](http://en.wikipedia.org/wiki/Takt_time) calculations to project future delivery.

> This calculation became invaluable during week three and four of the first milestone release. I was able to tell the team that they need to get 4 stories accepted a day in order to reach the milestone goal. We ran into a blocking issue, and we got up to 5-6 stories per day. The team responded by swarming on the roadblock and collaborating to shepherd the logjam through the system and got us back on track.
>
> While many individuals worked many late nights, we only had one mandatory evening of work on the last night of the project. Fueled by pizza, we solved our last integration challenge and were done by 8pm. To me, this made all the hours of work developing the spreadsheet and time putting in data worthwhile. I think if the team hadn't rallied when they did, the last week before delivery would have been very painful indeed.

I'm also breaking down story data by dev lead, QA lead, tag and location. While I'm aware of the potential uses of individual performance data, so far there are no strong patterns to observe. I get dev lead and QA lead from the senior person who's making changes in Rally. My heuristic is a workaround for the limitation that a story in Rally can only have a single owner. We change the owner of the story during its lifecycle on the board to know who to talk to about the story at any given time.

Originally, the Tag field was going to be used to slice data by Rally tag, but I ended up using it to track work by component. I parse story titles to determine what component(s) they affected. Again, not ideal, but good enough for now.

I also look at other daily metrics. I monitor the number of story changes made per day, for example, to see how active the team is.

![day-of-week-chart](/assets/day-of-week-chart-300x165.png)

As you can see, stories are most active on Tuesdays. Early in the project, there was a spike on Thursdays as well, but over time, that's dampened.

I look in changes in key metrics over time. For example, I see wide fluctuations in the amount of development time, but much steadier validation times over the life of the project.

Next time, I'll talk about Kanban flow process violations.
