---
layout: post
comments: true
title: 'Code Kata 2: My Solution'
categories:
- professional
tags:
- algorithm
- code exercise
- picard iteration
- programming
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
[Code Kata 2](http://web.archive.org/web/20131016085418/http://codekata.pragprog.com/2007/01/kata_two_karate.html "Code Kata 2") was harder than Kata 1\. Dave is right, it's hard to come up with five different ways to do something! However, I think I have five sufficiently different approaches to warrant a post. My code, in C#, is below the More tag.

Approach 1 is a simple for loop, starting at the bottom and working its way up. Approach 2 uses a different looping mechanism for variety, but it does its comparisons from both ends of the array, which is faster than Approach 1 for values towards the larger end of the array.

Approach 3 leverages the fact that in C#, the List object has a built-in IndexOf function, and frankly is the way I would normally implement it.

Approach 4 creates a Dictionary with index/value pairs (in other words, a hash table), then determines the result. Lookups after the hash is built should be very quick. However, for a large array, there's a lot of overhead in creating the hash, and the hash would need to be maintained or recomputed if the array changes.

Approach 5 uses a bifurcation algorithm, basically implementing the [Picard Iteration](http://en.wikipedia.org/wiki/Picard_iteration "Picard iteration") approach of successive approximations. By far, it was the hardest to write. It splits the array in half, checks which half the target value would be in, and repeats until it finds the target value or proves the target's not in the array. For a small array like this, it's overkill. For sparse lookups against a large array, it might even prove to be the fastest.

Approaches 2 and 5 were the last ones I came up with. I had to start questioning my assumptions, which is when I hit upon Approach 2\. Approach 5 came to me in the shower while I was trying to apply my Math degree to the problem.

I can't wait for Kata 3!

(I'm going to apologize for the code formatting in advance. I need to do some research about the hosting on Wordpress and what formatting is and isn't allowed!)

{% highlight csharp %}
using System;
using System.Collections.Generic;

namespace Kata2
{
    class Program
    {
        delegate int Chopper(int number, int[] array);

        static void Main(string[] args)
        {
            int[] array = new int[] { 1, 2, 3, 5, 8, 13 };
            TestChopper(Chop1, array);
            TestChopper(Chop2, array);
            TestChopper(Chop3, array);
            TestChopper(Chop4, array);
            TestChopper(Chop5, array);

            Console.WriteLine("Test complete");
            Console.ReadLine();
        }

        static void TestChopper(Chopper c, int[] array)
        {
            int highBound = array[array.Length - 1] + 1;
            Console.WriteLine(c.Method.Name);
            for (int i = 0; i < highBound; i++)
            {
                Console.WriteLine(string.Format("{0} has index {1}", i, c(i, array)));
            }
            Console.WriteLine("n");
        }

        ///
        /// Simplest approach: for loop
        ///
        ///
        ///
        ///
        static int Chop1(int number, int[] array)
        {
            for (int i = 0; i  number)
                {
                    break;
                }
            }
            return -1;
        }

        ///
        /// Bi-directional lookup with slightly different looping
        /// mechanism.
        ///
        ///
        ///
        ///
        static int Chop2(int number, int[] array)
        {
            int arraySize = array.Length;
            if (arraySize > 0)
            {
                int i = 0;
                do
                {
                    if (array[i] == number)
                    {
                        return i;
                    }
                    if (array[arraySize - i - 1] == number)
                    {
                        return arraySize - i - 1;
                    }
                    i++;
                } while (array[i-1] < number && i < (arraySize / 2));
            }
            return -1;
        }

        ///
        /// Convert array to List, then use built-in IndexOf method
        ///
        ///
        ///
        ///
        static int Chop3(int number, int[] array)
        {
            List list = new List(array);
            return list.IndexOf(number);
        }

        static Dictionary chop4Hash;
        ///
        /// Pre-populate a Dictionary, then do the lookup
        ///
        ///
        ///
        ///
        static int Chop4(int number, int[] array)
        {
            if (chop4Hash == null)
            {
                chop4Hash = new Dictionary();
                for (int i = 0; i < array.Length; i++)
                {
                    if (!chop4Hash.ContainsKey(array[i]))
                    {
                        chop4Hash.Add(array[i], i);
                    }
                }
            }

            if (chop4Hash.ContainsKey(number))
            {
                return chop4Hash[number];
            }
            else
            {
                return -1;
            }
        }

        ///
        /// Bifurcation algorithm
        ///
        ///
        ///
        ///
        static int Chop5(int number, int[] array)
        {
            int leftIndex = 0;
            int rightIndex = array.Length - 1;
            int currIndex = 0;
            int nextIndex = int.MinValue;
            do
            {
                nextIndex = (int)((leftIndex + rightIndex) / 2);
                if (nextIndex != currIndex)
                {
                    currIndex = nextIndex;
                }
                else
                {
                    currIndex = Math.Min(nextIndex + 1, array.Length - 1);
                }

                if (array[currIndex] == number)
                {
                    return currIndex;
                }
                else if (array[currIndex] < number)
                {
                    // number's to our right
                    if (leftIndex != currIndex)
                    {
                        leftIndex = currIndex;
                    }
                    else
                    {
                        break;
                    }
                }
                else
                {
                    // number's to our left
                    if (rightIndex != currIndex)
                    {
                        rightIndex = currIndex;
                    }
                    else
                    {
                        break;
                    }
                }
            } while (
                array[leftIndex] <= number
                  && number <= array[rightIndex]);

            return -1;
        }
    }
}
{% endhighlight %}
