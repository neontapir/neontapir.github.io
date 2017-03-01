---
layout: post
title: Ingesting CSV Files into Druid
date: 2017-02-10 15:30:00
description: How to ingest a CSV file into Druid
categories:
- professional
tags:
- csv
- json
- druid
- node
- dataset
- data-analysis
- ingestion
- columns
- error
- metrics

---

{% include side-image.html image="druid-icon.png" %}

I'm just getting my feet wet in data analysis. My Boulder team has started
working with a distributed data store called [Druid](http://druid.io). I
encountered an issue when importing data from a CSV file, and I wanted to share
a way I found to do it.

<!--more-->

Early on, I learned that a distributed data store like Druid is akin to a
database, but one where information is stored on multiple nodes. Often, these
are non-relational stores, which allow for lightning quick data access.

I decided I wanted to get some hands-on experience with Druid, so I installed it
on my laptop. Normally, one would use Druid to ingest events from a stream like
Twitter or a "clickstream" (a record of web site activity). However, I didn't
have a ready stream of data handy. Plus, for the purpose of seeing what Druid is
capable of, a batch import of data from a static data table seemed like the
easiest way to get started.

The Druid quick start documentation uses a JSON file to demonstrate batch
ingestion. I played with their quick-start data for a bit, but there are only a
few dozen records and I wanted something more substantial. Also, I wanted to use
a dataset that was more personally relatable than Wikipedia edits from a year
ago. In particular, I found a set of weather data on
[Kaggle](https://www.kaggle.com/) that caught my eye. The folks at
[FiveThirtyEight](https://fivethirtyeight.com/) had scraped some data from
[Weather Underground](https://www.wunderground.com/) for some weather stations
across the country. It's a part of [this dataset](https://www.kaggle.com/fivethirtyeight/fivethirtyeight).

My first ingestion was Seattle's KSEA station data for 2014-2015, since I
vacationed in Seattle last summer. This dataset contains daily highs, lows, and
precipitation observations.

In order to ingest data into Druid, you post a message to a node called the
"overlord", which handles Druid task distribution. This triggers Druid to index
data in order to create Druid segments, time-partitioned sets of data. Once data
has been ingested into segments, you can leverage Druid to slice and dice the
data.

{% include pullquote.html text="It took me a lot of trial and error to hit upon
the correct JSON syntax" %}

It took me a lot of trial and error to hit upon the correct JSON syntax, and the
main purpose of this post is to share my findings. Without further ado, here's
the JSON specification for the indexing job:

{% highlight json %}
{
  "type": "index_hadoop",
  "spec": {
    "ioConfig": {
      "type": "hadoop",
      "inputSpec": {
        "type": "static",
        "paths": "ksea.csv"
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

I also made a couple of small changes to the CSV file itself, which I will
mention as I go along.

A lot of the CSV examples I found online use the 'firehose' method, but I was
unable to get it to work. Instead, I ended up modifying the JSON specification
in the quick-start guide, which uses a Hadoop job. Any section not mentioned
below was left untouched from the quick-start guide.

The `ioConfig` node now says that we're using a flat file called 'KSEA.csv' as
our data source. I modified the `dataSource` node to give my dataset a
meaningful name ("seattle-weather") and to specify the range of data I wanted
(`intervals`).

I heavily modified the `parser` node. In the `parseSpec` node, I changed the
type from "json" to "csv". The [ingestion
documentation](http://druid.io/docs/latest/ingestion/) lists the high-level
nodes that are needed, but I found the documentation sparse in detail beyond
that.

This is the section that took the most time to get right. I found the errors
Druid gave were not intuitive at first. Fortunately, I have a lot of experience
reading stack traces and eventually was able to figure out what was going on
without resorting to reading the source code! It turned out the JNDI and JMX
errors were red herrings, and don't affect the parsing process. There were
several varieties of objects being null, which I later learned were the result
of omissions in my JSON file.

I changed the `timestamp` node to use the `date` column in the CSV file. I also
updated  the CSV file to put the date in a format I found easier to read. This
step wasn't strictly necessary, but I knew the 'yyyy-mm-dd' date specification
format off the top of my head.

A word about Druid segments. A segment can be envisioned as a table with columns
composed of a timestamp, a set of dimensions, and a set of metrics. Dimensions
are raw data values, whereas metrics are calculated values.

Knowing about segments makes the `parser` node easy to understand. The `columns`
array lists the columns in the CSV source file, in order. The `timestampSpec`,
`dimensionSpec`, and `metricsSpec` tells Druid how to ingest the source values
into a segment. For the purpose of getting this working, I chose a simple
metric, "count".

After getting all these sections straight, I hit a more intuitive error. It
turns out that with this configuration, Druid could not make sense of the header
row in the CSV file. Rather than try to find out how to tell Druid to ignore the
header, I simply removed it from the CSV file.

And thus, after a dozen tries, I got the data into Druid! Now that I have
ingestion working, the next step is to choose some more interesting metrics to
measure. For example, I could import multiple stations data and use a metric to
capture the city.
