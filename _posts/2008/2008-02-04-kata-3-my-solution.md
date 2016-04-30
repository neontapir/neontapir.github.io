---
layout: post
comments: true
title: 'Code Kata 3: My Solution'
categories:
- professional
tags:
- code exercise
- estimation
- programming

---
[Kata 3](http://web.archive.org/web/20131016085513/http://codekata.pragprog.com/2007/01/kata_three_how_.html) has to do with estimation. The full questions are on Dave's blog.

How Big?

*   _Roughly how many binary digits (bit) are required for the unsigned representation of:_
    *   1,000 : **10**
    *   1,000,000 : **14**
    *   1,000,000,000 : **18**  
    *   1,000,000,000,000 : **22** 
    *   8,000,000,000,000 : **25**
*   _My town has approximately 20,000 residences...._ **_Let's allow 100 characters for a name, 150 for an address, and 15 characters for a phone number. 165 * 20000 = 310000 characters_** 
*   _I’m storing 1,000,000 integers in a binary tree...._ **I don't know much about binary trees, but I would expect it to have ln 1,000,000 levels. Based on my answer above, that'd be about 14, yielding 2^14 nodes. As for space, each number could be stored in 14 bytes, which would be 14 MB for a million numbers.**

How Fast?

*   _My copy of Meyer’s Object Oriented Software Construction..._ **I'm going to guess about 120,000 words. Let's say the average word in a technical text is 5 characters long, so that's 600,000 letters. With formatting, I'd budget 900kb for plain text. This jives with my recollections of Project Gutenburg novels.**
*   _My binary search algorithm..._ **It should go exponentially, so a hundredfold increase in entries caused a 1.5ms increase. The next one is another hundredfold, so that would be 1.5ms x 1.5 ms, or 2.25mS. So, I say 7.75ms.**
*   _Unix passwords are stored using a one-way hash function..._ **Well, that would be 96! / (96 - 16)!, which is 96 * 95 * ... * 80, or about 88^16, or about 7700^8, or about 670000^4, or about 44x10^8 ^2, or about 176x10^16 ms. There's 1.5x10^9 seconds per year, so it would take millions of years to crack the algorithm. My answer is no. :)**

See also my previous Kata posts: [Kata 1]({% post_url 2008-01-26-code-kata-1-my-solution %}), [Kata 2]({% post_url 2008-01-31-kata-2-my-solution %})
