---
layout: post
comments: true
title: 'Object Mapper: Accepting File Input'
date: 2010-01-08 12:06:18 -07:00
categories:
- professional
tags:
- csharp
- file
- object mapper
- parsing engine
- URI
---

The work on the Object Mapper is nearly complete from when we left off with the [conversion engine]({% post_url 2010/2010-01-06-the-object-mappers-conversion-engine %}).

I did enhance the parsing engine, though. My co-worker was trying to consume the engine, so he was reading in his document and extracting the text. We decided this was a common enough activity it would be worth adding to the parsing engine.

I didn't want to pass in the filename as a string, because it would mean that the parsing engine would also become responsible for determining if a string contained a filename or an XML string. One rule of thumb is to avoid using primitives like strings to represent concepts -- things with rules -- like filenames. Instead, create a class to be the custodian of that knowledge.

The .NET Framework already has such a class, System.Uri. The nice thing about using a URI is that any network location can also be used, not just a filename, and I get some simple validation capability.

Integrating the URI was easy. The parsing engine wraps the input string into a StringReader and creates an XmlReader from that with which to do its work. And really, any TextReader would do, which made the enhancement easy. I created an overload that accepts a URI and wraps it in a StreamReader, which is also a TextReader. Problem solved!
