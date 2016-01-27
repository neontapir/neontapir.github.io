---
layout: post
comments: true
title: 'Lean Wastes and Software Delivery: Overproduction and Overprocessing'
categories:
- process
- professional
tags:
- lean
- processing
- production
- waste
status: publish
type: post
published: true
meta:
  _yoast_wpseo_linkdex: '67'
  _edit_last: '5'
  _yoast_wpseo_focuskw: overproduction
  _wpas_done_all: '1'
  _wpas_skip_28796: '1'
  _wpas_skip_4335974: '1'
  _wpas_skip_5821802: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1438194143;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1309;}i:1;a:1:{s:2:"id";i:1291;}i:2;a:1:{s:2:"id";i:1312;}}}}
author:
  login: Chuck
  email: neontapir@gmail.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
excerpt: !ruby/object:Hpricot::Doc
  options: {}
---
[![bronze-rose](/assets/bronze-rose-300x223.jpg)](/assets/bronze-rose.jpg)

It’s an all too common story in software delivery shops. How many times have you heard about a delivery team who writes a feature for an application, but there is a delay in release? This is overproduction, producing more than the next step needs. While it may not seem like this is a problem, it can cause issues.

For example, let’s say that the team upgrades a code library they use to a new version, because it lets them get rid of some data validation they wrote themselves that is now handled by the library. It’s Halloween, and the product is released quarterly. In a workplace version of trick or treat, a critical defect is reported against the software version that’s deployed in production.

Not only does the delivery team have to reproduce the error in the deployed version, they need to also reproduce the error in the new version. They need to know if the new version exhibits the issue. If it does, they can discuss the possibility of just deploying the new version. If not, they know they will also have to address it in the new version before they can release it. Either way, it is more work to diagnose the defect than it would have been with a single version of the codebase.

To minimize the chances of this happening, the firm should work toward **continuous delivery**. Continuous delivery is a powerful technique that requires a number of disciplines to be in place. The most common stepping stone is continuous integration, which refers to building an application from source control automatically, usually any time a code file changes. Of course, this presupposes the team uses a source control system! And for those builds to be useful, some assurance of quality is needed, which comes from automated tests. Fortunately, firms can reap benefits from each one of these techniques in isolation, so it’s not a large upfront investment, but rather a number of small investments over time.

Some customers are sensitive to changes. For example, customers may train their employees on new product features every quarter. It would be nightmarish for them to continuously retrain their staff! For those situations, delivery teams need to practice accretion of features, where additive changes are strongly preferred and breaking changes are avoided at all costs. Many firms that excel at continuous delivery insist that the features they develop can be activated or deactivated with a configuration setting. That way, the pieces that make the feature work can be deployed without any customer knowledge until the feature is turned on. Or they may pursue a plug-in architecture, where features can be deployed as separate code modules when they are completed.

Let’s take another example, reports. It is not uncommon for a particular report to be commissioned for a purpose, and after the purpose has been fulfilled, it goes unused but still produced. The typical dynamic I see is that Product actively pursues addition of features, but Development heads efforts to remove features.

Duplicate data is another common area for overproduction. I recently saw one firm where Team Bravo got Team Alpha to build a service that allowed it to extract data from the Alpha application’s database. On the surface, the use case made sense. In reality, though, Bravo was calling the service to extract gigabytes of data into the Bravo database, along with gigabytes of separate data from Team Charlie in order to make a unified report. It turned out that over 90% of the load on Alpha’s database was from Team Bravo, and that there were simple filtering changes to the extract service that would have greatly reduced the duplicate data. Many data analysts are probably shaking their heads as they read this.

An approach to addressing this is **whole team** thinking, not just at a **feature team** level, but extending to portfolio management as well. There are a number of frameworks that try to address scaling agile. I’ve found that the scaled agile framework (SAFe) is a good conceptual starting point, though I would advise teams to investigate other options before choosing an approach.

### Overprocessing

