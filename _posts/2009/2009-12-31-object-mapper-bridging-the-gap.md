---
layout: post
comments: true
title: 'Object Mapper: Bridging the Gap'
date: 2009-12-31 15:35:48 -07:00
categories:
- professional
tags:
- Adapter
- array
- csharp
- design patterns
- ElementInfo
- Factory
- field
- FieldInfo
- IAccessor
- object mapper
- property
- PropertyInfo
- refactoring
- Reflection
---

Recently, I talked about the [generation gap]({% post_url 2009/2009-12-29-object-mapper-generation-gap %}) I faced when considering elements at different levels of the hierarchy. I have a partial solution.

Recall I have the following hierarchy of objects:

{% highlight csharp %}
Person { Name : string }  
Parent { Children : Person[] } is-a Person  
Grandparent { Grandchildren : Person[] } is-a Parent
{% endhighlight %}

So, I created the following test classes:

{% highlight csharp %}

public class Person
{

	public string _name;

	public string Name

	{

		get { return _name; }

		set { _name = value; }

	}

	public Person[] Siblings;

	public Person[] Parents;

}

public class Parent : Person

{

	public Person _firstborn;

	public string FirstbornsName;

	public Person Firstborn

	{

		get { return _firstborn; }

		set { _firstborn = value; }

	}

	public Person[] _children;

	public Person[] Children

	{

		get { return _children; }

		set { _children = value; }

	}

	public object this[int index]

	{

		get { return _children[index]; }

	}

}

public class Grandparent : Parent

{

	public Person[] _grandchildren;

	public Person[] Grandchildren

	{

		get { return _grandchildren; }

		set { _grandchildren = value; }

	}

}
{% endhighlight %}

Obviously, these test classes will never form the basis of a top-notch genealogy program, but they are adequate to serve my purpose.

And, with the changes I'm about to describe, I'm able to write a passing test like this:

{% highlight csharp %}
		[Test]

		public void Grandchildren_test()

		{

			string xmlToParse =

				string.Format(

					@"<?xml version=""1.0"" encoding=""utf-8""?>

<Maps>   

	<Source ID=""source1"" Type=""{2}"">

		<Target ID=""target1"" Type=""{1}"">

			<Element Source=""Children"" Target=""Siblings"" />

			<Element Source=""Grandchildren[0]"" Target=""Firstborn"" />

			<Element Source=""Grandchildren[0].Name"" Target=""FirstbornsName"" />

			<!-- <Element Source=""Name"" Target=""Parents[0].Name"" /> -->

		</Target>

	</Source>

</Maps>

", typeof(Person).FullName, typeof(Parent).FullName, typeof(Grandparent).FullName);

			MappingDocumentParsingEngine parser = new MappingDocumentParsingEngine();

			List<ElementBase> elements = new List<ElementBase>(parser.Parse(xmlToParse));

			ObjectConversionEngine converter = new ObjectConversionEngine(elements.ToArray());

			Grandparent ellis = new Grandparent();

			ellis._name = "Ellis";

			Person andy = new Person();

			andy._name = "Andy";

			Person steve = new Person();

			steve._name = "Steve";

			Parent charles = new Parent();

			charles._name = "Chuck";

			charles._children = new Person[] { andy };

			ellis._children = new Person[] { steve, charles };

			ellis._grandchildren = new Person[] { andy };

			Parent actual = (Parent)converter.Convert(ellis);

			Assert.AreEqual("Andy", actual.Firstborn.Name);

			Assert.Contains(actual.Siblings, steve);

			Assert.AreEqual("Andy", actual.FirstbornsName);

			Assert.AreEqual("Ellis", actual.Parents[0].Name);

		}

{% endhighlight %}

And, yes, I used some of my own family names for testing. And I crammed multiple tests into one for brevity.

The part of the design that made this painful before was my `ElementInfo` class. In the Reflection library, the `PropertyInfo` and `FieldInfo` classes are very similar, but their method signatures are slightly different to accommodate indexed properties. I wanted to avoid making this distinction throughout my code, so I created an Adapter class I called `ElementInfo` to provide the rest of my code a unified interface, exposing a `GetValue()`, `SetValue()`, and `Type`.

However, it turns out my `ElementInfo` class had two responsibilities:

1.  Make a distinction between a property and a field
2.  Act as an accessor for a type (that is, to get and set values)

As a result, it was hard to extend. So, I decided to separate the `ElementInfo` class into two. During this exercise, it dawned on me that properties and fields are collectively called accessors, which lit the way for me to redesign this part of the domain model.

It was the `ElementInfo` constructor that was determining whether an accessor was a property or a field, so its logic got moved to an AccessorFactory. I re-ran my test suite, and everything passed (it was all green).

Once I did that, `ElementInfo` just had that decision logic in its own methods. Remembering that my goal was to extend this class to handle more types of accessors, I extracted an `IAccessor` interface and made `ElementInfo` implement it. (I use ReSharper, so refactorings like this are largely automated.) I then used the "Use Base Type Where Possible..." refactoring, so that as much as possible, I wasn't using my old `ElementInfo` class.

I then created Property and Field classes that implemented `IAccessor`, and reprogrammed the `AccessorFactory` to return Property and Field objects instead of `ElementInfo` objects. Re-ran the tests; all were green except the indexed property tests. So I deleted the `ElementInfo` class.

Now, I was in the position to create some new `IAccessor` implementations. The first I did was `IndexedProperty`, which you may recall that I had put into `ElementInfo` from last time. As I hoped, the only thing I needed to do to integrate it was add it to the `Create()` method on the `AccessorFactory`. Ran the tests; test suite still shows all green.

The first new implementation I needed was something I started out calling IndexableProperty, the idea being that it was a property whose type could be accessed with an indexer. However, it quickly became an `ArrayProperty`, because in my use case, the only examples of this are arrays. The analogous `ArrayField` followed shortly thereafter. With these in place, the `Grandchildren[0]` -> `Firstborn` mapping works.

What about `Grandchild[0].Name`? The engine doesn't understand dot notation yet. So I created an `AccessorComposite` IAccessor that takes multiple accessors chained by dots. It splits the accessor string on the dots and calls the AccessorFactory on each fragment. Now the `Grandchildren[0].Name` -> `FirstbornsName` mapping works.

I still have a challenge ahead. The commented-out mapping, `Name` -> `Parents[0].Name`, still won't work. When the `AccessorComposite` tries to set the value of `Parents[0].Name`, it fails because `Parents` hasn't been initialized. I could create some code that would initialize the Parents array. If I did, the array of `Parents` would be `{ null }`, and trying to get the value of `null.Name` doesn't compute. I would need to have the array of Parents equal to `{ new Person() }`, and then try to set that new `Person`'s name. For me, this is beyond the call of duty of an accessor representation!

I need to decide whether the user should explicitly populate `Parents[0]` before trying to set the name in the mapping, and if so how, or whether some other part of the engine should handle it. I'm leaning towards making it an explicit initialization, because having an array be null or empty might have meaning to the consumer of a converted object, and I don't want to prevent the ability to return those special values.

Transforming arrays is a nice segue into some of the challenges of having to infer type information, which will be discussed in the next post.
