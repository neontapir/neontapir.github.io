---
layout: post
comments: true
title: Solitaire Cipher
date: 2009-01-08 23:23:52 -07:00
categories:
- professional
tags:
- cipher
- lunch and learn
- solitaire

---
One of the things we do at work is "Lunch and Learn", a weekly seminar led by one of the development staff. Over the past few months, we've been doing the [Solitaire Cipher](https://www.schneier.com/solitaire.html). It was designed as a secure cipher operating with an ordinary deck of playing cards.

It was an interesting programming challenge, and a refreshing one for me. I hope to post some of the pertinent pieces of code soon. (As a parenthetical note, what public code repository solution would my readers suggest?)

I used a hybrid test-driven development, and found that it worked well for my style of coding. I'm beginning to use this thinking at work, where we're stubbing out interfaces, but using unit tests to explore their behavior.

Another thing these challenges are good for is providing a testbed for new technologies. Since we're taking a little more time with this one than usual, I'm going to expand my solution and make it a WCF service. I'm also going to implement the standard .NET framework cryptography hooks, including the ICryptoProvider interface and the SymmetricAlgorithm class.

If you're looking to do something similar at your workplace, or just for a challenge at home, we're cherry-picking through the [Ruby Quiz](http://rubyquiz.com/) list.
