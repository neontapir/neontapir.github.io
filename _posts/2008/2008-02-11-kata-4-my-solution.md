---
layout: post
comments: true
title: 'Code Kata 4: My Solution'
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
[Kata 4](http://web.archive.org/web/20131016084024/http://codekata.pragprog.com/2007/01/kata_four_data_.html) is about data munging. We're asked to download a couple of text files and extract some data. The first is weather data ([Listing 1](#listing1)). The second is soccer data ([Listing 2](#listing2)). [Listing 3](#listing3) is the DRY unified version. I combined the programs, but they could just as easily have been two programs. Then, we were asked to answer some questions. I'm going to answer them out of order. The writing of the first program certainly did alter my approach to the second. In fact, as you can see, the second program is almost identical to the first, because I retooled the first program to create the second program. I can't say whether factoring out code is **always** a good thing, but I think it certainly was in the case. Premature factoring is a waste of effort, but once the commonality emerges, I think factoring is often the right thing to do. I don't think the readability or maintainability of this particular program suffered too much, but I agree it can quickly become a concern in larger programs. See also my previous Kata posts: [Kata 1](http://neontapir.wordpress.com/2008/01/26/code-kata-1-my-solution/), [Kata 2](http://neontapir.wordpress.com/2008/01/31/kata-2-my-solution/) and [Kata 3](http://neontapir.wordpress.com/2008/02/04/kata-3-my-solution/).

<a name="listing1"></a>**Listing 1**: Weather data

{% highlight csharp %}
using System;
using System.IO;
using System.Text.RegularExpressions;

namespace Kata_4
{
    public class Kata4Part1
    {
        static void Main()
        {
            PrintSmallestDaySpread();
            Console.ReadLine();
        }

        static void PrintSmallestDaySpread() {
            string dayWithSmallestSpread = "(none)";
            int smallestSpread = int.MaxValue;
            using (FileStream f = File.Open(@"....weather.dat", FileMode.Open)) {
                using (StreamReader sr = new StreamReader(f)) {
                    while (! sr.EndOfStream) {
                        string s = sr.ReadLine();
                        Match m = Regex.Match(s, @"^s+(d+)s+(d+)s+(d+)");
                        if (m.Groups.Count > 1) {
                            string day = m.Groups[1].ToString();
                            int maxTemp = Convert.ToInt32(m.Groups[2].ToString());
                            int minTemp = Convert.ToInt32(m.Groups[3].ToString());
                            int spread = Math.Abs(maxTemp - minTemp);
                            if (spread < smallestSpread) {
                                smallestSpread = spread;
                                dayWithSmallestSpread = day;
                            }
                        }
                    }
                }
            }
            Console.WriteLine("The day with the smallest spread is day {0}", dayWithSmallestSpread);
        }
    }
}
{% endhighlight %}

<a name="#listing2"></a>**Listing 2**: Soccer data

{% highlight csharp %}
using System;
using System.IO;
using System.Text.RegularExpressions;

namespace Kata_4
{
    public class Kata4Part2
    {
        static void Main()
        {
            PrintSmallestGoalSpread();
            Console.ReadLine();
        }

        static void PrintSmallestGoalSpread() {
            string teamWithSmallestSpread = "(none)";
            int smallestSpread = int.MaxValue;
            using (FileStream f = File.Open(@"....football.dat", FileMode.Open)) {
                using (StreamReader sr = new StreamReader(f)) {
                    while (! sr.EndOfStream) {
                        string s = sr.ReadLine();
                        Match m = Regex.Match(s, @"^s+d+.s+(w+)s+d+s+d+s+d+s+d+s+(d+)s+-s+(d+)");
                        if (m.Groups.Count > 1) {
                            string team = m.Groups[1].ToString();
                            int goalsFor = Convert.ToInt32(m.Groups[2].ToString());
                            int goalsAgainst = Convert.ToInt32(m.Groups[3].ToString());
                            int spread = Math.Abs(goalsFor - goalsAgainst);
                            if (spread < smallestSpread) {
                                smallestSpread = spread;
                                teamWithSmallestSpread = team;
                            }
                        }
                    }
                }
            }
            Console.WriteLine("The team with the smallest goal spread is {0}", teamWithSmallestSpread);
        }
    }
}
{% endhighlight %}

<a name="#listing3"></a>**Listing 3**: Unified version

{% highlight csharp %}
using System;
using System.IO;
using System.Text.RegularExpressions;

namespace Kata_4
{
    public class Kata4Munger {
        public static string ExtractSmallestDifference(string fileName, string regex) {
            string itemWithSmallestSpread = "(none)";
            int smallestSpread = int.MaxValue;
            using (FileStream f = File.Open(fileName, FileMode.Open)) {
                using (StreamReader sr = new StreamReader(f)) {
                    while (! sr.EndOfStream) {
                        string s = sr.ReadLine();
                        Match m = Regex.Match(s, regex);
                        if (m.Groups.Count > 1) {
                            string day = m.Groups[1].ToString();
                            int maxTemp = Convert.ToInt32(m.Groups[2].ToString());
                            int minTemp = Convert.ToInt32(m.Groups[3].ToString());
                            int spread = Math.Abs(maxTemp - minTemp);
                            if (spread < smallestSpread) {
                                smallestSpread = spread;
                                itemWithSmallestSpread = day;
                            }
                        }
                    }
                }
            }
            return itemWithSmallestSpread;
        }
    }

    public class Kata4Part3
    {
        static void Main()
        {
            string itemWithSmallestSpread = Kata4Munger.ExtractSmallestDifference(@"....weather.dat", @"^s+(d+)s+(d+)s+(d+)");
            Console.WriteLine("The day with the smallest spread is day {0}", itemWithSmallestSpread);

            itemWithSmallestSpread = Kata4Munger.ExtractSmallestDifference(@"....football.dat", @"^s+d+.s+(w+)s+d+s+d+s+d+s+d+s+(d+)s+-s+(d+)");
            Console.WriteLine("The team with the smallest goal spread is {0}", itemWithSmallestSpread);
            Console.ReadLine();
        }
    }
}
{% endhighlight %}
