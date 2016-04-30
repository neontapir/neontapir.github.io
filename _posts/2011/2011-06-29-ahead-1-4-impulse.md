---
layout: post
comments: true
title: Ahead, 1/4 Impulse
date: 2011-06-29 07:06:00 -06:00
categories:
- professional
tags:
- project-management
- agile
- fail-fast
---

The new job is going well, which is to say we are failing fast. Just last night, we decided to revert four days of work because we didn’t like where an architectural choice was going.

I’m working on some software for the pharmaceutical industry, and I’m beginning to learn that drug management is a lot more complicated than picking cereal off the shelf!

We have a design document, which in some areas is really strong and in other areas is more like a problem statement than a proposed solution.

We have a prototype, but it’s more style than substance. For example, right now, the app structure is pretty flat. Flat is fine for a prototype, but not for the real thing.

(For the record, if you are working with WCF services, do not make one service per entity! We started trying to bring the responsibility of coordinating entity operations out of the UI into the domain services, and found it a morass of incompatible DTO namespaces. Whose Product object do you use: the product service’s, the stock shelf’s or receiving’s?)

So, until I get up to speed on the domain, my greatest value to the team is wearing my CSM hat. The team is new and there are a lot of agile practices that are new to these folks. There is a dedicated scrum master on the project (a first for me), and it makes more difference than I had predicted from what I’d read. But, he’s a project manager who’s a scrum enthusiast, whereas I have more field experience with scrum and three letters after my name, so I’m in a position to play the expert.

The main deviations from scrum are in the area of release planning. I was able to persuade the team not to do a 3-hour planning poker session for every user story we know. They only want an estimate accurate to the quarter, so who wants to be stuck with a moldy estimate by greenhorns on a story that will be tackled early next year, if at all? The analogy I used is it’s like a car repair estimate given in terms of unscrewing the oil cap, sticking in the dip stick, and so on. Given a do-over, I’d use the metaphor of prefab furniture assembly, but car repair got the job done.

Tasks have been a problem too. The technical lead of the project worries about things many people from traditional projects worry about. The vagueness of how tasks are selected or how detailed user stories are worry him. He’s worried about how code reviews will happen in an agile process, so I introduced the concept of the definition of done. I’m looking forward to defining done, because opinions range the gamut between “if it complies, it’s good” to a heavy process complete with gated check-ins, code reviews, code coverage, and so on.

Since I’m told this project has at least 16 months, I was told to resist “running up technical debt on the credit card”. I love that analogy. I have time to help the team develop strong TDD discipline, since they said they wanted it in one of their early retrospectives.

I love the team I’m on, I think we have the right people on the bus. And, I think we have a great product concept and the business and technical acumen to make it something special.
