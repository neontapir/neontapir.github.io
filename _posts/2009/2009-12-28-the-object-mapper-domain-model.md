---
layout: post
comments: true
title: The Object Mapper Domain Model
date: 2009-12-28 09:36:08 -07:00
categories:
- professional
tags:
- association
- conversion
- correspondence
- domain model
- function
- object mapper
- programming
- properties
- XML

---
Last time, I [introduced the object mapper]({% post_url 2009-12-23-introducing-the-object-mapper %}). Here, I describe its domain model.

The request and response objects that require mapping are plain-old CLR objects with properties for the most part, though there are some arrays to contend with. The challenge is that the request and response objects do not have the same structure.

Many of the properties have a one-to-one correspondence. For example, a Name field on one request object may align with a Name property on the DataStore request. In some cases, though, the property names are different.

Other properties share a one-to-many association, so the contents of the source object must be copied to several target properties. And yet other pesky properties share a many-to-one association. For example, a Java application's request might have address, city, state, and ZIP code as separate fields, but they must be combined into a single property of the DataStore request.

Here's an example of a simple mapping document for a Foo object with Name and Age properties:

{% highlight xml %}
<?xml version="1.0" encoding="utf-8"?>  
<Maps>  
<Source ID="source1" Type="Foo">  
<Target ID="target1" Type="Foo">  
<Element ID="Name" Source="Name" Target="Name" />  
<Element ID="Age" Source="Age" Target="Age" />  
</Target>  
</Source>  
</Maps>
{% endhighlight %}

There is a Source, which describes a source object. That Source object can be converted into a Target object. Objects have Elements, which describe either properties or fields. Each element has its own source and target attributes to describe what property of the source corresponds to what property of the target.

So far, so good. Let's say, though, that the source request object doesn't define an Age property, but it's required on the target request. For cases like this, I need the capability to inject a value:

{% highlight xml %}
<Source ID="source1" Type="Foo">  
<Target ID="source1" Type="Foo">  
<Element ID="Name" Source="Name" Target="Name" />  
<Inject Target="Age">37</Inject>  
</Target>  
</Source>
{% endhighlight %}

The Inject node allows me to specify the value I'd like to inject, in this case any target object would have an Age of 37.

This poses a challenge, because that "37" is a string by virtue of being XML. .NET doesn't offer a way to implicitly make that "37" into the number 37\. So, I need a way to convert primitive objects, objects with no properties:

{% highlight xml %}
<Object Source="System.String" Target="System.Int32">  
<Function Type="System.Int32" Method="Parse" />  
</Object>
{% endhighlight %}

The Function node defines a method to invoke when converting the object. It's a valid child of the Element node as well, so a property can be converted by a function as well.

Functions can refer to instance methods, which are called against an instance of a type. They can also refer to static methods, which belong to the type itself. One can even specify arguments, for cases like Substring where I might only want the first few letters of a string:

{% highlight xml %}
<Element ID="Name" Source="Name" Target="Name">  
<Function Type="System.String" Method="Substring">  
<Argument Type="System.Int32">0</Argument>  
<Argument Type="System.Int32">3</Argument>  
</Function>  
</Element>
{% endhighlight %}

Sometimes, I may want to convert an array of one type to an array of another by converting each of its members individually by use of the ApplyToEachElement flag:

{% highlight xml %}
<Object Source="System.String[]" Target="System.Int32[]" ApplyToEachElement="true">  
<Function Type="System.Int32" Method="Parse" />  
</Object>
{% endhighlight %}

Here, the conversion engine will take an array of strings and convert it to an array of integers by calling int.Parse with each string as an argument.

That introduces most of the domain concepts of the object mapper. Next post will delve into the components that comprise the object mapper itself.
