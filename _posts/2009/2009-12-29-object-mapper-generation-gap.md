---
layout: post
comments: true
title: 'Object Mapper: Generation Gap'
date: 2009-12-29 16:36:41 -07:00
categories:
- professional
tags:
- children
- ElementInfo
- generation
- grandparent
- indexed
- inheritance
- nested
- object mapper
- parent
- person
- polymorphism
- properties

---
In yesterday's post about the [domain model]({% post_url 2009-12-28-the-object-mapper-domain-model %}), I described some of the use cases for the object mapper.

In trying to use it in a real-world situation today, my co-worker found another domain concept.

Let's say I have the following hierarchy of objects:

*   Person { Name : string }
*   Parent { Children : Person[] } is-a Person
*   Grandparent { Grandchildren : Person[] } is-a Parent

Hopefully, that notation isn't too hard to read. By that, I mean to say that a Person has a Name, a Parent is a Person with an array of type Person called Children, and a Grandparent is a Parent with Grandchildren.

Let's further say that I want to use my Object Mapper to convert a Grandparent object into a Parent object.

To probe the problem, I created a new test class and started to write tests. I determined I'd need something like the following XML:

{% highlight xml %}
<Source ID="source1" Type="Grandparent">  
<Target ID="target1" Type="Parent">  
<Element Source="**[TBD]**" Target="Name" />  
<Element Source="Grandchildren" Target="Children" />  
</Target>  
</Source>
{% endhighlight %}

The fly in the ointment is what to put in the [TBD] section. I want the name of, say, the first child.

However, even with all of the elements I introduced yesterday, I have no way of asking for elements of different "generations", at different levels of the hierarchy. I have commands that can copy objects to objects and properties to properties, but not properties to objects or objects to properties.

Back to the TBD piece. It would be nice if it could read:

{% highlight xml %}
<Element Source="Children[0].Name" Target="Name" />
{% endhighlight %}

Children[0] is a C#-ish way of saying the first item in the array of Children, and the number is called the index of the array.

Of course, the test is red (i.e., doesn't pass), because the Parent object doesn't have a property called "Children[0],Name". So far, so good.

This is really two problems in one. I decided to defer the issue of calling a property on a property (nested properties) by ignoring the Name part of the puzzle. So, I created an extra property on Parent called Firstborn, which I'll try to populate like this:

{% highlight xml %}
<Element Source="Children[0]" Target="Firstborn" />
{% endhighlight %}

Failing test in hand, I applied myself to getting the test to pass. As I'll explain more in a future post, I have an Adapter class that allows me to treat fields and properties the same called ElementInfo. It's responsible for resolving properties, so I added support to the ElementInfo object to resolve indexed properties as well.

I re-ran my test. Still red.

After some debugging and head-scratching, I realized that what I really need is not support for indexed properties, but support for a property of a type that itself supports indexing, like Children which is an array.

To wit:

{% highlight csharp %}
public Person[] _children;

// what I want to be able to extract info from

// example: mom.Children[0]

public Person[] Children

{

    get { return _children; }

    set { _children = value; }

}

// what I ended up supporting, oops!

// example: mom[0]

public object this[int index]

{

    get { return _children[index]; }

}

{% endhighlight %}

So, once more into the breach, dear friends!

I now return you to the scheduled posts in the series while I resolve this. The next post will talk some about the XML parser.
