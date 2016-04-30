---
layout: post
comments: true
title: 'Object Mapper: Challenges of inferring type information'
date: 2010-01-04 17:05:23 -07:00
categories:
- professional
tags:
- activator
- csharp
- design patterns
- dynamic
- Factory
- FieldInfo
- infer
- ironruby
- MethodInfo
- object mapper
- PropertyInfo
- Reflection
- type
---
I left off last time talking about [array transformation Commands](http://neontapir.com/wp/2009/12/object-mapper-xml-parsing/), and mentioned they highlighted the troubles with inferring type information.

Remember that the parser can take a signature of

{% highlight csharp %}  
object Convert(object source)  
{% endhighlight %}

The reason all of the Convert methods do not take generics is for Java interoperability. Because the method can take any object, I need to lean heavily on the Reflection library to infer type information. (This is a situation where the new dynamic typing in C# 4.0 would have been invaluable!)

For example, let's take the ElementSetter command. In IronRuby or C# 4.0, this would be a piece of cake. In Ruby, I could simply say something like:

{% highlight csharp %}   
property_name = "Name"  
# ... stuff ...  
target.send(property_name, source.send(property_name))  
{% endhighlight %}  

Instead, I have to use type metadata to do the work:

{% highlight csharp %}
public override object Execute(object sourceObject, object targetObject)
{
  ElementInfo sourceProperty = new ElementInfo(sourceObject.GetType(), _source.ID);
  object sourceValue = sourceProperty.GetValue(sourceObject);
  ElementInfo targetProperty = new ElementInfo(targetObject.GetType(), _target.ID);
  targetProperty.SetValue(targetObject, sourceValue);
  return targetObject;
}
{% endhighlight %}

The `ElementInfo` class serves as an [Adapter](http://en.wikipedia.org/wiki/Adapter_pattern) for the Reflection library's PropertyInfo and FieldInfo classes, so that I can treat properties and fields the same throughout the rest of my code. The ID property of the `_source` and `_target`</tt>` variables contain the name of the property. Under the covers, the `ElementInfo` class just defers to the appropriate instance of either a `PropertyInfo` or `FieldInfo` class.

The logic behind finding the right `MethodInfo` object to represent a conversion function is a little more challenging. I wrote a `MethodResolver` class to handle the lookup of a method by its name. It can find both instance and static methods.

Another responsibility of the `MethodResolver` class is handling generic types. Using the `Type.GetMethod()` method, I can get a `MethodInfo` object. MethodInfo contains a method `ContainsGenericParameters()`. While that is true, there are open generic parameters to the method that need to be bound.

The last challenge to mention in this post is the creation of objects. How can one create a new instance of an arbitrary type. Generics provide some useful constructs like `default(T)`, but there is no convenient way to invoke this language feature outside of a generic method. And, as it turns out, `default(T)` doesn't always give me the answer I want.

I stumbled upon this in writing the array Command Decorator. I have an array of strings. I want to fill an array of integers by converting each member of the string array to an integer. But where do I get the new array from?

I tried a few casting solutions, but found that if I used an object[], for example, the objects inside the array would appear to lose their type information and be just objects, which caused problems later in the process.

I also tried to write something like:

{% highlight csharp %}
T[] destination = new T[](_source);  
{% endhighlight %}

I have an issue, though. This generic method must now have the constraint new(), which means I have to handle arrays as a special case.

I found that by creating an `ObjectFactory` class, it simplified other areas of the code. The `ObjectFactory`, being a [Factory](http://en.wikipedia.org/wiki/Factory_object), knows how to create new objects. It also holds a cache of previously created objects.

{% highlight csharp %}
public object Create(Type targetType)
{
	if (targetType.IsAssignableFrom(typeof(string)))
		return string.Empty;

	if (targetType.IsAssignableFrom(typeof(DateTime)))
		return DateTime.MinValue;

	if (targetType.IsArray)
		return Array.CreateInstance(targetType.GetElementType(), 0);

	try
	{
		return Activator.CreateInstance(targetType);
	}
	catch (MissingMethodException e)
	{
		throw new Exception(string.Format("No parameterless constructor for type {0}", targetType), e);
  }
}
{% endhighlight %}

`Activator` lives in the `System` namespace, and it's what the .NET Framework uses for instantiating objects in `AppDomains`. It works for my purposes, but as you can see, I did end up with some special handling of arrays in the end.

Having talked about some of the challenges of type inference, next post will discuss the conversion engine itself.
