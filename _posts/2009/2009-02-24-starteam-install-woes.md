---
layout: post
comments: true
title: StarTeam install woes
date: 2009-02-24 10:30:43 -07:00
categories:
- professional
tags:
- cross-client
- jvm
- memory
- starteam
- startup

---
I spent two hours trying to figure out why StarTeam 2008 Release 2 Client wouldn't install correctly on my machine. Whenever I'd launch it, I'd get a "**Could not create the Java virtual machine**" error.

Rather than being a problem locating the Java Virtual Machine, as I'd previously thought, turns out it's a memory allocation issue. In `StarTeamCP.stjava`, the default option set is "-Xmx1024m". My machine doesn't have a gig of RAM to spare for a Java VM, hence the error. By setting it to "-Xmx512m", I was able to get up and running.

I'm posting this in the hopes someone can profit from my struggles this morning. Deep shame be unto Borland for:

1) Making the default 1 GB, which is unrealistic for quite a few machines, mine included  
2) Not putting it in their Platform Notes with the release documentation.
