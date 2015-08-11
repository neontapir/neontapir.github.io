---
layout: post
comments: true
title: 'Rally data extract scripts: a Kanban experience report'
categories:
- coding
- process
- professional
tags:
- bash
- data
- experience
- kanban
- script
- story
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
excerpt: !ruby/object:Hpricot::Doc
  options: {}
---
This is the second in a series of blog posts about implementing Kanban on my current project. The first installment was about [establishing the flow](http://wp.me/p2vhlC-lM). This post talks about obtaining the data for the Kanban metrics. Later posts talk about the Excel spreadsheet that consumes the data.

[![script-bash](assets/script-bash.jpg)](http://neontapir.com/wp/wp-content/uploads/2014/06/script-bash.jpg)

My employer has standardized on [Rally](http://www.rallydev.com/), so we are using it for work item management. However, I've found that its Kanban flow support is not as robust as I need. I wanted to create several additional charts on some derived values, so I manually input some data for each story into Excel for my formulas and charts. Of course Rally supports custom applications in JavaScript, but I didn't relish the thought of performing statistical analysis in raw JavaScript. I chose to continue to use Excel for my metrics gathering.

After creating the first few, I started exploring the data and made more. At first, I would scour the revision history for the data I needed, but I quickly desired some automation. I wrote two shell scripts that query Rally's APIs for data. It currently takes me about 15 minutes a day of data entry to keep pace with the teams, which is short enough that I haven't taken the next step of converting a derivative of that script into a Excel data source.

Here's the output of my script, with some of the project-specific data scrubbed. I used [Fake Name Generator](http://www.fakenamegenerator.com/) to come up with poor Richard.

> Fake Name Generator generates a lot more than names. Except when I'm looking for character ideas for a story I'm writing, I only use it for realistic test data.

    $ ./storyQuery.sh 53142
    US12345 -- Reorganize test packages to support ease of testing
    Project: Backend
    Release: BETA
    Tags:

    State changes
    18641196378  2014-05-29  None         -------  Cedric Jorgenson
    Beta         2014-05-29  None         -------  Cedric Jorgenson
    Beta         2014-05-29  Ready        -------  Cedric Jorgenson
    Beta         2014-05-29  Design       -------  Gary Bennett
    Beta         2014-05-29  Development  -------  Peggy Bivens
    Beta         2014-05-30  Validation   -------  Richard Chenier
    Beta         2014-05-30  Validation   BLOCKED  Chuck Durfee
    Beta         2014-05-30  Validation   -------  Richard Chenier
    Beta         2014-05-30  Accepted     -------  Cedric Jorgenson

    User Count: 2
    Defects: 0 (NONE)
    Blocked: 1 hours
    Design: 0 hours
    Development: 25 hours
    Ready: 0 hours
    Validation: 0 hours

As you can see, the script uses both the story details and [Lookback](https://rally1.rallydev.com/analytics/doc/) APIs to get a concise history of the story. The story details API only provides rollup information; I need the Lookback API to get revision history.

In this case, Cedric is the [product owner](http://www.mountaingoatsoftware.com/agile/scrum/product-owner/), Gary is a quality engineer, and Peggy and Richard are developers on the project. Richard didn't implement the story, so he's handling validation. On stories that are risky or important to the project, a quality engineer will also perform ad-hoc testing.

My script doesn't do separate lookups to obtain names for person or release IDs, as you can see by the `18641205378` in the first line. For some enumerated value fields, you can request that Rally "hydrate" a field, but the updating user and release are not among them. Though written in [`bash`](http://www.gnu.org/s/bash), my script uses a [Perl](http://www.perl.org/) associative array to inject the names into the output. While there's a more complete call example later, that Perl call looks like this:

{% highlight bash %}
 | perl -pe '%users = (
 "10624400656","Cedric Jorgenson",
 "1191677143" ,"Chuck Durfee",
 "12294673246","Gary Bennett",
 "13318093404","Peggy Bivens",
 "13304263924","Richard Chenier",
 );
 foreach $key (keys %users) { s/$key/$users{$key}/g; }
 ' \
{% endhighlight %}

The `-e` option lets you execute Perl scripts inline. The `-p` option runs the script on each line in turn.

I use a separate query script to get a new person's name and update the script, which I run a handful of times a month. I get the release by hand, since setting up releases happens only a few times a year.

Here's how the story query script makes one of the Lookback API REST call gets some of its data. I defined `$KANBAN_FIELD` and `$MY_WORKSAPCE` earlier in the script. I parameterized `$KANBAN_FIELD` because the front-end team has a different workflow than the backend team and hence a different custom field in Rally to store the state.

{% highlight bash %}
 BODY=$(cat << EOF
 {
 "find" : { "FormattedID": "$STORY" },
 "fields" : ["ObjectID", "_ValidFrom", "_ValidTo", "Release", "Blocked", "$KANBAN_FIELD", "_User"],
 "compress" : true
 }
 EOF
 )

RESULTS=$(echo $BODY \
 | http -a $AUTH -j POST https://rally1.rallydev.com/analytics/v2.0/service/rally/workspace/
    $MY_WORKSPACE/artifact/snapshot/query.json \
 | json Results)
{% endhighlight %}

I'm using two CLI tools to help me, [httpie](http://httpie.org) and [json](http://trentm.com/json/). HTTPie is a Python script that simplifies cURL-style REST calls. The `-b` option only outputs the response body. The `-a` provides my Rally credentials. I don't store those in plaintext in the script, of course.

> If you're interested in seeing all the fields during script development, send `"fields": true` in the POST body.

The `json` tool is used to extract data from the REST call results. Here, I'm filtering the output to just the inner Results object. You can see `json`'s capabilities more clearly in the story details REST call:

{% highlight bash %}
 DETAILS=$(http -b -a $AUTH -j GET "$DETAILS_URL?query=(FormattedID =
   $STORY)&fetch=true&workspace=$WORKSPACE_URL")
 DETAILS_RESULTS=$(echo $DETAILS | json -D / QueryResult/Results)

if [[ $RAW = true ]]; then
 printf "Raw Details\r\n"
 echo $DETAILS_RESULTS | json
 fi

STORY_NAME=$(echo $DETAILS_RESULTS | json -a _refObjectName)
 DEFECT_STATUS=$(echo $DETAILS_RESULTS | json -a DefectStatus)
 DEFECT_COUNT=$(echo $DETAILS_RESULTS | json -D / -a Defects/Count)
 PROJECT_NAME=$(echo $DETAILS_RESULTS | json -D / -a Project/_refObjectName)
 RELEASE_NAME=$(echo $DETAILS_RESULTS | json -D / -a Release/_refObjectName)
 TAGS=$(echo $DETAILS_RESULTS | json -D / -a Tags/_tagsNameArray | json -a Name
   | tr '\n' ',' | sed -e "s/,$//;s/,/, /;")
{% endhighlight %}

The `-D` option on `json` sets the delimeter for the `-a` command, which causes `json` to parse each record of an array separately. To handle an array of arrays, you need to call `json` twice, as is done in for `$TAGS`. I use [`tr`](http://en.wikipedia.org/wiki/Tr_(Unix)) to translate the return character into a comma, and then [`sed`](http://www.grymoire.com/unix/sed.html) to do some inline substitutions. I also make use of GNU awk or [`gawk`](http://www.gnu.org/s/gawk/manual/gawk.html) to do some aggregation, as you can see from this excerpt:

{% highlight bash %}
 # Display blocked hours
 echo $RESULTS \
 | json -d, -a _ValidFrom _ValidTo Blocked \
 | grep true \
 | sed -e "s/9999-01-01T00:00:00.000Z/${NOW}/g;
 s/[TZ:-]/ /g;" \
 | gawk -F, '{d=(mktime($2)-mktime($1))
 printf ("%02d h\r\n",d/3600);}' \
 | gawk '{cnt+=$1}
 END{printf "Blocked: %s hours\r\n",cnt?cnt:0}'
{% endhighlight %}

Here, I use `json` to take the full JSON output of the REST call and strip out everything but the fields I specify. I then look for periods when the story is blocked (where the Blocked flag is true). I use `sed` to turn Rally's "max datetime" field into `$NOW`, which I obtain earlier. The first call to `gawk` takes the period of time and converts it into hours, whereas the second sums those times and reports the grand total. If the story was never blocked, it shows 0.

Armed with that summary, I then plug the data into my Excel spreadsheet, which is the topic of my next post. Then I'll talk about process violations.
