---
layout: post
comments: true
title: Bowling Game kata with Express and Node.js
categories:
- coding
- professional
tags:
- express
- kata
- node.js
- restify
- supertest

---
![bowling](/assets/bowling-300x225.jpg)

Last time, I talked about the [Bowling Game kata in Node.js]({% post_url 2014-01-08-bowling-game-kata-using-node-js %}), and mentioned that the next step in looking at the [MEAN stack](http://www.mean.io/) is [Express](http://expressjs.com/), which is a JavaScript web application framework.

The inclusion of Express means that the game scoring will need to be exposed as a web application. This seems like a good use case for [REST](http://en.wikipedia.org/wiki/Representational_state_transfer). I'm aware that [restify](http://mcavage.me/node-restify/) is a better fit for this kind of application, but in keeping with exploration of the MEAN stack, I stuck with Express. In doing some more exploration with Restify, I found that it needs the node development environment to be installed on Windows, which I found off-putting.

For testing, I used [supertest](https://github.com/visionmedia/supertest‎), which offers nice functionality for testing HTTP servers with a [fluent interface](http://en.wikipedia.org/wiki/Fluent_interface), another programming technique that I'm fond of.

Here's a sample of what the tests look like:

{% highlight javascript %}
 var request = require('supertest'),
 should = require('should');
 var game = require('../game.js').app;

var assertScoreEquals = function(expectedScore) {
 request(game).get('/score').expect(200).end(function(err,res) {
 result = res.body;
 result.should.have.property('score').eql(expectedScore);
 });
 };

var roll = function(pins) {
 request(game).post('/bowl/' + pins).end();
 };

var rollMany = function(times, pins) {
 for (var i = 0; i < times; i++) {
 roll(pins);
 }
 };

describe('Scoring a bowling game', function() {
 beforeEach(function() {
 request(game).get('/start').end();
 });

describe('gutter game', function() {
 it('should return 0', function() {
 rollMany(20,0);
 assertScoreEquals(0);
 });
 });
 });
 {% endhighlight %}

The supertest library is what provides the `request` object. Whenever you call `request`, you need to execute it with an `end()` call. I fumbled with this for a few hours. You'll notice that I'm ignoring the error object. I found that when I tried to use it, not only did it clutter up the test code with a `done` callback:

{% highlight javascript %}
 describe('gutter game', function() {
 it('should return 0', function(done) {
 rollMany(20,0);
 assertScoreEquals(0, done);
 });
 });
 {% endhighlight %}

but I also found while running in a `mocha -w` loop, it caused Mocha to throw exceptions after some time elapsed. I need to dig into this deeper.

Here's the game code, using Express to expose some REST endpoints for knocking down pins and scoring the game:

{% highlight javascript %}
 var express = require('express');
 var app = exports.app = express();

app.get('/start', function(req,res) {
 rolls = new Array();
 ball = 0;
 });

app.post('/bowl/:pins', function(req,res) {
 rolls[ball] = parseInt(req.params.pins);
 ball++;
 });

app.get('/score', function(req,res) {
 var total = 0;
 var ball = 0;
 for(var frame = 0; frame < 10; frame++) {
 // omitted, the scoring algorithm
 }
 res.send(200, {score: total});
 });

app.listen(process.env.PORT || 3000);
 {% endhighlight %}

As you can see, while the plumbing is more complicated, it uses the same structure as the pure Node.js solution. That's why I find tools like the Bowling Game kata to be valuable. By solving a problem I've solved many times before, the problem fades into the background and I'm able to focus on learning the language.

The next step is to include [AngularJS](http://angularjs.org).
