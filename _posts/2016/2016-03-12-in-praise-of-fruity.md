---
layout: post
title: In Praise of Fruity
date: 2016-03-12 19:30:00
categories:
- professional
tags:
- code
- benchmarking
- performance
- approaches
---

{% include side-image.html image="grapefruit.jpeg" caption="Not the Fruity logo, but I like grapefruit" %}

Another tech review, this time a Ruby library. [Fruity](https://github.com/marcandre/fruity) is
a library for performance testing. You have probably heard of its better-known
cousin, [Benchmark](http://ruby-doc.org/stdlib-2.2.0/libdoc/benchmark/rdoc/Benchmark.html).

When I'm interested in benchmarking, it's usually for small methods. I'll think
of a different way to approach a problem, and then the thought will occur to me,
"But is it performant?" Fruity is ideal for these kind of situations. But why
might I want to import a library when Benchmark is built in?

Let's take a recent example. I was working through the Minesweeper exercise on
[Exercism.io](http://exercism.io). I was thinking if there was a better way to
make sure my Minesweeper grid didn't have any illegal characters in it. The
first way was to convert an array of characters into a string, then to use
`count` to make sure the count of all unwanted characters was zero.

After I finished the exercise, I thought about another way. The `Array` class
has an intersection operator `&`. If I used that, I wouldn't have to convert the
array to a string and maybe save some cycles.

When I'm wanting a Ruby sandbox, I turn to [Pry](http://pryrepl.org/). I don't
use most of Pry's features, but I like it over IRB for its better syntax
highlighting.

First, some test data:

    [9] pry(main)> xyzzy = ['x','y','z','z','y']
    => ["x", "y", "z", "z", "y"]
    [10] pry(main)> good = ['+','|','*','1','2','3','4',' ','-']
    => ["+", "|", "*", "1", "2", "3", "4", " ", "-"]

Here's a performance comparison using Benchmark:

    [15] pry(main)> n = 100000
    => 100000
    [16] pry(main)> Benchmark.bm do |x|
    [16] pry(main)*   x.report { xyzzy.join.count('^+|*1234 -') == 0 }
    [16] pry(main)*   x.report { xyzzy & good == xyzzy }
    [16] pry(main)* end
           user     system      total        real
       0.000000   0.000000   0.000000 (  0.000007)
       0.000000   0.000000   0.000000 (  0.000012)
    => [#<Benchmark::Tms:0x007fff0326ce38
      @cstime=0.0,
      @cutime=0.0,
      @label="",
      @real=7.4260024121031165e-06,
      @stime=0.0,
      @total=0.0,
      @utime=0.0>,
     #<Benchmark::Tms:0x007fff0326c4d8
      @cstime=0.0,
      @cutime=0.0,
      @label="",
      @real=1.1732001439668238e-05,
      @stime=0.0,
      @total=0.0,
      @utime=0.0>]

Note that this output is a little cryptic. It does tell me that the first way
is faster, but I need to do a little work. I had to think about the number
of iterations I wanted for the test. And, I had to do some mental math to
figure out the real answer I wanted, which is "which one is faster and by
how much?"

Now, let's have a look at Fruity:

    [11] pry(main)> compare do
    [11] pry(main)*   count { xyzzy.join.count('^+|*1234 -') == 0 }
    [11] pry(main)*   intersect { xyzzy & good == xyzzy }
    [11] pry(main)* end
    Running each test 2048 times. Test will take about 1 second.
    count is faster than intersect by 3x ± 0.1

Notice a few things about Fruity:

  * There's less boilerplate code
  * I was able to give each algorithm a name
  * I didn't have to specify the number of iterations. Fruity came up with an
  intelligent guess.
  * Fruity reported its results in relative terms

A simple test like this highlights a different in approach between Fruity and
other benchmarking tools. For more on that, take a look at the [project's README
on Github](https://github.com/marcandre/fruity/blob/master/README.rdoc). In
short, Fruity seeks to eliminate noise by not reporting insignificant
differences.

Fruity can do more than just anonymous methods, as I've shown here. It can
compare methods on a class or another kind of callable. It can also do
comparisons with parameters.

In cases like mine, clarity trumps precision. It's the difference between asking
LaForge and Data a question. I'd prefer some synthesis over a data dump (no pun
intended). Next time you're wondering about performance in Ruby, give Fruity a
try.
