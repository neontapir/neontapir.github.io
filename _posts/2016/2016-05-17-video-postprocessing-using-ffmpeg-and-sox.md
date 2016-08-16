---
layout: post
title: "Video Post-Processing Using FFmpeg and SoX"
date: 2016-05-17 09:00:00
categories:
- personal
tags:
- FFmpeg
- SoX
- ImageMagick
- post-processing
- audio
- video
---

{% include side-image.html image="audio_processing.jpg" %}

As an experiment, I recently recorded a lunch and learn session at work. The
other R&D offices post theirs online, so I thought I'd do the same. On my work
machine, my choice of tools is limited. As I researched the subject, I learned
some good techniques and wanted to share.

Our office has a GoPro, but its microphone doesn't record sound well, so I
brought in my decade-old SD camcorder. The raw footage formed a "minimal viable
product". I pointed the camera at the slideshow, made sure the speaker Paul was
in the frame, and recorded for 50 minutes. The slides are legible, and you can
make out what Paul is saying.

In retrospect, I wish I had a fill light on Paul. The white slides washed him
out, and the age of the camera meant that the camera couldn't cope. The colors
were washed out, and Paul is a shadowy figure in the corner of the frame. The
camcorder uses a proprietary .MOD file format and the raw footage was 1.8 GB,
too bulky to share.

Aside from compressing it, I felt there were a couple of small things I could do
to enhance the quality of the video.

<!--more-->

The room had an air vent that was running
throughout his talk. And, I wanted to preface the video with a title screen.

