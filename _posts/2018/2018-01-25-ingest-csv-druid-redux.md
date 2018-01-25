---
layout: post
title: Ingesting CSV Files into Druid, Redux
date: 2018-01-25 10:00:00
description: Step-by-step instructions to ingest a CSV file into Druid
categories:
- professional
tags:
- actual
- average
- columns
- csv
- data
- data-analysis
- dataset
- druid
- error
- ingestion
- json
- metrics
- node
- precipitation
- weather
---

{% include side-image.html image="druid-icon.png" %}

Last year, I posted an article on my experience [ingesting a CSV file into Druid](<{% post_url 2017/2017-02-10-ingest-csv-druid %}>). Yesterday, I got an email from a reader who needed more detail to make it work. So, today, I recreated that work and am posting a step-by-step guide.

<!--more-->

The first step is to install Druid. I did this through Homebrew.

{% highlight bash %}
$ brew install druid
{% endhighlight %}

As of the time of this writing, Druid 0.11.0 is the latest.

Next, I went to Kaggle and downloaded a fresh copy of the [FiveThirtyEight dataset](https://www.kaggle.com/fivethirtyeight/fivethirtyeight/data), which is distributed as a ZIP file called `data.zip`.

I created a folder on my machine at `~/sandbox`, unzipped the data, and got started.

{% highlight bash %}
~/sandbox
▶ unzip data.zip
...
extracting: data/us-weather-history.zip
extracting: data/weather-check.zip
extracting: data/womens-world-cup-predictions.zip
extracting: data/world-cup-predictions.zip
▶ unzip data/us-weather-history.zip
▶ ls
data               data.zip           us-weather-history
▶ cd us-weather-history
~/sandbox/us-weather-history
▶ ls
KCLT.csv                KMDW.csv                visualize_weather.py
KCQT.csv                KNYC.csv                wunderground_parser.py
KHOU.csv                KPHL.csv                wunderground_scraper.py
KIND.csv                KPHX.csv
KJAX.csv                KSEA.csv
{% endhighlight %}

In particular, I'm interested in the file `us-weather-history/KSEA.csv`.

Okay, let's start following the [Druid quickstart guide](http://druid.io/docs/latest/tutorials/quickstart.html).

The first thing it wants it for Apache Zookeeper to be installed and started. I use Homebrew to ensure it's installed, find out where it's installed, and get it running.

{% highlight bash %}
~/Downloads
▶ brew install zookeeper
Updating Homebrew...
==> Auto-updated Homebrew!
Updated 1 tap (homebrew/core).

Warning: zookeeper 3.4.10 is already installed

▶ brew info zookeeper
zookeeper: stable 3.4.10 (bottled), HEAD
Centralized server for distributed coordination of services
<https://zookeeper.apache.org/>
/usr/local/Cellar/zookeeper/3.4.10 (241 files, 31.4MB) \*
  Poured from bottle on 2017-07-18 at 07:49:56
From: <https://github.com/Homebrew/homebrew-core/blob/master/Formula/zookeeper.rb>
==> Dependencies
Optional: python ✔
==> Options
\--with-perl
	Build Perl bindings
\--with-python
	Build with python support
\--HEAD
	Install HEAD version
==> Caveats
To have launchd start zookeeper now and restart at login:
  brew services start zookeeper
Or, if you don't want/need a background service you can just run:
  zkServer start

▶ zkServer start
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg
Starting zookeeper ... ./zkServer.sh: line 149: /usr/local/var/run/zookeeper/data/zookeeper_server.pid: Permission denied
FAILED TO WRITE PID

▶ sudo chmod -R g+w /usr/local/var/run/zookeeper
Password:

▶ zkServer start
ZooKeeper JMX enabled by default
Using config: /usr/local/etc/zookeeper/zoo.cfg
Starting zookeeper ... STARTED
{% endhighlight %}

You'll notice I had a false start due to permissions, since I'm running as a non-privileged user.

The next step is to start Druid. Again, I rely on Homebrew to tell me where Druid is installed.

{% highlight bash %}
▶ brew info druid
druid: stable 0.11.0
High-performance, column-oriented, distributed data store
<http://druid.io>
/usr/local/Cellar/druid/0.11.0 (478 files, 243.6MB) \*
  Built from source on 2018-01-25 at 10:26:40
...
~/Downloads
▶ cd /usr/local/Cellar/druid/0.11.0
Cellar/druid/0.11.0
▶ bin/init
zsh: no such file or directory: bin/init

Cellar/druid/0.11.0                                                           ⍉
▶ ls bin
druid-broker.sh        druid-jconsole.sh      druid-overlord.sh
druid-coordinator.sh   druid-middleManager.sh
druid-historical.sh    druid-node.sh
{% endhighlight %}

Darn. Let's try to install Druid using the quickstart guide instructions, to see if `bin/init` is included.

{% highlight bash %}
~/sandbox
▶ curl -O <http://static.druid.io/artifacts/releases/druid-0.11.0-bin.tar.gz>
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  219M  100  219M    0     0  13.5M      0  0:00:16  0:00:16 --:--:-- 22.7M

▶ tar -xzf druid-0.11.0-bin.tar.gz

▶ cd druid-0.11.0

~/sandbox/druid-0.11.0
▶ bin/init

~/sandbox/druid-0.11.0
▶
{% endhighlight %}

Success! Next, I run the commands in the tutorial that start Druid processes. I use iTerm2, so I used the Duplicate Tab command to create a new terminal window per process. For example:

{% highlight bash %}
Last login: Thu Jan 25 11:02:31 on ttys005

* * *

/ After the game the king and the pawn go in the same box. \\
\\                 -- Italian proverb                       /

* * *

        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||

~/sandbox/druid-0.11.0
▶ java `cat conf-quickstart/druid/middleManager/jvm.config | xargs` -cp "conf-quickstart/druid/\_common:conf-quickstart/druid/middleManager:lib/\*" io.druid.cli.Main server middleManager
2018-01-25T18:02:50,166 INFO [main] io.druid.guice.PropertiesModule - Loading properties from common.runtime.properties
... lots of log entries ...
{% endhighlight %}

The tutorial continues with importing some Wikipedia data. Let's continue to follow the tutorial to make sure Druid is set up correctly, then we'll import our CSV weather data.

{% highlight bash %}
~/sandbox/druid-0.11.0                                                        ⍉
▶ curl -X 'POST' -H 'Content-Type:application/json' -d @quickstart/wikiticker-index.json localhost:8090/druid/indexer/v1/task
{"task":"index_hadoop_wikiticker_2018-01-25T18:05:32.491Z"}%
{% endhighlight %}

That worked! The coordinator console at <http://localhost:8090/console.html> and the console at <http://localhost:8081/#/datasources> both show the `wikiticker` data we're expecting.

I cut and pasted the JSON file I created in my 2017 post into a file.

{% highlight bash %}
~/sandbox
▶ vi seattle-weather.json
{% endhighlight %}

As mentioned in my 2017 post, I also made some modification of the FiveThirtyEight datafile. I loaded the file in Excel and changed the date column format to 'yyyy-mm-dd' and saved the result.

{% highlight bash %}
~/sandbox/druid-0.11.0
▶ curl -X 'POST' -H 'Content-Type:application/json' -d @../seattle-weather.json localhost:8090/druid/indexer/v1/task
{"task":"index_hadoop_seattle-weather_2018-01-25T18:16:17.082Z"}%
{% endhighlight %}

Now, let's check the UI. First, the coordinator console at port 8090.

Ah, it appears the job has failed. Clicking on the log button, it's easy to see why:

`Input path does not exist: file:/Users/me/sandbox/druid-0.11.0/ksea.csv`

I moved up to the `sandbox` folder, then modified my `seattle-weather.json` file to match the location on disk. For the record, here's the file in its entirety:

{% highlight json %}
{
  "type": "index_hadoop",
  "spec": {
    "ioConfig": {
      "type": "hadoop",
      "inputSpec": {
        "type": "static",
        "paths": "../us-weather-history/KSEA.csv"
      }
    },
    "dataSchema": {
      "dataSource": "seattle-weather",
      "granularitySpec": {
        "type": "uniform",
        "segmentGranularity": "day",
        "queryGranularity": "none",
        "intervals": [
          "2014-07-01/2015-07-01"
        ]
      },
      "parser": {
        "type": "hadoopyString",
        "parseSpec": {
          "format": "csv",
          "timestampSpec": {
            "format": "yyyy-mm-dd",
            "column": "date"
          },
          "columns": [
            "date",
            "actual_mean_temp",
            "actual_min_temp",
            "actual_max_temp",
            "average_mean_temp",
            "average_min_temp",
            "average_max_temp",
            "record_mean_temp",
            "record_min_temp",
            "record_max_temp",
            "actual_precipitation",
            "average_precipitation",
            "record_precipitation"
          ],
          "dimensionsSpec": {
            "dimensions": [
              "actual_mean_temp",
              "actual_min_temp",
              "actual_max_temp",
              "average_mean_temp",
              "average_min_temp",
              "average_max_temp",
              "record_mean_temp",
              "record_min_temp",
              "record_max_temp",
              "actual_precipitation",
              "average_precipitation",
              "record_precipitation"
            ]
          }
        }
      },
      "metricsSpec": [
        {
          "name": "count",
          "type": "count"
        }
      ]
    },
    "tuningConfig": {
      "type": "hadoop",
      "partitionsSpec": {
        "type": "hashed",
        "targetPartitionSize": 5000000
      },
      "jobProperties": {}
    }
  }
}
{% endhighlight %}

Keep in mind that if you use a relative path like I did, it is relative to the folder you started the Druid processes in, in my case `sandbox/druid-0.11.0`.

{% highlight bash %}
~/sandbox
▶ curl -X 'POST' -H 'Content-Type:application/json' -d @./seattle-weather.json localhost:8090/druid/indexer/v1/task
{"task":"index_hadoop_seattle-weather_2018-01-25T18:20:29.870Z"}%
{% endhighlight %}

It tried for a while longer, but failed again. I saw JNDI and JMX exceptions again, like I did last year. However, toward the end, I did find some useful exceptions:

    Caused by: io.druid.java.util.common.RE: Failure on row[date,actual_mean_temp,actual_min_temp,actual_max_temp,average_min_temp,average_max_temp,record_min_temp,record_max_temp,record_min_temp_year,record_max_temp_year,actual_precipitation,average_precipitation,record_precipitation]
    Caused by: io.druid.java.util.common.parsers.ParseException: Unparseable timestamp found!
    Caused by: java.lang.IllegalArgumentException: Invalid format: "date"

I forgot to strip the header row out of the dataset. Running it again, I got a SUCCESS status in the coordinator console:

![Coordinator console screenshot](/assets/druid-coordinator-console-20180125.png "Coordinator console screenshot")

In the regular console on port 8081, `seattle-weather` now shows up as a disabled datasource.

![Console screenshot of disabled datasources](/assets/druid-disabled-datasources-20180125.png "Console screenshot of disabled datasources")

If you click on the `seattle-weather` link, it will offer to enable the datasource for you.

![Console screenshot of the enabled seattle-weather datasource](/assets/druid-seattleweather-datasource-20180125.png "Console screenshot of the enabled seattle-weather datasource")

I hope this post has been helpful.
