---
layout: post
title: 'Lean Wastes and Software Delivery: Wasted Inventory'
date: 2014-02-05 18:56:40.000000000 -07:00
categories:
- process
- professional
tags:
- inventory
- lean
- waste
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
<img src="/assets/inventory-300x225.jpg"/>

In manufacturing, any piece of work that is ready for the next step   might be
considered inventory: finished goods, works in progress, and   even raw
material.

For a software delivery team, it’s hard to measure inventory. For some   teams,
they are done with a feature when it is checked into source   control. For
others, they are done when they have delivered build   artifacts. A team’s
definition of done comes into play here. A   definition of done can be thought
of as a list of characteristics of   completed work. One common example is that
all new functionality is   covered by unit tests. If Team Bravo tells me a
feature is done, then I   can assume that if I ask to see unit tests that
exercise the new   feature, Team Bravo can point me to them.

Whether the finished product is code or binaries, until that deliverable   is in
the hands of customers (internal or external), the producer earns   nothing from
producing it and thus that code has a potential to be   waste. Firms don’t pay
teams to produce code, they need their customers   to pay for the features that
are realized by that running code. And I’ve   been on teams producing a feature
that was cancelled or shelved before   delivery.

Before the advent of distributed version control systems like Git and
Mercurial, source control systems used to store a full copy of each file   being
monitored. In systems like those, branching was expensive in terms   of time and
disk space. Keeping dorment branches beyond their usefulness   was a form of
waste. Even using Git, I recommend that teams utilize tags   and remove inactive
branches, because branches are easy to recreate.

Still, having seen the contents of many of my colleague’s "temp"   folders,
teams need to be disciplined about cleaning build and work   artifacts — for
example, sample production data used to diagnose an   issue solved months ago.
Often these files can be huge, which makes them   poor candidates for a version
control system. Teams should take the time   to set up a **shared file system**
for such files, so that a hard drive   failure on Keith’s machine won’t start a
panic. Free options like Box,   Dropbox and SugarSync might suffice for small
shops, enterprise   solutions like Amazon S3 also exist.

Developers also experiment on their machines, and it’s easy for those   machines
to become tainted by unusual software installations as well as   experimental
and debug versions of code libraries. Having a **continuous   integration**
system can help protect against unwitting building a   environmental dependency
into your software. I say from experience that   you don’t want to be a position
where you need to keep a departed   developer’s machine up and running on the
network because it’s the only   place a piece of production code will compile.

For every group that produces an output (code library, software package, what
have you), they require a set of inputs. Software is built from raw materials,
but instead of physical items programs are built from ideas. **Backlog
grooming** is analogous to a crude oil refinery, substituting ideas for crude
oil and requirements for gasoline.

If a team does not have good discipline around its backlog, much like   those
"temp" folders above, there will be items in the backlog that   won’t see the
light of day in the near future. Ideas that are no longer   relevant, or as some
say have been "overtaken by events". Ones that   aren’t commercially viable.
Defects that don’t apply anymore. If the   backlog gets months long, you may
find that people create new stories   and features that duplicate ones already
in the backlog.

Whether it’s the team that decides what to do next or a product owner,   each of
those items needs to be reevaluated. This accumulated time   reviewing stale
features is wasteful. Teams should strive to keep their   backlogs trim. Really,
as long as there is always one single thing more   to do, the team can continue
working, so teams should keep their   backlogs as small as possible without
running dry. A kanban board can be   of immense help in planning workflows like
this.

Next installment is wasted motion and transportation.