My work computer is a Mac, but I don't have carte blanche to install anything I
want. But I can install programs, so I downloaded all the tools I needed via
Homebrew. I used [FFmpeg](https://ffmpeg.org) for video,
[SoX](http://sox.sourceforge.net) for audio,
and [ImageMagick](http://www.imagemagick.org) for pictures.

{% highlight bash %}

brew install ffmpeg
brew install sox
brew install ImageMagick

{% endhighlight %}

The first thing I needed to do was discover what a .MOD file is. I learned that
a .MOD file is just a camcorder manufacturer specific MPEG-2 container. I was
able to just rename it to an .mpg extension and proceed.

### Step 1: Clean audio noise

I found a site that outlines [how to use SoX to eliminate noise]( http://www.zoharbabin.com/how-to-do-noise-reduction-using-ffmpeg-and-sox/). I
customized this procedure for my workflow.

First, I split the audio and video streams into 2 separate files:

* The video stream: `ffmpeg -i input.mp4 -qscale 0 -an tmpvid.mp4`
* The audio stream: `ffmpeg -i input.mp4 -qscale 0 tmpaud.wav`

I started operating on the audio stream using SoX. The goal was to filter out
the background noise. In addition to the `sox` command itself, SoX distributes
some helper scripts like `play`, which assumes some command-line arguments. I
used `play tmpaud.wav` to listen and find a section of background noise.

As I narrowed in on a section of silence in the audio, I used a different form
on the command to make sure that I was only getting silence, `play tmpaud.wav
trim 96.0 1.5`. The first number is the playback start position, and the second
number is the duration, both given in seconds.

Then, I used FFmpeg to extract that portion of the audio, where `-ss` is the
time offset from beginning in (hh:mm:ss.ms) format, and `-t` is the duration in
seconds.

{% highlight bash %}
ffmpeg -i input.mp4 -vn -ss 00:00:00 -t 00:00:01 noiseaud.wav
{% endhighlight %}

Once I had a sample of the background noise, I could use SoX to create a
"profile", via:

{% highlight bash %}
sox noiseaud.wav -n noiseprof noise.prof
{% endhighlight %}

In this case, the profile will be used to filter out the noise, like so:

{% highlight bash %}
sox tmpaud.wav tmpaud-clean.wav noisered noise.prof 0.15
{% endhighlight %}

The tutorial page suggests a sensitivity threshold in a range of .21-.3, but I
found that even .21 introduced some attenuation. However, .15 left enough of
Paul's voice that he was intelligible when he was talking quietly.

Each time I generated a new `tmpaud-clean.wav` file, I listened to it with
`play tmpaud-clean.wav`. When I was satisfied with the results, I used FFmpeg
to merge (remux) the two streams back together:

{% highlight bash %}
ffmpeg -i tmpaud-clean.wav -i tmpvid.mp4 -q:a 0 -q:v 0 presentation.mp4
{% endhighlight %}

The `q:a` and `q:v` arguments tell FFmpeg to preserve the quality settings of
the input streams.

### Step 2: Create a title banner video

I created the image using PowerPoint, which I already had installed. I used a
branded title page to put the title of Paul's talk and his contact information.
I exported that slide to a JPEG of size 720x405, `title.jpg`.

In order to combine this with my presentation, I need to convert the still
picture into a video file that contains a video track and a blank audio track.

The first task was to create an audio file with X seconds of silence. The
easiest way I found is to have SoX generate the silence, and then use a script
to put it in a WAV file format. I found a person who wrote a [Perl script to
generate silence](http://www.boutell.com/scripts/silence.html). It's called like
this: `perl silence.pl 5 silence.wav` to yield 5 seconds of silence. His script
is in the public domain, so I'm reproducing the contents of silence.pl here:

{% highlight perl %}
#!/usr/bin/perl
# Courtesy of http://www.boutell.com/scripts/silence.html

$seconds, $file = @ARGV;
if ((!$seconds) || ($file eq "")) {
  die "Usage: silence seconds newfilename.wav\n";
}

open(OUT, ">/tmp/$$.dat");
print OUT "; SampleRate 8000\n";
$samples = $seconds * 8000;
for ($i = 0; ($i < $samples); $i++) {
  print OUT $i / 8000, "\t0\n";
}
close(OUT);

system("sox /tmp/$$.dat -c 2 -r 44100 -e signed-integer $file");
unlink("/tmp/$$.dat");
{% endhighlight %}

I ran into a snag with the next step. As I said, PowerPoint exports in 720x405,
whereas the camcorder records in 720x404. That one extra line caused me a
headache because of a known bug in the H.264 encoder, producing the error
"height not divisible by 2". To fix this, I found out I could add this argument
to any FFmpeg command: `-vf 'scale=trunc(iw/2)*2:trunc(ih/2)*2'`. In a nutshell,
this calculation reads the height and width from the input file and rounds them
to the nearest even value.

Because of the H.264 bug mentioned above, I used ImageMagick to resize my slide
export to a height with an even number:

{% highlight bash %}
convert -resize 720x404 title-source.jpg title.jpg
{% endhighlight %}

Then, I combined the video and audio streams into a video file with FFmpeg:

{% highlight bash %}
ffmpeg -loop 1 -i title.jpg -i silence.wav -c:v libx264 -t 5 -pix_fmt yuv420p title.mp4
{% endhighlight  %}

For this command to work, the `silence.wav` file needs to be at least as long as
the loop time (specified here by '-t 5').

### Step 3: Put these two videos that are different sizes together

This step one took a while to figure out. Once I used convert to make the file
sizes the same as shown above, I still couldn't proceed because of this
recurring error:

> Input link in1:v0 parameters (size 718x404, SAR 3232:3231) do not match the
corresponding output link in0:v0 parameters (718x404, SAR 1:1)

It turns out that for concat to work, the videos not only need to be the same
size, but also have the same values for a couple of technical parameters like
screen aspect ration (SAR). After some experimentation, I learned to fixed the
size and SAR of the second video on the fly to equal the first with the
following command:

{% highlight bash %}
ffmpeg -i title.mp4 -i presentation.mp4 -filter_complex \
'[1:v:0] scale=718x404,setsar=sar=1 [1v]; [0:v:0] [0:a:0] [1v] [1:a:0] \
concat=n=2:v=1:a=1 [v] [a]' -map '[v]' -map '[a]' out.mp4
{% endhighlight %}

Let me unpack that `filter_complex` argument. Sections are semicolon delimited.
The first section takes the second source’s first (and only) video segment
`1:v:0`, scales it, and sets its SAR, naming the resulting stream “1v"
(which I named arbitrarily).

Stream 1v gets piped to the next operation, which does the concatenation. I
specify source 0, then source 1, then say I’m going to concatenate them (2
sources into 1 video, 1 audio). Since this is a pipe, I need to terminate the
pipe. This is handled by the map operations, which name the results ‘v’ and ‘a’
(also arbitrary names).

### Step 4: Reduce file size

The resulting file was still really large, so I chose to compress it.

{% highlight bash %}
ffmpeg -i in.mp4 -c:v mpeg4 -preset slow -b:v 500k -maxrate 500k \
-bufsize 1000k -threads 0 -b:a 128k out.mp4
{% endhighlight %}

The “slow” preset is a good compromise between speed and quality. The result was
about 10% the size of the raw MPEG2 file.

### Step 5: Change file modification time

This one is the easiest of all.

{% highlight bash %}
touch -m -t 201605131100 out.mp4
{% endhighlight %}

This will make the file’s modification time May 13, 2016 at 11:00am. And, with
that, I distributed the talk to my colleagues in other offices!