Overprocessing is processing that doesn’t add value. In the world of software, this is known as "goldplating": creating features or implementations that go beyond the requirements. I see this most often in places that don’t practice **whole team** when it comes to requirements. Whole team is a concept where the entire team is responsible for the software development lifecycle. Everyone gets input in all parts of the process. When Product, Development and Operations are divided, sometimes the requirements don’t well reflect all the work that’s needed to produce a product. This opens the door for overprocessing.

One example I see is a misunderstanding of the value provided by each discipline practices, such as Development’s testing infrastructure. In places where Product has sole ownership of requirements, I’ve seen teams fighting for testing facilitation features, such as whether to include interfaces for making sure a service has deployed correctly. Having left out these features, I then see Product complain because it’s difficult to troubleshoot the application in production. Operations can be a powerful ally in these discussions, but they aren’t often at the negotiating table. Operations can also help ensure that proper security or monitoring considerations are introduced early.

Sometimes, developers foresee that a simple implementation of a feature won’t handle anticipated future use cases. It can be hard to resist the temptation to code a more robust solution right away, even though that future use case may not materialize for months or years, if at all. This often happens during the phase in a developer’s career when they are learning design patterns and they try to apply them in places where they aren’t appropriate. Then, they learn about enterprise architecture patterns and the cycle repeats. Or they learn about a new technology. This impulse toward fresh thinking is perfectly normal and should be encouraged, but at the same time, the needs of the product need to outweigh incorporating new technology simply for newness' sake.

I’ve seen Operations guilty of this too, for example in the realm of virtualization. When this technique of replacing physical machines with software images running in a machine emulator is new, there can be a drive to lower opertional costs by virtualizing everything. There have been a couple of times now where I’ve seen Operations ignore Development and virtualize a performance-critical piece of hardware, only to undo it later. I’m thinking of a couple of database and version control servers here, both of which needed a lot of memory and did a lot of disk and network I/O.

In another case, I saw Product insist on tight security for an application. Development did not communicate the performance costs and responded with a service oriented architecture solution that was unacceptably slow from doing a two-way security certificate authentication on every service call — for a real world analogy, imagine your house and having to unlock a door every time you wanted to walk into another room — but it was also hard to onboard clients. The burden was akin to having to install a security certificate on every laptop that wanted to do a Google search, and Operations balked at the idea of having to manage all those certificates on machines they didn’t control. While that level of security might be appropriate for some applications, it was deemed far more robust than the application in question needed.

When Development and Operations are not working together, sometimes problems are handled in an overly complicated manner. In one case, Operations had written front-end scripts and even patched Development programs in production without letting Development know. Predictably, this led to odd defects in production that couldn’t be reproduced in test environments, as well as increasing reluctance to put new versions into production — because it would mean development work by Operations to update their adaptations of the system! When Operations and Product work together, the need to cobble solutions like this together is greatly reduced and those rare instances tend to last only until a new version can be deployed.

I have also seen goldplating occur when there has been turnover in Product, and the development staff have a lot of experience with the product. Senior developers sometimes develop the feeling that they know the customers better than the product team does, and they know they would like some feature they dreamed up. Here, Product disciplines like the business model canvas, value mapping and other techniques should be applied, to evaluate those ideas from Development and Operations against the market and target customer base.

Another example is when Product and teams spend lots of grooming time fleshing out stories, only to decide that the work item won’t be played — that the outcomes requested won’t be produced. Paragraphs and charts may be created when a sentence would do. And although the discussions may have lasting impact on the direction of the product, much of that brainpower talking about potential future issues like implementation details goes to waste. It’s important to groom epics, features, stories and tasks to the appropriate level of detail for their state in the delivery lifecycle.

In summary, having a good process for incorporating Product, Development and Operations into the feature discussion can alleviate overprocessing. A healthy discussion between these three groups implies a level of mutual **trust**, because distrustful parties will tend to discount each other’s input. A whole team approach can help build that trust faster.

An early step in that direction is use of **feature teams**. Companies that try to preserve silos and handoff work between departments impede frequent feedback, which is a tenet of all agile processes. If this concept is new to your work environment, experiment with a single **colocated** team with the firm’s goal being for the three group to learn how to work together.

I hope you enjoyed this series!
