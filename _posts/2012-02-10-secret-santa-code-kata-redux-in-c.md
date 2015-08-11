---
layout: post
comments: true
title: Secret Santa Code Kata Redux in C#
categories:
- coding
- professional
tags:
- c-sharp
- C#
- code exercise
status: publish
type: post
published: true
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
Here’s another solution to the [Secret Santa code kata](http://rubyquiz.com/quiz2.html), this time in my “native” programming language of C#. This is the second solution I’ve written this week to this problem. Code katas are about experimenting with different approaches to simple but not trivial problems.

My [first solution]({% post_url 2012-01-25-secret-santa-code-kata-in-powershell %}), written in PowerShell, relied on selecting random pairs of people and using a “hill-climbing” algorithm to avoid getting stuck. This time, I gave myself the constraint that the solution had to be deterministic — no randomness. I had been toying with the idea of using an Abelian [ring](http://en.wikipedia.org/wiki/Ring_(mathematics)). A couple of common examples are the hours on a clock or the modulus (remainder) operator in math. But I couldn’t decide how I’d handle iterating through the members of that ring without duplicates. I determined that I’d need to re-sort the list.

I wrote this solution using test-driven development (TDD), meaning I wrote my tests before implementation — I won’t show all of those tests today. As it turned out, I didn’t need to code a Ring class. I find when I do TDD, I often don’t end up writing half the code I thought I’d need!

Unlike my PowerShell solution which just used strings, I knew I wanted to create a data object to store the incoming rows of data in, which I named the Participant class:

{% highlight csharp %}  
using System;

namespace SantaKataApp {  
  public class Participant {  
    private Participant(string firstName, string lastName, string email)  
    {  
      FirstName = firstName;  
      LastName = lastName;  
      Email = email;  
    }

    public string FirstName { get; private set; }  
    public string LastName { get; private set; }  
    public string Email { get; private set; }

    public static Participant Create(string descriptor, int id)  
    {  
      var parts = descriptor.Split();  
      var email = parts[2].Replace("<", "").Replace(">", "");  
      return new Participant(parts[0], parts[1], email);  
    }

    public override string ToString()  
    {  
      return string.Format("{0} {1} <{2}>", FirstName, LastName, Email);  
    }  
  }  
}  
{% endhighlight %}

For a while, I thought I might need to implement `IEquatable<Participant>`, `Equals()`, and `GetHashCode()` in order to compare Participants, but again, TDD proved me wrong.

The plan for this approach was to:  
 1\. Parse the incoming list  
 2\. Resort the list  
 3\. Display the results

The act of resorting took the majority of the development time. I created a `ListResorter` class to do the work.

I started by writing tests….

{% highlight csharp %}
using System;  
using System.Collections;  
using System.Collections.Generic;  
using System.Linq;  
using Microsoft.VisualStudio.TestTools.UnitTesting;  
using SantaKataApp;

namespace SantaKataTests  
{  
  [TestClass]  
  public class ListResorterTests  
  {  
    [TestMethod]  
    public void SwapItemsInList_Succeeds()  
    {  
      var list = new List<int>(new[] { 3, 2, 1 });  
      var listResorter = new ListResorter<int>(list, null);  
      listResorter.Swap(0, 1);  
      CollectionAssert.AreEqual(list.ToArray(), new[] { 2, 3, 1 });  
    }

    [TestMethod, ExpectedException(typeof(InvalidOperationException))]  
    public void SwapWithInvalidIndex_Throws()  
    {  
      var list = new List<int>(new[] { 3, 2, 1 });  
      var listResorter = new ListResorter<int>(list, null);  
      listResorter.Swap(74, 1);  
    }

    [TestMethod]  
    public void CanAdjoin_WithTwoItems_DeterminesIfTheyCanAdjoin()  
    {  
      var list = new List<int>(new[] { 3, 1, 2 });  
      var listResorter = new ListResorter<int>(list, (x,y) =>x % 2 != y % 2);  
      Assert.IsTrue(listResorter.CanAdjoin(1, 2)); // list[1] = 1, list[2] = 2  
      Assert.IsFalse(listResorter.CanAdjoin(0, 1));  
    }

  // ... and so on ...  
  }  
}  
{% endhighlight %}

These are the first two tests I wrote. I decided the simplest operation I needed to resort a list was the ability to swap two items in that list. Once I had that working, I picked the next piece, the ability to decide if two things can adjoin (“to be close to or in contact with”), and I proceeded from there.

Notice that the `LineResorter<T>` constructor takes a list to operate against, and a function that compares two instances of type T and determines if they can be adjoining in the list. In the case of my unit tests, I used `(x,y) => x % 2 != y % 2`, which is a fancy way of saying that two odds or two evens can’t be next to each other in the list. I wanted to use a different type (int) than I’d be using in my real use case to make sure I didn’t make any assumptions about the nature of type T. This comparison was the first one for two numbers that came to mind.

Each time I needed functionality out of the `ListResorter`, I wrote a test. I watched it fail, then I made all the tests pass. If I saw opportunities to refactor, I took them whenever all my tests were green (passing). By the time I was done, I had about a dozen tests and this class:

{% highlight csharp %}  
using System;  
using System.Collections.Generic;  
using System.Linq;

namespace SantaKataApp  
{  
  public class ListResorter<T>  
  {  
    private readonly List<T> _list;  
    private readonly Func<T, T, bool> _canAdjoin;

    public ListResorter(List<T> list, Func<T, T, bool> canAdjoin)  
    {  
      _list = list;  
      _canAdjoin = canAdjoin;  
    }

    internal void Swap(int index1, int index2)  
    {  
      ThrowIfIndexesAreInvalid(index1, index2);  
      T temp = _list[index2];  
      _list[index2] = _list[index1];  
      _list[index1] = temp;  
    }

    private void ThrowIfIndexesAreInvalid(int index1, int index2)  
    {  
      if (_list.Count < index1 - 1 || _list.Count < index2 - 1)  
      throw new InvalidOperationException("An index is beyond the length of the array");  
    }

    internal bool CanAdjoin(int index1, int index2)  
    {  
      ThrowIfIndexesAreInvalid(index1, index2);  
      return _canAdjoin(_list[index1], _list[index2]);  
    }

    public int GetNextIndex(int i)  
    {  
      if (i >= _list.Count)  
        throw new InvalidOperationException("Invalid index");  
      if (i == _list.Count - 1)  
        return 0;  
      return i + 1;  
    }

    internal bool CanAllAdjoin()  
    {  
      return !_list.Where((t, i) =>!CanAdjoin(i, GetNextIndex(i))).Any();  
    }

    public List<T>Resort()  
    {  
      var list = _list;

      while (! CanAllAdjoin())  
      {  
        for (int i=0; i < list.Count; i++)  
        {  
          int j = GetNextIndex(i);  
          int k = GetNextIndex(j);  
          if (! CanAdjoin(i, j) &amp;&amp; CanAdjoin(i, k))  
          Swap(j, k);  
        }  
      }  
      return list;  
    }  
  }  
}  
{% endhighlight %}

This class has two public methods, `GetNextIndex()` and `Resort()`. That Abelian ring idea still lives in the `GetNextIndex()` method, which says that the next member after the last in the list is the first, making the list circular. `Resort()` does what you would expect.

The other methods in the class are marked internal, so that my TDD tests can access them via the `[Assembly:InternalsVisibleTo()]` attribute in the `Assembly.cs` code file. After design is done, I would consider rewriting the test methods that talk to internal methods so that they are exercised through the public method. I don’t want my unit tests to be break should someone decide to change the internal implementation of these methods. You can see a bit of this thinking in the `ThrowIfIndexesAreInvalid()` method. I pulled this method out to avoid duplication of code during refactoring, where I already had unit tests in place and thus I didn’t need to write new ones.

Once I had `ListResorter` working, writing a console wrapper was easy:

{% highlight csharp %}  
using System;  
using System.Collections.Generic;  
using System.IO;  
using System.Linq;

namespace SantaKataApp  
{  
  class Program  
  {  
    static void Main(string[] args)  
    {  
      string[] fileContents = File.ReadAllLines(args[0]);  
      Func<Participant, Participant, bool>surnamesDontMatch = (x, y) =>x.LastName != y.LastName;  
      List<Participant>names = fileContents.Select(Participant.Create).ToList();

      var listResorter = new ListResorter<Participant>(names, surnamesDontMatch);  
      List<Participant>sorted = listResorter.Resort();

      DisplayParticipants(listResorter, sorted);  
    }

    internal static void DisplayParticipants(ListResorter<Participant>listResorter, IList<Participant>sorted)  
    {  
      for(int i=0; i < sorted.Count; i++)  
      Console.WriteLine(Display(sorted[i], sorted[listResorter.GetNextIndex(i)]));  
    }

    internal static string Display(Participant name, Participant giveToName)  
    {  
      var giveTo = giveToName != null ? giveToName.ToString() : "NONE";  
      return string.Format("{0} gives a gift to {1}", name, giveTo);  
    }  
  }  
}  
{% endhighlight %}

Most of the work done in the console app is formatting the output for display. The heavy lifting is done by the `ListResorter` class.

This program outputs data like:

<pre>
PS C:temp> .SantaKataApp.exe .names_santa.txt
Luke Skywalker &lt;luke@theforce.net&gt; gives a gift to Toula Portokalos &lt;toula@manhunter.org&gt;
Toula Portokalos &lt;toula@manhunter.org&gt; gives a gift to Leia Skywalker &lt;leia@therebellion.org&gt;
Leia Skywalker &lt;leia@therebellion.org&gt; gives a gift to Gus Portokalos &lt;gus@weareallfruit.net&gt;
...
</pre>

I met my goal: the output is the same every time given the same input file.

I time-boxed the effort at two hours and I came close to reaching my limit. I initially began by writing an iterator, but abandoned it when I realized that I only wanted to traverse the collection once.

There is more that could be done to this program, of course. For example, I’m not happy about `DisplayParticipants` using `GetNextIndex()`. The only reason that `DisplayParticipants()` needs a `ListResorter` is to use its ring-like `GetNextIndex()` method. This functionality should have been extracted into its own class.

Comments? Questions?
