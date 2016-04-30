---
layout: post
comments: true
title: Conversion to Jekyll
categories:
- op-ed
tags:
- jekyll
status: publish
type: post
published: true

---
![Jekyll](/assets/jekyll-logo.png)

I've decided to convert this site from Wordpress to
[Jekyll](http://jekyllrb.com/), a Ruby static site generator that's suitable for
use with [GitHub Pages](https://pages.github.com/). GitHub Pages is attractive
because publishing is as easy as committing files to a repository.

I'm using [Qck-Theme](https://github.com/qckanemoto/jekyll-qck-theme) to style
the site, because it has a little customized theming, but is still simple.

Getting started is easy, although I learned a few things the hard way. I ended
up having to get help from GitHub Pages support, and their technicians were fast
and very knowledgable. Kudos to James and Steven!

First recommendation is to install Jekyll locally for site development. If you
plan to use GitHub Pages to host your site, do yourself a favor and use the
[pages-gem](https://github.com/github/pages-gem) to install Jekyll and its
dependencies. It uses the same versions of the gem files that GitHub does, so
you can eliminate some causes of odd behavior that way.

Second, this is open source software, so contribute where you can. I learned a
lot about Jekyll and how it generates sites by doing keyword searches on GitHub
through my theme's source code. I also found behavior worth a feature request
and a bug. When you fix it locally, isolate the fix and submit a patch!

I used the [WordpressDotCom
importer](http://import.jekyllrb.com/docs/wordpressdotcom/)  to pull my site
data from neontapir.com. It did a fairly good job, but there were a couple
gotchas.

The most annoying was that the importer used relative paths to the `/assets`
folder, where the images are stored. This meant that almost all the images on
the site were broken.

I used a command like this to fix it:

    ls _posts/* _pages/* | xargs perl -pi -e 's/img src="assets/img src="\/assets/'

A more insidious issue had to do with a bug in Jekyll itself. By the time you
read this, it's probably already been fixed, but Jekyll doesn't handle time
zones in the post dates in the front matter of articles. (Front matter is what
Jekyll calls post metadata like title, description and publication date.)

It manifested in an inability for the `post_url` directive to find other posts
by filename, even though they were in the folder. Files have the date encoded in
them, and the search function noticed there was a mismatch between the date in
the filename and in the front matter, so it wouldn't return the file. This
caused a site build failure that I couldn't reproduce locally.

The imported site was usable almost immediately, but it took another 2-3 hours
to get it looking half-decent. Most of that time was looking for links to other
posts and replacing them with post_url directives, as well as configuring
social sharing buttons and Disqus for comments.

Overall, I'd recommend it. For me, Jekyll lowers the barrier to entry for
writing new content, even if it's not as fully featured. That having been said,
I rarely used many of the features Wordpress offers.
