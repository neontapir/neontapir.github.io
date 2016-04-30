---
layout: post
comments: true
title: StarTeam's File Compare / Merge tool
date: 2009-03-31 14:12:08 -06:00
categories:
- professional
tags:
- compare
- merge
- review
- software
- starteam

---
I used to use DiffMerge as an alternate file compare/merge tool, but I've found that under StarTeam 2008 Release 2, it now leaves annotation artifacts in my file, something like this:

`[newer file]`

Since I'm working in C#, the compiler doesn't take too kindly to literal symbols in the middle of its files. For the time being, I'm resigned to using StarTeam's built-in tool.

One day, however, the built-in File Compare/Merge tool stopped working on me. The progress bar said "Finding Differences...", flickering from left to right, never completing.

I resolved the issue by stopping StarTeam and deleting the syncdb folder under my Local\\SettingsApplication\\DataBorlandStarTeam folder.

I hope this information helps someone. I wasn't able to find another page describing this. Anybody else have this issue?
