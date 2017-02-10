---
layout: post
comments: true
title: Introducing the Object Mapper
date: 2009-12-23 04:12:29 -07:00
categories:
- professional
tags:
- csharp
- conversion
- Java
- object
- object mapper
- programming
- request
- response
- web service
- XML

---
In my last work-related post, I described ([the transition](%{ post_url 2009/2009-12-18-the-grass-may-be-greener-less-filling %}) from my old workplace to my new one. In it, I briefly mentioned the project I'm working on. In an upcoming series of posts, I'll highlight some of the technical challenges I faced while creating the object mapper service.

First, let me describe the object mapper service. Out there somewhere in the company, there exists a handful of Java applications that interface with a legacy application to get some data. That data is now also exposed by a .NET application I'll call the DataStore, so the goal is to retire the legacy application.

To do that, we're putting in place a .NET web service written in C# 2.0, which will accept requests from each of those Java applications. It takes the request, convert it to a DataStore request, execute the request, and then take the DataStore's response and convert it back into a response object that Java application can consume.

Most of the work of the web service is accomplished by passing messages from the Java application to the DataStore and back. However, the web service does need to convert requests and responses. Hard-coding the web service to do that would introduce some unwanted dependencies on the Java applications and the DataStore. Any time one of their requests or responses changed structure, the web service would need to change as well.

Instead, I've created a component that uses an XML document that describe how to map objects of one type to another to drive the conversion process. This is the object mapper.

The next post will describe the domain model of the object mapper.
