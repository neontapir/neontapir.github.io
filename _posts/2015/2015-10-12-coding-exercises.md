---
layout: post
title: Testing Your Mettle
date: 2015-10-12 12:50:00
categories:
- coding
- professional
tags:
- interviewing
- exercise
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---

<img src="/assets/tools-wood-bench.jpg" style="float:right" /> When hiring for a
technical position, I like to give candidates a coding exercise to test their
**mettle**. In this post, I talk about traits to look for in coding exercises and
use those to discuss why coding exercises are useful.

Obviously, much of this advice would apply to a similar professional exercise
like a backlog grooming exercise for a prospective product owner, but I'm hiring
for developers at the moment, so that's the focus of this post.

## When to give the exercise

Normally, as the hiring manager, I'll talk to candidates about the position and
answer any questions they might have about the position. In the course of that
discussion about their background, the candidate and I jointly decide if the
position is worth pursuing for both of us.

I like to administer the coding exercise before the first team interview, which
I like to conduct in-person where possible. This gives the team and the
candidate something concrete to discuss during the interview. Otherwise, I find
that these discussions devolve into a resume review, which is less valuable than
"talking shop". With the results of a coding exercise in front of the team, they
conduct a code review with the candidate, which naturally leads to deeper
discussions, and also often elicits better probing questions from the candidate
about the position and the environment.

## Traits of Good Coding Exercises

### Clearly explain the end goal

I think it's crucial to let candidates know the philosophy behind the exercise,
and especially what aspects of the exercise they can ignore. In general, I ask
candidates to develop a few things well as opposed to many things poorly.

### Time-boxed

In general, candidates will be completing this coding exercise on their own
time. To be respectful of that fact, coding exercises should be time-boxed to a
reasonable amount of time. During my MBA classes, most exams that required
freeform responses lasted no more than two hours, and I think that's an
appropriate duration for a coding exercise also.

Having a time limit allows evaluators to compare candidates as well. While speed
is not the only criteria, it helps me compare candidates to people on my current
team and previous teams. If I'm trying to decide if a person is a junior,
intermediate or senior developer, it's useful to know what they can accomplish
given a new problem in a given amount of time.

The downside to this approach is that time pressure can cause some aberrant
behaviors, outside the normal stress of a job interview.

### Some scaffolding

This time pressure often means that I will provide some scaffolding. This allows
me to better target the exercise to whatever aspects of the solution I'm looking
to examine, as opposed to seeing if the candidate can create a new project
correctly. That's why some exercises I give are refactoring exercises instead of
new feature writing, so that the candidate has time to show me their design
chops without having to create all the necessary infrastructure.

It also allows me to illustrate how the candidate will fit into the team. For
example, if I'm hiring for a .NET developer on a team that has already has a
MS-SQL database developer, I will often work with said database developer to
provide a database schema with several useful stored procedures so that they get
a head-start and so they know they don't need to worry so much about databases
in this position.

On the other hand, if the candidate will be expected to work on SQL stored
procedures, I'll design the exercise to include a SQL component to signal that.
This exercise is as much about the candidate deciding if they want to work with
us as much as it is for me. In my experience, if they don't like SQL stored
procedures, they will either submit an alternative or bow out of the candidacy.

#### Require minimal extra setup by the candidate

A good coding exercise will focus on whatever technologies are needed for the
position, and will leverage a standard coding environment whenever possible. For
example, if I am interested in finding out the candidate's approach to coding in
Java, I avoid obscure libraries that would distract candidates.

Where possible, I use common industry tools like Git to distribute and evaluate
the exercise, because those are in heavy use by my team and it allows me to
ensure that a candidate can use them. When using Git, I collect answers as
patches rather than as a fork so that candidates can't look at each others'
work.

A word on the SQL example above: unless I expect that all candidates will have a
working SQL environment, I avoid technologies that require a lot of setup. I
want developer candidates to focus on showing their value, not their environment
setup expertise.

### Include some interesting decisions, appropriate to the level of the position

To me, a test like FizzBuzz is like a parlor trick. Many programmers know this
exercise, and the solutions don't vary much. Thus, they are like a Boolean test
of programming prowess: **can you program? (true/false)**. I liken a coding
exercise to an essay question rather than multiple choice, so I design meatier
problems to solve than can be handled by one method.

I also detail the outcome I expect to see, and these are the only clarification
questions I'll answer from candidates before submitting their answer. Unless I'm
interviewing for a junior position where a test that that might be appropriate
or where I expect to be giving detailed instructions, I like to give
instructions with the same level of ambiguity that the candidate can expect when
they join the team. This means that intermediate candidates can expect more
prescriptive objectives and more scaffolding than senior or architect candidates
(more on scaffolding later).

My coding exercises often include more work than can be done in the time allowed
(more on that later), to force candidates to make priority decisions. With more
senior positions, I even leave architectural or framework decisions to the
candidates, expecting that they have relevant experience to bring to bear. These
exercises often include some red herrings as well, to see if candidates can
deduce what portions of a system are important to an issue and those that can
safely be ignored.

In many cases, I suggest that senior candidate introduce their own features, not
only to see how they explain their feature but also to provide them a chance to
exercise their imagination. To me, coding has elements of art as well as
science, so a coding exercise would not be effective if there was only one
acceptable solution.

### Offsite, in comfort

One deficiency of whiteboard exercises where candidates work a simple coding
problem on a whiteboard is that they favor people who are socially extroverted
and quick to adapt to new circumstances. In my experience, people who excel at
whiteboard exercises and are a good social fit make for good team members.

However, whiteboard tests tend to provide false negatives for introverted
candidates, who may not be comfortable with the "thinking out-loud" component,
as well as for junior or intermediate candidates that are not confident in their
abilities. People tend to be concerned about syntax errors that an IDE would
immediate point out or even correct. I observe that many candidates are
self-conscious and don't produce their best efforts.

To mitigate this, I like to allow candidates to work on coding exercises in one
of two environments:

* the candidate's chosen environment, using their own equipment and setup
* as a pair programming exercise, in-person using their equipment when possible

While pair programming is my personal preference, it does require synchronous
timing between the evaluator and candidate. And, I'll admit, often the issue is
my schedule! Thus, I design my exercises for asynchronous use as a remote
exercise and administer in-person when I can.

### Conclusion

I hope you found this post interesting. If you'd like to see examples of coding
exercises I've given, have a look at my
[coding-exercises repo](https://github.com/neontapir/coding-exercises).
These two are in use for the positions I'm hiring for. If you'd like more
information on those positions, hit me up.
