---
layout: post
comments: true
title: 'Object Mapper: XML Parsing'
date: 2009-12-30 16:55:55 -07:00
categories:
- professional
tags:
- array
- csharp
- Command
- composite
- converter
- decorator
- design patterns
- element
- injector
- object
- object mapper
- parser
- parsing
- schema
- setter
- transformation
- XML
- XmlReader
- XSD

---
Recently, I've described [the object mapper's domain model]({% post_url 2009-12-28-the-object-mapper-domain-model %}) and illustrated that it's still evolving by discussing the "[generation gap]({% post_url 2009-12-29-object-mapper-generation-gap %})". In this post, I talk about the components of the object mapper.

There are two main components to the object mapper. Since the mapper is configured via XML, clearly I need something to read in the XML and initialize the domain model. Because I'm constrained to C# 2.0, I used an XmlReader. To handle malformed mapping XML documents, I wrote an XSD schema and validate incoming XML before parsing.

Each node triggers the creation of a domain object. Each Source and Target is implemented with the [Composite pattern](http://en.wikipedia.org/wiki/Composite_pattern) as an Element. Sources are comprised of Targets, and Targets are comprised of leaf elements like property mappings.

Each component of the Element Composite exposes an Execute method that calls a [Command](http://en.wikipedia.org/wiki/Command_pattern). There are two sets of commands: one working on objects, the other on elements (properties or fields). For example, there is an ObjectSetter, that simply sets the target to the source. Correspondingly, an ElementSetter sets the target property value to the source property's value.

Other types of Commands include an ObjectConverter, which invokes the conversion Function on the source and sets the target object equal to the result, and an ElementInjector, which sets a target element equal to a value specified in the mapping XML.

Array transformations are handled by way of a [Decorator](http://en.wikipedia.org/wiki/Decorator_pattern), which handles the invocation of the decorated Command on each element in the array.

Next post, I'll talk about how I made some progress on bridging that generation gap.
