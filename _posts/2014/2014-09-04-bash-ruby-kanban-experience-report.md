---
layout: post
comments: true
title: 'From Bash to Ruby: A Kanban experience report'
date: 2014-09-04 21:27:10.000000000 -06:00
categories:
- coding
- process
tags:
- bash
- docker
- kanban
- rspec
- ruby
- script
- slop
- vagrant
- vcr
status: publish
type: post
published: true
author:
  login: Chuck
  email: neontapir@gmail.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
![rubylang](/assets/rubylang.png)

In the intervening months since my last post, the project has accelerated significantly. We released the first version of the platform, and now are adding features to meet an aggressive migration schedule. I even traveled to Minsk, Belarus to meet our contractor team, to do some process training, and to discuss strategies for improving our communication and throughput.

There have been some process improvements too. I got tired of manually inputting the output of [my Bash script]({% post_url 2014-06-12-rally-data-extract-scripts-kanban-experience-report %}), so I converted the script into a **Ruby** program. I wanted to share some of the implementation details, specifically the libraries I used. I am a Ruby novice, so I consciously chose not to use the Rally gem that's available as a learning experience.

The application now supports two output modes: screen (the original output) and a pipe-delimited export file. My needs are very simple, so I use **slop** for command-line option parsing. The Ruby script also accepts an input file, instead of getting data one work item at a time.

I chose **mustache** as a template engine, and implemented the Strategy design pattern to switch between them based on a command-line parameter. While mustache is frequently used for HTML output, I found that it handles plain-text output just as well.

I'm using **rspec** for testing. I could not have gotten this application working without **vcr**. This application makes a lot of REST calls via **rest-client** and **json**, and I didn't want to spam Rally every time I ran my test suite. With the vcr module in place, I captured the result of those calls once, and they are replayed when the code under test requests data. Pure gold.

While I can use the pipe-delimited export file as a data feed for Excel, the script will need some features to emulate some "processing" I was doing by hand. For example, there are still times when work items are moved backward on the Kanban board. In those cases, the Ruby script reports a negative duration in a process state.

However, the script has had to wait. I've been tasked with getting a Vagrant image and Docker environment for our platform created. The immediate need is so that we can on-ramp temporary developers quickly. There are other use cases, though. We could use Docker as a way to deploy our platform to a cloud provider. We could use the image for our sales folks, who could use a standalone configuration of the platform to demonstrate products to customers. I partnered with our build engineer, and I'm testing the first version now.
