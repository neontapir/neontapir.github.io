#!/usr/bin/env python3
import feedparser
import html2markdown
import re

# <item>
#   <itunes:title>The Accountability Dial</itunes:title>
#   <title>The Accountability Dial</title>
#   <description><![CDATA[<p>In this episode, Chuck illustrates the use of Jonathan Raymond's Accountability Dial technique, with Manager Tools feedback examples as well.</p><p><a rel="payment" href="https://www.patreon.com/agilechuckwagon">Support the show</a> (https://www.patreon.com/agilechuckwagon)</p>]]></description>
#   <content:encoded><![CDATA[<p>In this episode, Chuck illustrates the use of Jonathan Raymond's Accountability Dial technique, with Manager Tools feedback examples as well.</p><p><a rel="payment" href="https://www.patreon.com/agilechuckwagon">Support the show</a> (https://www.patreon.com/agilechuckwagon)</p>]]></content:encoded>
#   <itunes:image href="https://storage.buzzsprout.com/variants/olq4a2ik13r4w1yqfllusnwim2ae/8d66eb17bb7d02ca4856ab443a78f2148cafbb129f58a3c81282007c6fe24ff2?.jpg" />
#   <itunes:author>Chuck Durfee</itunes:author>
#   <itunes:summary>In this episode, Chuck illustrates the use of Jonathan Raymond&#39;s Accountability Dial technique, with Manager Tools feedback examples as well.</itunes:summary>
#   <enclosure url="https://www.buzzsprout.com/277882/3008284-the-accountability-dial.mp3?blob_id=11193598" length="12358978" type="audio/mpeg" />
#   <guid isPermaLink="false">Buzzsprout-3008284</guid>
#   <pubDate>Wed, 25 Mar 2020 09:00:00 -0600</pubDate>
#   <itunes:duration>1027</itunes:duration>
#   <itunes:keywords>management, discipline, feedback, categories, scale</itunes:keywords>
#   <itunes:season>10</itunes:season>
#   <itunes:episode>6</itunes:episode>
#   <itunes:episodeType>full</itunes:episodeType>
#   <itunes:explicit>false</itunes:explicit>
# </item>

rss_url = "https://feeds.buzzsprout.com/277882.rss"

feed = feedparser.parse( rss_url )
items = feed["items"]
for item in items:
    # print(item)
    # print(item['tags'])
    # for tag in item['tags']:
    #   print(tag['term'])

    time = item[ "published_parsed" ]
    title = item[ "title" ].replace(':', " -") #.encode('utf-8')
    fileName = str(time.tm_year) + '-' + ("%02d" % time.tm_mon) + '-' + ("%02d" % time.tm_mday) + '-' + title + '.md'
    fileName = re.sub("[/']", '', fileName)
    fileName = fileName.replace(' ', '-').replace('---', '-')
    duration = str(round(float(item["itunes_duration"]) / 60))
    value = item["content"][0]['value']
    value = re.sub('<p>This episode is sponsored by .*</p>', '', value)
    value = re.sub('<a.+rel="payment".*>.+</a>', '', value)
    value = re.sub('<p>\s*</p>', '', value)
    value = value.replace('(https://www.patreon.com/agilechuckwagon)', '')
    value = html2markdown.convert(value) + ' (length: ' + duration + ' min)'
    value = value.replace('&nbsp;', ' ')
    
    season = 0
    episode = 0
    match = re.match('.*(\d+)x(\d+).*', title)
    if match:
      season = str(int(match.group(1)))
      episode = str(int(match.group(2)))
      title = re.sub('.*(\d+)x(\d+).*', '', title)
    else:
      season = item["itunes_season"]
      episode = item["itunes_episode"]
    
    f = open(fileName,'w') 
    f.write('---\nlayout: post\ntitle: ' + title + '\n')
    if item.has_key('image'):
      f.write('eye_catch: ' + item['image']['href'] + '\n')
    f.write('tags:\n- agile-chuck-wagon\n')
    if item.has_key('tags'):
      for tag in item['tags']:
        f.write('- ' + tag['term'] + '\n')
    f.write('''comments: true
categories:
- professional
- podcast
status: publish
published: true
meta:
  _edit_last: "1"
type: post
---

''')
    f.write('## Agile Chuck Wagon, season ' + season + ', episode ' + episode + '\n\n')
    f.write(value + '\n')
    # break
print('end')
