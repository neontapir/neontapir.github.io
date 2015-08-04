---
layout: post
title: 'Lean Wastes and Software Delivery: Waiting and Defects'
date: 2014-01-22 18:41:51.000000000 -07:00
categories:
- process
- professional
tags:
- bottlenecks
- defects
- lean
- waiting
- waste
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
<div style="float: right; padding: 1em;"><img src="/assets/waiting-198x300.jpg" /></div>

Lean thinking comes from innovation in statistical process control. The idea is
that honing techniques leads to measurably better results. Lean identifies eight
"wastes", activities that subtract value from a process. They are:

*   wasted talent
*   wasted inventory
*   wasted motion of people
*   wasted time (waiting)
*   wasted transportation of goods
*   defects
*   overproduction
*   overprocessing

From the perspective of a software delivery project, some of these   wastes
don’t seem to apply. In this series of posts let’s focus on each   in turn,
starting with waiting and defects.

## Waiting and Defects

> I hate waiting.
>
> — Inigo Montoya, The Princess Bride

When people think of lean processes, the waste of **waiting** is usually   what
they have in mind. In software delivery processes, it can manifest   in a number
of forms. In software delivery, it turns out that techniques   that reduce
waiting can also reduce **defects**. Defects occur when   software doesn’t
behave as intended.

When a delivery team member joins the team, inefficiencies in the   onboarding
process can introduce waste. If they are also joining the   firm, the costs
steepen. Every moment that the new person spends not   adding value to the
product is waste from this perspective. Thus, it’s   important for the new
person to be integrated into the team as quickly   as possible. I recommend
paired programming to minimize this kind of   waste. Shadow a person who’s role
you’ll be filling. See what they do   and don’t do, and learn the new codebase
like you would a foreign   language, through immersion.

