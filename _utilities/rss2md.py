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

def parse_value(item):
  value = item["content"][0]['value']
  value = re.sub('<p>This episode is sponsored by .*</p>', '', value)
  value = re.sub('<a rel="payment" href="https://www.patreon.com/agilechuckwagon">.+</a>', '', value)
  value = value.replace('<p> (https://www.patreon.com/agilechuckwagon)</p>', '')
  value = re.sub('^\s+', '', value)
  value = re.sub('\s+$', '', value)
  value = html2markdown.convert(value) + ' (length: ' + duration + ' min)'
  value = value.replace('&nbsp;', ' ')
  return value

def parse_season_episode(item, title):
  match = re.match('.*(\d+)x(\d+).*', title)
  if match:
    season = str(int(match.group(1)))
    episode = str(int(match.group(2)))
    title = re.sub('.*(\d+)x(\d+).*', '', title)
  else:
    season = item["itunes_season"]
    episode = item["itunes_episode"]
  return (season, episode)

# rss_url = "277882.rss.txt" 
rss_url = "https://feeds.buzzsprout.com/277882.rss"

feed = feedparser.parse( rss_url )
items = feed["items"]
for item in items:
  # print(item)
  # print(item['tags'])
  # for tag in item['tags']:
  #   print(tag['term'])

  time = item[ "published_parsed" ]
  # if time.tm_year < 2020:
  #   continue

  title = item[ "title" ].replace(':', " -") #.encode('utf-8')
  
  fileName = str(time.tm_year) + '-' + ("%02d" % time.tm_mon) + '-' + ("%02d" % time.tm_mday) + '-' + title + '.md'
  fileName = re.sub("[/']", '', fileName)
  fileName = fileName.replace(' ', '-').replace('---', '-')
  fileName = '../_posts/' + str(time.tm_year) + '/' + fileName

  duration = str(round(float(item["itunes_duration"]) / 60))

  value = parse_value(item)

  episode_info = parse_season_episode(item, title)
  season = episode_info[0]
  episode = episode_info[1]
  
  f = open(fileName,'w') 
  f.write('---\ntype: post\nlayout: post\ntitle: ' + title + '\n')
  if item.has_key('image'):
    eye_catch = item['image']['href']
  else:
    eye_catch = "/assets/img/acw.png"
  f.write('eye_catch: ' + eye_catch + '\n')
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
---

''')
  f.write('### Agile Chuck Wagon, season ' + season + ', episode ' + episode + '\n\n')
  f.write(value + '\n')

print('...done')
