---
layout: post
comments: true
title: 'Object Mapper: Conversion Engine and Conditional Commands'
date: 2010-01-06 17:50:11 -07:00
categories:
- professional
tags:
- Boodhoo
- csharp
- code
- conditional
- conversion
- delegate
- design patterns
- engine
- Factory
- lambda
- Nothin' But .NET
- object mapper
- Predicate

---
Last time, I talked about [the mapping document parser](http://neontapir.wordpress.com/2009/12/30/object-mapper-xml-parsing/) component of my object mapper.

The other component, the Conversion Engine, is the workhorse of the Object Mapper. Its ObjectConversionEngine class is the public interface to conversion functionality, and it exposes methods with the following signatures:

{% highlight csharp %}  
object Convert(object source)  
T Convert(object source)  
object Convert(object source, object target)  
{% endhighlight %}

The first two signatures are used when constructing a new instance of the target object. The generic overload makes use of the extra type information to attempt to use .NET type converters when all else fails. The final signature is used when updating an existing target object.

When asked to convert an object, the engine will first try to locate a mapping that matches the source and target object types. If it finds a mapping, it invokes the mapping's Command against the source object. Being a Composite, the invocation will cascade down to each individual leaf element.

I wanted to mention two things about this process. Because we may need to create an object in a multi-step process, a Source can have multiple Targets. After each Target's command is executed, the result is cached in the ObjectFactory so it can be injected by a later command.

However, it's easy to imagine a situation where I may want to do something conditionally. For example, if I have an array of addresses on my source type, my destination type may have a PrimaryAddress property and a SecondaryAddresses array. In this case, I want the first address of the source to map to the PrimaryAddress property and the rest to go into the array.

For this, I need a new type of command, a ConditionalCommand. The XML looks like this:

{% highlight xml %}  
<Object Source=""System.String"" Target=""System.String"">  
<If Operation=""Equals"" Operand=""SomeValue"">true</If>  
<Else>false</Else>  
</Object>
{% endhighlight %}  

I thought about how to implement this for a while. When I specified this feature, I'd envisioned using expression trees. When I found out I was restricted to C# 2.0, I even spiked a version using an IL generator to create methods programatically using `Reflection.Emit`!

IL generation is not for the faint of heart, and I told myself there's got to be a better way! What I wanted originally was a lambda, which thanks to J.P. Boodhoo's [Nothin' But .NET](http://blog.developwithpassion.com) course I knew was just syntactic sugar for delegates.

I defined a Condition delegate type:

{% highlight csharp %}   
bool Condition(object source, out object result, params object[] arguments)  
{% endhighlight %}

And then I created a `ConditionalCommandBuilder` to create them. It's really a Factory class, but I preferred the name "builder" here. It uses a fluent interface, so the If methods return a `ConditionalCommandBuilder` for chaining.

{% highlight csharp %}
public ConditionalCommandBuilder IfObject(string operation, object operand, ICommand command)

{

    Predicate predicate = GetPredicate(operation, operand);

    Condition condition = delegate(object source, out object result, object[] arguments)

                            {

                                if (predicate(source))

                                {

                                    result = command.Execute(source, arguments);

                                    return true;

                                }

                                result = null;

                                return false;

                            };

    _conditions.Add(condition);

    return this;

}

{% endhighlight %}

The `GetPredicate()` command returns a `Predicate`, which is a delegate defined in the .NET Framework. The operation variable defines what type of predicate to retrieve, such as `Equals`, `Exists`, or `GreaterThan`. The operand value given to the delegate is captured for later use.

Perhaps the most interesting `GetPredicate()` method is the one that retrieves `CompareTo()` results:

{% highlight csharp %}
private Predicate GetCompareToPredicate(object operand, ICollection compareToValues)

{

    Predicate predicate = delegate(object source)

                    {                                       

                        Type type = source.GetType();

                        MethodInfo compareTo = type.GetMethod("CompareTo", new Type[] { typeof(object) });

                        if (null != compareTo)

                        {

                            object converted = TypeResolver.ConvertTo(type, operand);

                            return compareToValues.Contains((int)compareTo.Invoke(source, new object[] { converted }));

                        }

                        throw new Exception(string.Format("{0} must implement CompareTo(Object) to use the GreaterThan conditional", type));

                    };

    return predicate;

}
{% endhighlight %}

The `TypeResolver` class is analogous to the `MethodResolver` class I talked about in a previous post, but it finds types by name instead of methods.

One advantage to coding with design patterns is that they isolate concerns. Once I got a `ConditionCommand` to be created correctly, the rest of the conversion engine worked like a charm!
