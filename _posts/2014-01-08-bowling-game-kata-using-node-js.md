---
layout: post
title: Bowling Game kata using Node.js
date: 2014-01-08 09:15:52.000000000 -07:00
categories:
- coding
- professional
tags:
- kata
- node.js
- should
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
excerpt: !ruby/object:Hpricot::Doc
  options: {}
---
[![bowling](assets/bowling-300x225.jpg)](http://neontapir.com/wp/wp-content/uploads/2014/01/bowling.jpg)

At work, my team is working on building commodity functionality for a SOA network of services. While learning more about SOA, I've become interested in [Node.js](http://nodejs.org‎), a JavaScript library that makes it easy and quick to build network applications.

When I'm first learning a language, one of the first projects I tackle is Bob Martin's [Bowling Game kata](http://butunclebob.com/ArticleS.UncleBob.TheBowlingGameKata). I've written about [code katas](http://neontapir.com/wp/2012/08/code-katas/) before, suffice it to say I still think they are a valuable learning tool. When learning a new language, one of the first questions I want to answer is how to unit test my code, and this kata presents a fairly simple problem that's well-suited to test-first design.

So, I coded up a solution to the kata using node.js. There are plenty of examples on the web already, but I didn't use them directly. I fumbled around with node.js for a while, then I went looked to improve my knowledge of the language's facilities and constructs.

I used [Mocha](http://visionmedia.github.io/mocha/‎) as my test framework. I discovered after a while that Mocha has a mode where you can have Mocha watch a folder for changes and execute tests using `mocha -w`. I find the instant feedback of continuous testing to be very valuable.

I started with `assert` for testing, but ended up choosing [should](https://github.com/visionmedia/should.js/), because I prefer BDD-style syntax when making assertions. Here's a representative sample, taken from early on in the kata:

{% highlight javascript %}
 game = require('..\\game.js');
 should = require("should");

var rollMany = function(times, pins) {
 for (var i = 0; i < times; i++) {
 game.roll(pins);
 }
 };

describe('When scoring a bowling game', function() {
 beforeEach(function() {
 game.reset();
 });

describe('all gutter balls', function() {
 it('should score 0 for 20 gutter rolls', function() {
 rollMany(20, 0);
 game.score().should.equal(0);
 });
 });
 });
 {% endhighlight %}

With assert, the assertion would look like:

{% highlight javascript %}
 assert.equal(game.score(), 0);
 {% endhighlight %}

For simple assertions, assert is legible. However, for more complicated ones, I find that BDD-style syntax more naturally expresses what I'm verbalizing as I construct the test.

The code to actually perform score the game is (game.js):

{% highlight javascript %}
 module.exports.reset = function() {
 rolls = new Array();
 roll = 0;
 };

module.exports.roll = function(pins) {
 rolls[roll] = pins;
 roll++;
 };

module.exports.score = function() {
 var total = 0;
 var ball = 0;

var isStrike = function() { return rolls[ball] == 10; };
 var strikeBonus = function() { return rolls[ball + 1] + rolls[ball + 2]; };
 // other helpers

for (var frame = 0; frame < 10; frame++) {
 // omitted, the scoring algorithm itself
 }
 return total;
 };
 {% endhighlight %}

I've removed the algorithm in case you'd like to code it yourself. I will say it took quite a while to get the hang of all the parentheses and curly bracket nesting. Before doing this kata, I didn't often touch JavaScript and would often mess this up the first time. Afterward, it became natural.

I did have some trouble understanding how modules expose methods and variables until I read [How to Use Exports in NodeJS](http://blog.liangzan.net/blog/2012/06/04/how-to-use-exports-in-nodejs/), which I found concise and informative.

After I got this kata under my belt, I started doing more research and getting interested in the [MEAN stack](http://www.mean.io/) (MongoDB, Express, AngularJS, and Node.js). Next time, I'll show the kata with the inclusion of Express.
