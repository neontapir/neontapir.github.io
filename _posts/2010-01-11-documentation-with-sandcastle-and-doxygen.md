---
layout: post
comments: true
title: Code Documentation with Sandcastle and doxygen
categories:
- professional
tags:
- CHM
- documentation
- doxygen
- help files
- LaTeX
- object mapper
- RTF
- sandcastle
- SHFB
- XML comments
status: publish
type: post
published: true
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
Last time, we talked about [accepting file input]({% post_url 2010-01-08-object-mapper-accepting-file-input %}), the last feature added to the Object Mapper. Now, it has come time to document the module.

I use ReSharper to help code in Visual Studio, but it still doesn't generate XML comments as well as I'd like, so I also use GhostDoc, which turns code into better English than ReSharper does. There is still editing to do, for while describing the code in English is marginally useful, GhostDoc still cannot provide context.

Finding missing documentation was trial and error until I installed the AgentSmith ReSharper plug-in, which made finding them a breeze after I turned solution-wide analysis on and marked missing documentation as a ReSharper error. Once I had all the classes, properties, and methods documented, I set out in search of a tool to convert those XML comments into something nice.

The first tool I tried was Microsoft's Sandcastle. Sandcastle itself is tough to use, so I went to CodePlex and also downloaded the [Sandcastle Help File Builder](http://www.codeplex.com/SHFB). It does a nice job of creating HTML and compressed help files (CHM).

I did have to alter a few things. I wanted namespace comments, and dug around a little before I discovered the Project Properties -> Comments expansion button on the right, and I typed those in. I did want to avoid outputting VB.NET and C++ contextual references, so I had to go into the Syntax Filters dialog and disable them. I also customized the root namespaces, help title, HTML help name, and copyright text, and I was ready to go.

But the requirement was to generate the documentation in Word. For as good as Sandcastle is, it doesn't seem to do anything but HTML and CHM.

The next tool I tried was [doxygen](http://www.doxygen.org/). It's a UNIX tool with Windows binaries, so it took a little more cajoling. At first, it wouldn't generate any content at all, but I got it working in short order after I saved its configuration file prior to rendering.

doxygen also supports more formats: LaTeX, RTF, and MAN pages, though it won't do CHM. RTF is a close cousin to Word document formatting, so I had high hopes. However, I found the generated RTF document disappointing, and later found a forum where the author admitted as much.

LaTeX is a great layout specification language, so I thought it might be a decent stepping stone to a Word doc. I spent a merry while trying to monkey with LaTeX2RTF, a free converter on sourceforge, but the results were disappointing. It couldn't understand doxygen's custom elements.

I'm still looking for a better solution, any ideas?
