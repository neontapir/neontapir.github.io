---
layout: post
title: In Praise of Sass
date: 2016-08-16 15:00:00
description: How I use Sass on my blog
categories:
- personal
tags:
- blog
- color
- functions
- jekyll
- sass
- style
- website
---

{% include side-image.html image="sass-logo.svg" %}

I know Sass isn't the only game in town when it comes to higher-order CSS
styling languages. However, it's the one supported by the Jekyll theme I'm
using, so I've been dabbling in it.

<!--more-->

One thing I love is the color functions that Sass provides. They make it really
easy to stick with a color scheme, because you can use them to style your site
with just a few colors without having to manually calculate RGB values. Jekyll
is a static site generator, so these values get calculated at compile time. For
example, it allows me to define my blog's color scheme like so:

{% highlight sass %}
$page-title-color: goldenrod;
$page-title-outline: darken($page-title-color, 20%);

$text-color: black;
$caption-color: lighten($text-color, 50%);

$brand-color: #44eeff;
$link-color: darken(desaturate($brand-color, 50%), 20%);
$pullquote-color: adjust-hue($link-color, 20deg);
{% endhighlight %}

{% include pullquote.html text="You can do more with Sass than just
change the brightness of colors." %}

The `lighten` and `darken` functions behave as you would expect, making the
color brighter or dimmer. Since this is the "neon" tapir, my base color is
rather bright. I use the `desaturate` function to keep the link color
more closely resembling the brand color, then I `darken` the result for
readability. For the pull quote color, I wanted it to stand out some, so
I used the `adjust-hue` function to go a certain distance around the color
wheel. In my case, it turned a blue-green link color into a purer blue.

I figured out these values through trial and error, by reading through
documentation and trying out individual functions on their own. However, I found
a site that provides an interactive guide, [A visual guide to Sass and Compass
Color Functions](http://jackiebalzer.com/color). The site only offers a color
picker, so I couldn't get quite the exact hue I wanted. Nevertheless, a site
like this greatly speeds up the process.

For example, I didn't see the application of the `shade` function to my color
scheme until I started looking at this site. However, I found in experimenting
that some of these color functions return results that can't be used by other
ones. For example, `lighten(shade($color, 20%), 10%)` throws an error in one of
the Jekyll converters.

The site showed me the effects of various functions, as well as allowing me to
tweak the values without having to rebuild my site to see the changes. Had I
used this site originally, I feel sure I would have ditched the neon green
secondary coloring much faster. I think the goldenrod makes for a more readable
design while still fitting in with the "neon" theme. Let me know what you think.
