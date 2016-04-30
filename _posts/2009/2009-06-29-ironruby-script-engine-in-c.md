---
layout: post
comments: true
title: IronRuby script engine in C#
date: 2009-06-29 11:40:32 -06:00
categories:
- professional
tags:
- csharp
- code
- engine
- extensions
- ironruby
- module
- programming
- script
- approaches
---
This post talks about the IronRuby engine we built. Our application has a requirement that certain elements of program logic must be able to be changed without a deployment. The application's initial architecture involved compiling C# functions on the fly, but it ran into memory pining issues after several hundred function sets had been loaded, which brought the application down every so often. Our team was charged with the task of preventing this situation while maintaining the feature.

We debated two approaches. We chose to use an interpreted script solution over a plug-in architecture because interpreted scripts are ideally suited to oft-changing code. Also, the logic is currently stored in XML files, and Ruby requires less character escaping than C# does when represented in XML. IronRuby won over IronPython because our team had a little experience with Ruby and none with Python.

The heart of the solution is a C# class called the IronRubyScriptEngine. In order to play along, you'll need to include the following assemblies from the IronRuby 0.5.0 distribution:

{% highlight csharp %}

using IronRuby;

using IronRuby.Builtins;

using Microsoft.Scripting.Hosting;

{% endhighlight %}

Here's the engine's constructor:

{% highlight csharp %}
public IronRubyScriptEngine()

{

    LoadRequiredAssemblies();

    _runtime = Ruby.CreateRuntime();

    _engine = Ruby.GetEngine(_runtime);             

    ResetScope();

}

/// <summary>

/// We need the assembly loaded into memory before CreateRuntime() is called, so we force it here.

/// </summary>

private static void LoadRequiredAssemblies()

{

    ClrString.IsEmpty("");

}

/// <summary>

/// Resets the scope, allowing you to run the same script against multiple inputs.

/// </summary>

public void ResetScope()

{

    _scope = _engine.CreateScope();

}

{% endhighlight %}

As you can see, creating an IronRuby engine in C# is very easy.

We pass parameters into our engine with a method called SetParameter. More on this in a moment.

{% highlight csharp %}

public IronRubyScriptEngine SetParameter(string parameterName, object value)

{

    _scope.SetVariable(parameterName, value);

    return this;

}

{% endhighlight %}

The real work is done inside the `Invoke` method, which wraps a snippet of Ruby code in a Proc. It dynamically creates the correct input parameter syntax, interprets the snippet, then invokes the script with the values of the parameters.

{% highlight csharp %}
private object Invoke(string script)

{

    var variableNames = _scope.GetVariableNames();

    string expression = string.Format("Proc.new {% raw %} {{ |{0}| {1} }} {% endraw %}", variableNames.ToDelimitedString(", "), script);

    ScriptSource source = _engine.CreateScriptSourceFromString(expression);

    var proc = (Proc) source.Execute();

    Proc lambda = proc.ToLambda();

    object[] scopeVariables = variableNames.Select(name => _scope.GetVariable(name)).ToArray();

    return lambda.Call(scopeVariables);

}

{% endhighlight %}

Let's say I have a `Person` class, and I want to determine if the person is happy. By using `SetParameters`, I can associate an object with a parameter name, so that if I write a snippet `bob.happy?`, the engine creates `Proc.new {% raw %} {{ |bob| bob.happy? }} {% endraw %}` and when called, my Person class instance is passed in.

As most Ruby afficionados know, Procs and Lambdas differ in how they handle the return keyword. We chose Lambdas so that return exits the scope like it would in a C# method.

`ToDelimitedString` is a simple yet handy extension method on `IEnumerable`.

{% highlight csharp %}
public static string ToDelimitedString<T>(this IEnumerable<T> sequence, char delimiter)

{

    return DelimitValues(sequence, delimiter.ToString());

}

public static string ToDelimitedString<T>(this IEnumerable<T> sequence, string delimiter)

{

    return DelimitValues(sequence, delimiter);

}

private static string DelimitValues<T>(IEnumerable<T> sequence, string delimiter)

{

    string[] values = sequence.Select(x => x.ToString()).ToArray();

    return string.Join(delimiter, values);

}

{% endhighlight %}

With this engine in place, it was easy to migrate our existing logic into Ruby functions. The final version of the engine includes script caching, so we don't interpret the same function over and over.

As the migration proceeded, we decided to refactor some of the logic to re-use code, something that was difficult in the old architecture. In Ruby, it's easy to extend a class. In IronRuby, you can certainly do that with CLR classes as well. However, the classes we needed to extend exist on the wrong side of a `Remoting` boundary. Extending an anonymous `RemotingProxy` of the class proved tough, so we chose to extend the object instead.

{% highlight ruby %}
module FooExtensions  
  def extended?  
    true  
  end  
end
{% endhighlight %}

In the snippet, we apply the extension with the following code:

{% highlight ruby %}
require 'FooExtensions.rb'  
myFoo.extend FooExtensions  
myFoo.extended?  # returns true
{% endhighlight %}

Between the terseness of Ruby and re-use of code, we have much less code to maintain. Although the Ruby functions are slower than their C# counterparts, they are certainly performant enough for our scenario.

I hope this post has been interesting. Comments are welcome.
