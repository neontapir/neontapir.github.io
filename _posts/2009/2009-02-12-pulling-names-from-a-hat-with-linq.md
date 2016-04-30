---
layout: post
comments: true
title: Pulling names from a hat with LINQ
categories:
- professional
tags:
- code exercise
- development
- linq
- names from a hat
- programming
- random
- rng
- rubyquiz
- secret santas
- software
- takerandom
- word
- approaches
---
Each week at work, we have a Lunch and Learn sessions for developers. Sometimes, we assign a programming problem, and people solve it during the course of the week and present their solutions in the following session. Lately, even though we're a C# shop, we've taken to getting problems from [RubyQuiz](http://rubyquiz.com/). We've found them to be a good fit for us, as most of the problems can be solved to some degree within the two hours per week we're alloted for skill development.

We recently assigned the [Secret Santas problem](http://rubyquiz.com/quiz2.html). For those of you who don't know this Christmas tradition, some large families and groups have enough people that it is a burden to buy every other person a present. Instead, each person draws a name from a hat, and buys a present for just that person. The full problem description is at the Ruby Quiz web site.

Solving these problems isn't a serious challenge, but looking at the - approaches people take is fascinating.

The approach I liked best was my co-worker's, who used a ring. In real life, essentially he would had everyone form in a circle in a random order, and each person gave a gift to the person on their right.

I chose to put the names in a collection, and to use LINQ to pull random members from the collection. It turns out this concept can be rather useful, so I'm presenting it here. As with everything in this blog, it's released under the [Creative Commons Attribution 3.0 Unported](http://creativecommons.org/licenses/by/3.0/) license.

{% highlight csharp %}
using System;
using System.Collections.Generic;
using System.Linq;

namespace Domain
{
    public static class IEnumerableExtensions
    {
        //private static readonly RandomNumberGenerator RNG;
        private static readonly Random _random;

        static IEnumerableExtensions()
        {
            // 8 ms to initialize
            _random = new Random();

            // 650ms to initialize
            //RNG = RandomNumberGenerator.Create();
        }

        // ~80 ms/record
        private static int ChooseRandomIndex(int range)
        {
            return _random.Next(range);
        }

        // ~10 ms/record
        //private static int ChooseRandomIndex(int range)
        //{
        //    var bytes = new byte[4];
        //    RNG.GetNonZeroBytes(bytes);
        //    uint randomInteger = BitConverter.ToUInt32(bytes, 0);
        //    return Convert.ToInt32(randomInteger % range);
        //}

        public static T TakeRandomOrDefault<T>(this IEnumerable<T> sequence)
        {
            if (!sequence.Any())
                return default(T);

            return GetRandomItem(sequence);
        }

        public static T TakeRandomOrDefault<T>(this IEnumerable<T> sequence, Func<T, bool> predicate)
        {
            return TakeRandomOrDefault(sequence.Where(predicate));
        }

        /// <exception cref=”ArgumentException”>sequence</exception>
        public static T TakeRandom<T>(this IEnumerable<T> sequence)
        {
            if (!sequence.Any())
                throw new ArgumentException(“sequence”, “Can’t get random member of an empty sequence”);

            return GetRandomItem(sequence);
        }

        /// <exception cref=”ArgumentException”>sequence</exception>
        public static T TakeRandom<T>(this IEnumerable<T> sequence, Func<T, bool> predicate)
        {
            return TakeRandom(sequence.Where(predicate));
        }

        private static T GetRandomItem<T>(IEnumerable<T> sequence)
        {
            int chosenIndex = ChooseRandomIndex(sequence.Count());
            return chosenIndex > 0
                       ? sequence.Skip(chosenIndex).First()
                       : sequence.First();
        }
    }
}
{% endhighlight %}

From looking at the code, you can see that I tried different random number generators. I wasn't surprised that the `RandomNumberGenerator` from the `System.Security.Cryptography` namespace is expensive to construct, but I found it interesting that it gets random data appreciably faster than the Random class. My benchmarking wasn't extensive, just some elapsed times gleaned from running my unit tests.

Enjoy!
