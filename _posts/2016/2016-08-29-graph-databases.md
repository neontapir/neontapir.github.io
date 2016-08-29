---
layout: post
title: Introducing Graph Databases
date: 2016-08-29 15:00:00
description: A third kind of database, based on graph theory
categories:
- professional
tags:
- database
- relational
- graph
- twitter
- movie
- data
- example
- tutorial

---

{% include side-image.html image="Microsoft_Excel_2013_logo.png" width="25" %}

Today, I want to talk to you about a different kind of database than the ones
you are probably used to. I start with a brief description of common types of
databases, then introduce graph databases with a couple of examples.

<!-- more -->

If you have been in the software development industry for a long time, you
probably started with relational databases. If you've ever used a spreadsheet,
this concept should sound familiar. A relational database stores data items in
life-structured groups called tables that contains rows and columns. The row
represents a discrete piece of data, and a column represents a characteristic of
the item common to every row in the table. In a database proper, that structure
is enforced by a specification called a schema.

It's called a relational database because data characteristics like key values
can be used to relate items to rows in other tables without moving the data.
That saves on data storage costs and makes it easy to update, I can keep a
common value like the office's address in one table and my employees in other,
without having to store a copy of the office address with each employee. If the
office moves, I only have to update the address table, and that change will be
reflected for all those related employees.

{% include side-image.html image="jekyll-logo.png" width="25" %}

Relational database don't handle both unstructured data and large objects very
well. They also lead to situations where you have data structures that are only
supporting. For example, it's hard to imagine what I might want to use the
office address table for by itself, without knowing anything about the offices
those addresses belong to. It's possible to employ workarounds to combat these
issues, but it's often at the expense of usability and performance. As these
edge cases became more common, it led to the growth of a different style of
database that thrived in those circumstances.

The most common form of non-relational databases store data in records, which
are similar to tables in some respects, but those records do not have a strict
schema enforcing a structure. MongoDB and Cassandra as two well know
non-relational databases.

An example of this style of data store is a blog like this one. I'm using
Jekyll, which takes a set of files and compiles them into a static website. This
very blog entry is contained in a text file in a folder, lightly formatted using
the Markdown specification. The Jekyll engine reads through the file looking for
header text in a certain format called YAML (Yet Another Markup Language) in
order to know how to treat this blog entry: what category it belongs in, what
tags to apply, and so on.

{% include side-image.html image="logo-neo4j.svg" width="25" %}

There are other ways to store data that aren't relational, though, and one of
these ways is what I want to share with you. At work, our team makes heavy use
of a graph database engine called [Neo4J](https://neo4j.com/). Graph theory is a
mathematical discipline that speaks to the relationship between things, and a
graph database structures data into nodes and edges in accordance with that
theory. A node is like a record in a non-relational database, in that lacks a
lot of imposed structure. The power of a graph database comes from the way that
relationships between nodes are handled. In a relational database, these
relationships are modeled as links using common data values like IDs to connect
two rows. In a graph database, these relationships are called edges, and like
nodes, they can have attributes of their own.

Let me give you an example of why this might be useful. Let's say I have a movie
database. In a relational database, I might have a movie table, an actor table,
and a director table. Values in these three tables might be related through IDs.
However, let's look at an edge case. The 2004 film Primer was directed by Shane
Carruth, produced by Shane, written by Shane, and starred Shane. He also wrote
the music and edited the film. A relational database would have a difficult time
expressing the fact that all these Shanes are indeed the same person.

A graph database would have no such trouble. You could model this with two
nodes, a Primer node and a Shane Carruth node. These two nodes would have
multiple edges between these two nodes. There's a DIRECTED_BY edge, a WRITTEN_BY
edge, and so on. The case where there are multiple writers is easy for a graph
database, but can require a schema update with collateral code changes for a
relational database.

If you're interested in exploring such a database, Neo4J offers an [example
database](https://neo4j.com/developer/movie-database/) with IMDB-style records.
With a graph database, there's a SQL-esque language for expressing these queries
called Cypher. Neo4J has a page with [basic
queries](https://neo4j.com/developer/guide-build-a-recommendation-engine/#_basic_queries)
and explains them.

{% include side-image.html image="twitter-graph-data-model.png" width="25" %}

Not convinced about the utility of graph databases? How about a LinkedIn-style
query, again from the example page linked above. Let's say I want to find all
the "second-degree" actors of Tom Hanks. In other words, actors who have
appeared with Tom Hanks are direct or "first-degree" connections. Any actor
who's worked with a direct connection of Tom's who isn't a direct connection
would be one degree removed, or a second degree connection. In a relational
database, this would require a large association table with some subqueries to
achieve. Here's the query shown on that page:

{% highlight cypher %}
MATCH (tom:Person)-[:ACTED_IN]->(movie1)<-[:ACTED_IN]-(coActor:Person),
         (coActor)-[:ACTED_IN]->(movie2)<-[:ACTED_IN]-(coCoActor:Person)
WHERE tom.name = "Tom Hanks"
AND NOT (tom)-[:ACTED_IN]->(movie2)
RETURN coCoActor.name
{% endhighlight %}

I think Cypher queries are easy to read. Nodes are in parentheses. Edges are in
square brackets. Item specifications that need to be referred to elsewhere in
the query can be given names using colons, like the "tom" or "coActor" nodes.
Arrows between then show the direction of the relationship -- more on that in a
moment.

However, I prefer to play around with more personally meaningful data. The site
[Graph your network!](http://network.graphdemos.com/#browser) allows you to do
just that with your personal Twitter data. This is an interactive tutorial that
uses your public Twitter information as data. I've captured a picture of the
data model here.

Queries that graph databases excel at are ones that explore relationships with
the data. An example would be finding out people I'm mentioning on Twitter. In
this example, the Cypher query would be:

{% highlight cypher %}
MATCH
  (u:User {screen_name:'ChuckDurfee'})-[p:POSTS]->(t:Tweet)-[:MENTIONS]->(m:User)
WITH
  u,p,t,m, COUNT(m.screen_name) AS count
ORDER BY
  count DESC
RETURN
  u,p,t,m
LIMIT 10
{% endhighlight %}

If I want the reverse, people who mention me, I simply need to change the query
slightly:

{% highlight cypher %}
MATCH
  (u:User)-[p:POSTS]->(t:Tweet)-[:MENTIONS]->(m:User {screen_name:'ChuckDurfee'})
WITH
  u,p,t,m, COUNT(m.screen_name) AS count
ORDER BY
  count DESC
RETURN
  u,p,t,m
LIMIT 10
{% endhighlight %}

Notice here that the direction of the relationship has been reversed just by
changing the specification on the nodes. I could also rewrite this query by
changing the direction of the arrows.

{% highlight cypher %}
MATCH
  (u:User {screen_name:'ChuckDurfee'})<-[:MENTIONS]-(t:Tweet)<-[p:POSTS]-(m:User)
WITH
  u,p,t,m, COUNT(m.screen_name) AS count
ORDER BY
  count DESC
RETURN
  u,p,t,m
LIMIT 10
{% endhighlight %}

I hope this post has whet your appetite for looking into graph databases. They
can be powerful tools for analyzing the way items relate to one another.
