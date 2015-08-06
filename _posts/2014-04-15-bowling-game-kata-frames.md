---
layout: post
title: Bowling Game kata and frames
date: 2014-04-15 15:34:50.000000000 -06:00
categories:
- coding
tags:
- implementation
- junit
- kata
- test
- unit
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
I ran into an interesting scenario after revisiting the Bowling Game kata from memory. The exercise was a small reminder of the power of test-first development.

I worked through the kata as usual, but I was unable to recall each step, so I wrote the code fresh. I came to the following implementation, which passes the normal JUnit tests:

{% highlight java %}  
public int score() {
 int score = 0;
 for(int i = 0; i < 20; i++) {
   if (scores[i] == 10) {
     score += scores[i+1] + scores[i+2];
   }
   else if (scores[i] + scores[i+1] == 10) {
     score += scores[i+2];
   }
   score += scores[i];
 }
 return score;
}
{% endhighlight %}

I realized that I'd forgotten to support the notion of frames. An example is the logic for 10 pins. A strike only occurs when the 10 pins are knocked down in the first try in the frame.

Unit tests are only as good as the use cases they cover. Because I hadn't written a test that implemented the "strike" business rule, I had a faulty implementation.

Fortunately, it's easy to resolve this situation with test-first development. Here's the failing test I used to exploit this design weakness:

{% highlight java %}
 @Test
 public void spareWithTenPins() {
   g.roll(0);
   g.roll(10); // spare, not strike
   g.roll(2);
   g.roll(1);
   assertEquals(15, g.score());
 }
 {% endhighlight %}

Next, I fixed the implementation to take attempts in pairs -- that is, a "frame" -- and the `spareWithTenPins` and other tests passed. Here's the new `score()` implementation:

{% highlight java %}
 public int score() {
   int score = 0;
   for(int f = 0; f < 10; f++) {
     int i = f * 2;
     if (scores[i] == 10) {
       score += scores[i+1] + scores[i+2];
     }
     else if (scores[i] + scores[i+1] == 10) {
       score += scores[i+2];
     }
     score += scores[i] + scores[i+1];
   }
 return score;
 }
 {% endhighlight %}

It's worth noting that this is not clean code -- I'm not using variables with intention-revealing names, for example. I found that I was somewhat lax about the refactoring step when performing this kata today.
