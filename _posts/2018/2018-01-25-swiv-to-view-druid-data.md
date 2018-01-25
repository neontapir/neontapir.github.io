---
layout: post
title: Using Swiv to Visualize Druid
date: 2018-01-25 12:00:00
description: Step-by-step instructions to visualize Druid data using Swiv
categories:
- professional
tags:
- data
- data-analysis
- dataset
- druid
- node
- weather
- swiv
---

{% include side-image.html image="swiv-logo.png" %}

Last year, I posted an article on my experience [ingesting a CSV file into Druid](<{% post_url 2017/2017-02-10-ingest-csv-druid %}>). Today, I recreated that work and am posting a [step-by-step guide](<{% post_url 2018/2018-01-25-ingest-csv-druid-redux%}>). You may be wondering what you can do with Druid data, so I wrote up a quick follow-up.

<!--more-->

For this step, I'm going to use the open-source visualizaton tool Swiv, which used to be Pivot.

{% highlight bash %}
git/github/yahoo
▶ git clone git@github.com:yahoo/swiv.git
Cloning into 'swiv'...
remote: Counting objects: 19407, done.
remote: Total 19407 (delta 0), reused 0 (delta 0), pack-reused 19407
Receiving objects: 100% (19407/19407), 46.22 MiB | 3.98 MiB/s, done.
Resolving deltas: 100% (13155/13155), done.

git/github/yahoo
▶ cd swiv

github/yahoo/swiv  master ✔                                             188d  ⍉
▶ sudo npm i -g yahoo-swiv
npm WARN deprecated fs-promise@0.5.0: Use mz or fs-extra^3.0 with Promise Support
npm WARN deprecated node-uuid@1.4.7: Use uuid module instead
/usr/local/bin/swiv -> /usr/local/lib/node_modules/yahoo-swiv/bin/swiv
\+ yahoo-swiv@0.9.42
added 207 packages in 9.693s
sudo npm i -g yahoo-swiv  13.37s user 5.24s system 180% cpu 10.320 total

github/yahoo/swiv  master ✔                                              188d
▶ swiv --druid localhost:8082
Starting Swiv v0.9.42
Adding cluster manager for 'druid' with 0 dataCubes
Swiv is listening on address :: port 9090
{% endhighlight %}

And voilà, <http://localhost:9090> leads to a data visualization tool! For some reason, the datasource names were not showing in the UI, but I have only two, so it was easy to find my `seattle-weather` data. A few drag and drops later, I got the following:

![Swiv screenshot](/assets/swiv-example-20180125.png "Swiv screenshot")

The distribution of counts of various precipitation values is not very interesting, but it should be enough to show how to use Swiv to visualize Druid data.
