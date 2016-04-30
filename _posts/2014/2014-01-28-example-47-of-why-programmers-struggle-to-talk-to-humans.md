---
layout: post
comments: true
title: 'Example #47 of Why Programmers Struggle to Talk to Humans'
date: 2014-01-28 13:47:54 -07:00
categories:
- coding
- professional
tags: []
status: publish
type: post
published: true
---
My friend and fellow programmer Josh just walked over to my cubicle and asked if I had any disinfecting wipes. I opened my drawer, looked at the shelve, said "yes" and closed the drawer.

He looked annoyed for a moment, until I said, "I believe in [Command/Query separation](http://martinfowler.com/bliki/CQRS.html). He smiled and then said, "May I have one, please?"

Command-query responsibility separation (CQRS) is a good data access pattern for complicated object domains, in which the way you search or query for data is kept separate from the way that you modify or run commands against the data. When you are just getting data, you don't need to worry about data integrity rules. In this case, I kept Josh from both asking whether I had disinfecting wipes and asking to have one in the same sentence.

However, I discovered today it's not a good pattern for human interaction. For simple domains like the everyday world, it's probably enough just to ask for one.
