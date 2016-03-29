---
layout: post
comments: true
title: 'Establishing the Flow: a Kanban experience report'
date: 2014-06-05 07:29:17 -06:00
categories:
- process
- professional
tags:
- development
- experience
- git
- kanban
- Rally
- scrum
- Stash
- state
- team
status: publish
type: post
published: true
author:
  login: Chuck
  email: neontapir@gmail.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
![simple-kanban-board](/assets/simple-kanban-board.png)

To my mind, Kanban the process is a good fit for managing software projects in a startup situation, like we have at my current employer. In his book _The Lean Startup_, Eric Ries talks about the importance of build-measure-learn feedback loops. Kanban supports the measure phase of this feedback loop through rich metrics.

> I'd like to preface this blog series by saying that it's only been eight weeks since Kanban was applied in earnest on this project, and while I've done this before, examples should not be taken as a definitive statement of best practice. In fact, there are a number of places where potential improvements are obvious. Note also that this project has a very aggressive delivery timeline and that date has limited the number and scope of improvements the team is willing to undertake.

On this project, we have about 10 people here in Colorado and another 20 contractors in eastern Europe. If we were using scrum, I'd be a scrum master to all those teams, as well as a "release train engineer" in SAFe parlance. I'm honestly not sure what the analogous role is called with Kanban teams, since many Kanban teams are self-managed. Because project manager has a specific meaning at my employer, the best title I've come up with is "project coordinator" or maybe "technical project manager" (although that title has baggage too).

When I was tasked with implementing Kanban for this project, I started by talking to the team about workflows they have enjoyed using in the past. I used the [getKanban](http://getkanban.com) game to illustrate how a well-considered Kanban flow operates, and the team still talks about the game. We ended up adopting a similar flow to getKanban's for our backend team.

*   In getKanban, the states are: Ready, Design Doing, Design Done, Development Doing, Development Done, Test, and Deployed.
*   For our backend team board, we chose Ready, Design, Development, Validation and Accepted.
*   The front-end team chose different states: Ready, Requirements, Wireframes, Data Contracts (where we identify API changes and groom stories for the backend team), Proof of Concept, Production Ready, Validation, and then Accepted.

> There was a lot of confusion about the Proof of Concept and Production Ready columns, which I renamed after the first delivery milestone to Development and Deployment. I'm also finding that stories on the front-end board don't spend significant time in Wireframes or Data Contracts, so I'm considering consolidating Requirements, Wireframes and Data Contracts into a "Design" step.

I spent time with both teams establishing some exit criteria for each step in the workflow. On the backend board, stories exit Ready when they are groomed, including acceptance criteria and test scenarios. During Design, the developer, often in partnership with a quality engineer, comes up with test suites and a high-level design approach, at least to the component and API level. Then, during Development, they create the implementation as well as any [JUnit](http://junit.org) and [FitNesse](http://www.fitnesse.org) fixtures needed to exercise their code. After a code review, the story enters Validation where the functionality is exercised by FitNesse as well as ad-hoc testing. Then, the PO accepts the story. Should we decide at some point that the story is no longer desired, it gets moved to Rejected.

> In practice, team members often break these exit criteria, and we went through a couple of weeks of blocking stories that didn't pass muster. I found this was an effective way to get the team to pay attention to exit criteria. With a team this large, it's hard to get everyone together at once. I discovered that I underestimated the communications effort -- both in terms of a Russian/English language barrier as well as need for repetition.

We use [`git`](http://github.com) for source control, specifically the Atlassian server project [`Stash`](https://www.atlassian.com/software/stash), which allows us to keep our code behind our firewall and to use LDAP for user access. We use pull requests for code reviews, because Stash offers similar reviewing capabilities to [github](http://github.com).

> The eastern European team is used to `Subversion` and new to `git`, and that's caused some confusion with branching strategies. When one team reported they were spending man-days handling merge conflicts, I suspect it is either because of the way they handle branching or how they have configured git. In my experience, after some explanation, merge issues of this magnitude arise much less frequently with git. The tiny size of our initial code base is also a contributing factor -- there is a lot of contention for certain key files. I've challenged the team to dig into why that file and the code it contains are involved in so many of our features to make sure they are avoiding creating a [God object](http://en.wikipedia.org/wiki/God_object) or the like.

The next post digs into the data collection aspect of a Kanban flow. Later posts talk about my Excel spreadsheet that consumes that data, what metrics I pull, and process violations.
