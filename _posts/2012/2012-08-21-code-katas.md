---
layout: post
comments: true
title: Code Katas
categories:
- coding
- professional
tags:
- code kata
- coding
status: publish
type: post
published: true
meta:
  _sd_is_markdown: '1'
  _edit_last: '5'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1438144527;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:880;}i:1;a:1:{s:2:"id";i:1255;}i:2;a:1:{s:2:"id";i:1150;}}}}
author:
  login: Chuck
  email: neontapir@gmail.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
excerpt: !ruby/object:Hpricot::Doc
  options: {}
---
In my last post, I talked about [book clubs]({% post_url 2012-08-15-starting-a-technical-book-club %}). In it, I touched on code katas.

For a long time, I thought that code katas were puzzles that people solved together. I'll describe a few of those exercises in another article. Group coding exercises are fun but have different goals.

![Code Kata](/assets/IMG_0117.png)

### Katas

Katas are a concept from martial arts. I'll speak from a taekwondo perspective, since I have a second degree black belt. As a white belt, you start off learning some of the Korean terms we use in the _do-jang_ (gym) and a couple of basic stances. Next, we teach you how to punch coreectly and how to block a front kick, which is a common kind that's also taught to white belts. With these three moves, we teach a beginning exercise called four-direction punch.

It's not too exciting to watch, except as a parent of an enthusiastic white belt. (Or, watching a master do it.) These are the moves: you punch, you turn in stance, you block, you step forward and punch, and so on, until you've faced all four directions.

At first glance, it may not seem very useful to learn this. You can't compete in tournaments with it, and it won't save you in an altercation on the street. Alone.

Alone, it won't do those things. But, practiced regularly, an exercise will help hone your taekwondo. To do this exercise correctly, you need to punch just so, turn just so, land the stance just so, and block just so -- and you need to mean it. Crisp, precise, powerful technique is the demand.

### Katas, with Code

Code katas are the same. They involve simple goals, implemented the same way, over and over. [Jim Hood](https://twitter.com/hoodja) is the one who taught me the true meaning of a code kata.

Every morning, at a prescribed time, in a prescribed conference room, Jim leads people through the same kata. They work on speed, but not rushing. They work on test-driven development, not because they don't know how to implement the algorithm, but precisely because they do know how to write a prime number generator.

### The Benefits

Programmers should program code katas for the same reason that martial artists should practice their forms. The form drills the moves into your brain and into your muscle memory. When you are tired after the initial flurry of blows while sparring or when you distracted and caught unaware in a serious situation, you will not spend precious heartbeats thinking about how to respond. You will do what you've trained to do.

When you, the programmer, are stuck on how to implement the complicated business rules your product owner just explained to you, you want to implement well-designed, test-driven code. A code kata is the foundation for solid code implementations.

### Attributes of a Good Code Kata

I've already mentioned one example. The prime number generator is a good example. It's:

*   very small scope (one function)
*   stands alone, requires no infrastructure
*   can be covered by a handful of tests
*   can be implemented in 10-15 minutes

## Some Examples

The [Fizz Buzz Test](http://c2.com/cgi/wiki?FizzBuzzTest) is a staple of programming interviews, and it meets all our criteria.

The [Project Euler](http://projecteuler.net/) problems contain a number of candidates. Jim may have gotten his [prime number generator](http://projecteuler.net/problem=7) kata from here. [Prime composite factors](http://projecteuler.net/problem=3), [palindromic numbers](http://projecteuler.net/problem=4), and [Pythagorean triplets](http://projecteuler.net/problem=9) might also make good ones.

The [kata catalog on Coding Dojo](http://www.codingdojo.org/cgi-bin/index.pl?KataCatalogue) has a number of good problems to solve. The [Potter kata](http://www.codingdojo.org/cgi-bin/index.pl?KataPotter) and [Roman numerals kata](http://www.codingdojo.org/cgi-bin/index.pl?KataRomanNumerals) look promising.

These [15 exercises to know a programming language](http://www.knowing.net/index.php/2006/06/16/15-exercises-to-know-a-programming-language-part-1/) are good for learning a language, but I think they might be a little long for a code kata. If you have the time, though, these exercises being up important language concepts.

Peter Provost has a good [blog post about katas](http://www.peterprovost.org/blog/2012/05/02/kata-the-only-way-to-learn-tdd), in which he talks about them as a vehicle to learn TDD.

Do you have a favorite kata? Please share it in the comments.
