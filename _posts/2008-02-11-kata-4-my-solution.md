---
layout: post
title: 'Code Kata 4: My Solution'
date: 2008-02-11 07:13:57.000000000 -07:00
categories:
- professional
tags:
- code exercise
- dry
- munging
- programming
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
excerpt: !ruby/object:Hpricot::Doc
  options: {}
---
[Kata 4](http://web.archive.org/web/20131016084024/http://codekata.pragprog.com/2007/01/kata_four_data_.html) is about data munging. We're asked to download a couple of text files and extract some data. The first is weather data ([Listing 1](#listing1)). The second is soccer data ([Listing 2](#listing2)). [Listing 3](#listing3) is the DRY unified version. I combined the programs, but they could just as easily have been two programs.

Then, we were asked to answer some questions. I'm going to answer them out of order. The writing of the first program certainly did alter my approach to the second. In fact, as you can see, the second program is almost identical to the first, because I retooled the first program to create the second program.

I can't say whether factoring out code is **always** a good thing, but I think it certainly was in the case. Premature factoring is a waste of effort, but once the commonality emerges, I think factoring is often the right thing to do. I don't think the readability or maintainability of this particular program suffered too much, but I agree it can quickly become a concern in larger programs.

See also my previous Kata posts: [Kata 1](http://neontapir.wordpress.com/2008/01/26/code-kata-1-my-solution/), [Kata 2](http://neontapir.wordpress.com/2008/01/31/kata-2-my-solution/) and [Kata 3](http://neontapir.wordpress.com/2008/02/04/kata-3-my-solution/).

<a name="listing1"></a>**Listing 1**: Weather data

<pre><span class="kwrd">using</span> System;
<span class="kwrd">using</span> System.IO;
<span class="kwrd">using</span> System.Text.RegularExpressions;

<span class="kwrd">namespace</span> Kata_4
{
    <span class="kwrd">public</span> <span class="kwrd">class</span> Kata4Part1
    {
        <span class="kwrd">static</span> <span class="kwrd">void</span> Main()
        {
            PrintSmallestDaySpread();
            Console.ReadLine();
        }

        <span class="kwrd">static</span> <span class="kwrd">void</span> PrintSmallestDaySpread() {
            <span class="kwrd">string</span> dayWithSmallestSpread = <span class="str">"(none)"</span>;
            <span class="kwrd">int</span> smallestSpread = <span class="kwrd">int</span>.MaxValue;
            <span class="kwrd">using</span> (FileStream f = File.Open(<span class="str">@"....weather.dat"</span>, FileMode.Open)) {
                <span class="kwrd">using</span> (StreamReader sr = <span class="kwrd">new</span> StreamReader(f)) {
                    <span class="kwrd">while</span> (! sr.EndOfStream) {
                        <span class="kwrd">string</span> s = sr.ReadLine();
                        Match m = Regex.Match(s, <span class="str">@"^s+(d+)s+(d+)s+(d+)"</span>);
                        <span class="kwrd">if</span> (m.Groups.Count > 1) {
                            <span class="kwrd">string</span> day = m.Groups[1].ToString();
                            <span class="kwrd">int</span> maxTemp = Convert.ToInt32(m.Groups[2].ToString());
                            <span class="kwrd">int</span> minTemp = Convert.ToInt32(m.Groups[3].ToString());
                            <span class="kwrd">int</span> spread = Math.Abs(maxTemp - minTemp);
                            <span class="kwrd">if</span> (spread < smallestSpread) {
                                smallestSpread = spread;
                                dayWithSmallestSpread = day;
                            }
                        }
                    }
                }
            }
            Console.WriteLine(<span class="str">"The day with the smallest spread is day {0}"</span>, dayWithSmallestSpread);
        }
    }
}</pre>

<a name="#listing2"></a>**Listing 2**: Soccer data

<pre><span class="kwrd">using</span> System;
<span class="kwrd">using</span> System.IO;
<span class="kwrd">using</span> System.Text.RegularExpressions;

<span class="kwrd">namespace</span> Kata_4
{
    <span class="kwrd">public</span> <span class="kwrd">class</span> Kata4Part2
    {
        <span class="kwrd">static</span> <span class="kwrd">void</span> Main()
        {
            PrintSmallestGoalSpread();
            Console.ReadLine();
        }

        <span class="kwrd">static</span> <span class="kwrd">void</span> PrintSmallestGoalSpread() {
            <span class="kwrd">string</span> teamWithSmallestSpread = <span class="str">"(none)"</span>;
            <span class="kwrd">int</span> smallestSpread = <span class="kwrd">int</span>.MaxValue;
            <span class="kwrd">using</span> (FileStream f = File.Open(<span class="str">@"....football.dat"</span>, FileMode.Open)) {
                <span class="kwrd">using</span> (StreamReader sr = <span class="kwrd">new</span> StreamReader(f)) {
                    <span class="kwrd">while</span> (! sr.EndOfStream) {
                        <span class="kwrd">string</span> s = sr.ReadLine();
                        Match m = Regex.Match(s, <span class="str">@"^s+d+.s+(w+)s+d+s+d+s+d+s+d+s+(d+)s+-s+(d+)"</span>);
                        <span class="kwrd">if</span> (m.Groups.Count > 1) {
                            <span class="kwrd">string</span> team = m.Groups[1].ToString();
                            <span class="kwrd">int</span> goalsFor = Convert.ToInt32(m.Groups[2].ToString());
                            <span class="kwrd">int</span> goalsAgainst = Convert.ToInt32(m.Groups[3].ToString());
                            <span class="kwrd">int</span> spread = Math.Abs(goalsFor - goalsAgainst);
                            <span class="kwrd">if</span> (spread < smallestSpread) {
                                smallestSpread = spread;
                                teamWithSmallestSpread = team;
                            }
                        }
                    }
                }
            }
            Console.WriteLine(<span class="str">"The team with the smallest goal spread is {0}"</span>, teamWithSmallestSpread);
        }
    }
}
</pre>

<a name="#listing3"></a>**Listing 3**: Unified version

<pre><span class="kwrd">using</span> System;
<span class="kwrd">using</span> System.IO;
<span class="kwrd">using</span> System.Text.RegularExpressions;

<span class="kwrd">namespace</span> Kata_4
{
    <span class="kwrd">public</span> <span class="kwrd">class</span> Kata4Munger {
        <span class="kwrd">public</span> <span class="kwrd">static</span> <span class="kwrd">string</span> ExtractSmallestDifference(<span class="kwrd">string</span> fileName, <span class="kwrd">string</span> regex) {
            <span class="kwrd">string</span> itemWithSmallestSpread = <span class="str">"(none)"</span>;
            <span class="kwrd">int</span> smallestSpread = <span class="kwrd">int</span>.MaxValue;
            <span class="kwrd">using</span> (FileStream f = File.Open(fileName, FileMode.Open)) {
                <span class="kwrd">using</span> (StreamReader sr = <span class="kwrd">new</span> StreamReader(f)) {
                    <span class="kwrd">while</span> (! sr.EndOfStream) {
                        <span class="kwrd">string</span> s = sr.ReadLine();
                        Match m = Regex.Match(s, regex);
                        <span class="kwrd">if</span> (m.Groups.Count > 1) {
                            <span class="kwrd">string</span> day = m.Groups[1].ToString();
                            <span class="kwrd">int</span> maxTemp = Convert.ToInt32(m.Groups[2].ToString());
                            <span class="kwrd">int</span> minTemp = Convert.ToInt32(m.Groups[3].ToString());
                            <span class="kwrd">int</span> spread = Math.Abs(maxTemp - minTemp);
                            <span class="kwrd">if</span> (spread < smallestSpread) {
                                smallestSpread = spread;
                                itemWithSmallestSpread = day;
                            }
                        }
                    }
                }
            }
            <span class="kwrd">return</span> itemWithSmallestSpread;
        }
    }

    <span class="kwrd">public</span> <span class="kwrd">class</span> Kata4Part3
    {
        <span class="kwrd">static</span> <span class="kwrd">void</span> Main()
        {
            <span class="kwrd">string</span> itemWithSmallestSpread = Kata4Munger.ExtractSmallestDifference(<span class="str">@"....weather.dat"</span>, <span class="str">@"^s+(d+)s+(d+)s+(d+)"</span>);
            Console.WriteLine(<span class="str">"The day with the smallest spread is day {0}"</span>, itemWithSmallestSpread);

            itemWithSmallestSpread = Kata4Munger.ExtractSmallestDifference(<span class="str">@"....football.dat"</span>, <span class="str">@"^s+d+.s+(w+)s+d+s+d+s+d+s+d+s+(d+)s+-s+(d+)"</span>);
            Console.WriteLine(<span class="str">"The team with the smallest goal spread is {0}"</span>, itemWithSmallestSpread);
            Console.ReadLine();
        }
    }
}</pre>

.csharpcode, .csharpcode pre
 {
 font-size: small;
 color: black;
 font-family: consolas, "Courier New", courier, monospace;
 background-color: #ffffff;
 /*white-space: pre;*/
 }
 .csharpcode pre { margin: 0em; }
 .csharpcode .rem { color: #008000; }
 .csharpcode .kwrd { color: #0000ff; }
 .csharpcode .str { color: #006080; }
 .csharpcode .op { color: #0000c0; }
 .csharpcode .preproc { color: #cc6633; }
 .csharpcode .asp { background-color: #ffff00; }
 .csharpcode .html { color: #800000; }
 .csharpcode .attr { color: #ff0000; }
 .csharpcode .alt
 {
 background-color: #f4f4f4;
 width: 100%;
 margin: 0em;
 }
 .csharpcode .lnum { color: #606060; }