Okay, so all of the team is onboard. The next step is to look at your   product
delivery process for bottlenecks. In a lean process context, a   bottleneck is a
part of the process where flow is constricted. While   there may be a number of
inefficiencies in a system, the most severe   bottleneck will constrict the
entire system. Troubleshooting bottlenecks   is beyond the scope of this post,
but one of my favorite guides to the   process is the [Universal
Troubleshooter’s   Guide](http://www.troubleshooters.com/tpromag/9803.htm).

One of the many examples given is one of a bicycle, with the goal of   improving
your commute time of two hours. If you have a $75 coaster   break bike, what
keeps you from going faster — the bottleneck of the   system — is having just
one gear, which is poorly suited to hills.

For $150, you might get a mountain bike with multiple speeds that gives   you a
20% faster commute. Having removed the first bottleneck, the next   limitation
is wind buffeting from an inferior riding posture. A road   bike for $300 can
solve that bottleneck, which offers specialized tires   and a better riding
posture, yielding a 17% commute time improvement.

However, there is a point of diminishing returns. The next step up would   be a
mid-grade road bike, which overcomes the limitations of the   entry-level
components, but it only offers a 5% improvement for double   the cost at $600.
Other approaches like training or riding clothes   would likely yield better
results, which implies that at this point bike   components aren’t the
bottleneck.

With the bike example in mind, think about your software delivery   process.
From idea to requirements to design to implementation to   testing to customer
validation, where is the point that work tends to   pile up? That point is
likely to be the bottleneck. Lean process has a   lot of good guidance on
finding and removing bottlenecks, and it’s worth   exploring even if you are
using another agile methodology like scrum.   Once you identify the bottleneck,
there are techniques that can increase   delivery speed at each stage:

<table width="80%" frame="border" cellspacing="0" cellpadding="4"><colgroup><col width="25%"><col width="75%"></colgroup>

<thead>

<tr>

<th align="left" valign="top">Stage</th>

<th align="left" valign="top">Techniques</th>

</tr>

</thead>

<tbody>

<tr>

<td align="left" valign="top">

Idea to requirements

</td>

<td align="left" valign="top">

Backlog grooming, domain-specific language (DSL), working agreements

</td>

</tr>

<tr>

<td align="left" valign="top">

Requirements to design

</td>

<td align="left" valign="top">

Prototyping, behavior-driven development (BDD), domain-driven design (DDD), unified modeling language (UML)

</td>

</tr>

<tr>

<td align="left" valign="top">

Design to implementation

</td>

<td align="left" valign="top">

Paired programming, continuous integration (CI), version-control system (VCS), test-first development (TDD)

</td>

</tr>

<tr>

<td align="left" valign="top">

Implementation to delivery

</td>

<td align="left" valign="top">

Automated acceptance testing, continuous deployment

</td>

</tr>

</tbody>

</table>

Notes: "Paired programming" is usually "pair programming" though I prefer
"paired" because paired is a better adjectival descriptive of the activity than
the verb "to pair". Similarly, TDD is usually "test-driven" but I prefer
"test-first" because it more accurately sums up the philosophy of writing
software guided by tests.

**Backlog grooming** allows a product owner to engage a delivery team   during
story creation. These sessions offer teams a separation between   communicating
what the work is and deciding how to accomplish the work.   Product owner can
use the feedback on the newly-drafted stories to   refine the stories, address
the team’s questions and concerns, and use   the team’s rough size estimates for
release planning. Without backlog   grooming, these "what" and "how" discussions
both happen during   iteration planning. I’ve found mixing the two discussions
to be   inefficient, because the variations in design and other aspects of the
"how" are much larger if team members have different concepts of what’s   being
requested, and thus it takes longer to reach concensus.

Product owners and teams need a common trade language to bridge the gap
between business requirements and technical requirements, and the best   tool
I’ve found for this is **behavior-driven development** or BDD. I   prefer
Cucumber as a framework, which forms a **domain-specific   language** (DSL) or
jargon for communicating requirements. Each feature   and requirement are
expressed in a certain format, which programmers can   easily map to automated
tests.

This idea of a DSL can be extended further to the problem domain, which   brings
up a number of concepts from **domain-driven design**, especially   _ubiquitous
language_. It’s very helpful if the business experts use   terms the same way as
the technical staff. It helps them both understand   the problem space better.
While it’s true that domain-driven design   includes a number of tactical
technical patterns, it also contains a   number of strategic approaches for
modeling domains that are of use to   both business experts and delivery
technicians.

The same holds true of technical diagrams. Since there are so many ways   to
visually communicate information, it can take time and effort to   communicate
how symbols are being used. Use of a common standard like   the **unified
modeling language** (UML) can alleviate this. For people   who know the
language, the individual symbols fade into the background   and the focus
because the message they intend to convey.

Just as a ubiquitous language and UML can help smooth communications,
**working agreements** can help teams make decisions ahead of time.   Common
working agreements include a **definition of done** and a   **definition of
ready**. For example, as part of a definition of done,   if all team members
accept that a story isn’t ready to code until the   **acceptance criteria** are
defined — the things the product owner   expects to be true when the story is
ready for acceptance — then that’s   one decision that doesn’t need to be made
with every story. The   conversation shifts from "hey, do we need acceptance
criteria on this   one?" to "how will we show you that we’re done with this
story".   Rehashing decisions over and over is a form of waste. Teams should
only   revisit these agreements once in a great while or when something
changes.

**Prototypes** are a 21st Century version of the saying, "a picture is   worth
a thousand words". When exploring new applications, new technical
infrastructure or new approaches, prototypes can be very useful. They   offer an
environment for engineers to learn how best to leverage   technologies to
achieve a goal. Prototypes can also be useful to   business experts, who can get
some tactile feedback on their proposed   workflows. I know teams that use
prototypes even for established   applications to verify their understanding of
the requirements.

When working in a language that is as abstract as a computer programming
language, even the most expressive code can be challenging. **Paired
programming** is the most direct way for one delivery team member to
communicate low-level technical implementation details with another one.
Although it can be slower to implement a feature using paired   programming than
with a solitary programmer, studies have shown that the   code produced by a
pair contains fewer defects and that the majority of   defects are found during
code reviews. For a pair of programmers, code   reviews occur naturally and
continuously. Because mistakes are least   expensive to fix while the code is
being written, the overall time to   produce quality code is reduced by paired
programming.

Sitting next to another developer isn’t a luxury everyone can enjoy. I   know a
number of developers who pair remotely using a virtual network   computing (VNC)
tool like WinVNC and a telephone or get a second opinion   with a screen-sharing
tool like join.me or Skype. Many developers don’t   see it paired programming as
a luxury, but as a burden. For those   uncomfortable with the concept, a weaker
alternative that provides many   of the benefits is an interactive code review
in a conference room or   via software as above. For distributed teams, or teams
in a   meeting-heavy work environment, a source control tool like Git with
support for pull requests can provide a forum for asynchronous code   reviews.

**Continuous integration** (CI) describes a practical approach of
coordinating the work of multiple developers through the use of a common   code
location. It’s advantageous when that code location can track   changes, which
is why most developers make use of a **version control   system** (VCS) like
Subversion or Git. Originally made to help coders   collaborate, use of VCS has
expanded to [book
authors](http://web.archive.org/web/20131113121113/http://teach.github.com:80/articles/book-authoring-using-git-and-github/)
and even
[lawmakers](https://blog.abevoelker.com/gitlaw-github-for-laws-and-legal-documents-a-tourniquet-for-american-liberty/).

While a VCS can help contributors understand the evolution of a work   product,
it doesn’t include the ability to know whether the work product   changes are
productive. A CI tool like Jenkins or TeamCity automates the   process of
watching for changes and taking action, usually building the   software and
running automated tests. However, a CI server can be used   for other tasks,
like compiling code quality reports and building   documentation as well.

One of the more popular uses is for **continuous deployment**, in which   build
artifacts that pass automated tests are automatically deployed to   a test
environment for manual inspection. Or they set up deployment at   the push of a
button, so that long-running tests won’t be disturbed by   an untimely
deployment. And, in a world where it’s easy to deploy   changes or one where
there’s a ready failover environment, companies can   simply automatically
deploy to production, knowing that they can easily   revert if need be.

### Testing and Defects Reduction

Testing does not improve speed to market, a key reason why delivery   teams
sometimes sacrifice testing. In most cases, though, testing is an   important
discipline for agile teams, because quality code will improve   chances for
longevity in the market. Here, we are talking about two   primary kinds of
testing: unit testing and automated acceptance testing.   Both kinds of testing
are about delivering the right thing to customer,   not about delivering it
faster.

**Test-first development** is a tactical software development approach   that
ensures the programmer is the first user of the code being written.   Each unit
of code is exercised by I find that it quickly exposes   potential design issues
early, especially when it comes to consuming   objects.

In writing these "unit" tests, I sometimes find myself writing   boilerplate
code or having to always use certain objects in conjunction,   both of which can
indicate beneficial refactoring. I sometimes find that   I’m contemplating using
an object in a new or different way, which can   indicate a design flaw. I let
my intuition be my guide — there is a   difference between not writing tests
because they are uninteresting   (property getters and setters come to mind) and
not writing tests   because they are hard to orchestrate. I aim for 80% code
coverage by   tests, which gives me the benefits of TDD without imposing a
dogmatic   requirement to write uninteresting tests.

**Acceptance testing** is closely related to unit tests, but for many,   it’s a
separate discipline. Not only do developers want to know that   their new code
is working correctly, they want to make sure it   integrates with existing code
or systems. These tests have a different   audience, so they should be
considered separately. Whole books have been   written on this subject, please
see them if you want strategies for   agile testing, but it’s worth noting that
troubles found during   deployment or integration are still less expensive to
fix than after   shipment to the customer. Accordingly, it’s worth some effort
to reduce   defect escape rates with acceptance testing. For people who practice
BDD, their Cucumber specifications can easily be implemented as   acceptance
tests.

While tools like FitNesse and Cucumber can help with acceptance testing,   a CI
tool can be used to run them automatically. This allows software   development
teams to develop a "car dashboard" of their code health,   letting them know
whether it’s safe to proceed or time to pull into a   service station. Many
teams create working agreements for how to handle   failing builds or broken
automated tests.

Sometimes defects occur because a piece of software is working but is   hard to
use. **User experience** can help alleviate common data entry   mistakes like
clicking on the wrong button when two are placed too close   together, use of
confusing labels, obscured functionality hidden in   configuration menus and the
like.

Next installment, we'll examine wasted talent.
