---
layout: post
comments: true
title: 'Code Kata 1: My Solution'
date: 2008-01-26 05:24:54 -07:00
categories:
- professional
tags:
- approaches
- code exercise
- composite
- decorator
- null object
- pricing
- supermarket

---
{% include side-image.html image='shopping-cart.png' %}

At the CodeKata site, [Code Kata 1](http://web.archive.org/web/20131016084201/http://codekata.pragprog.com/2007/01/code_kata_one_s.html) deals with supermarket pricing. You should go off and ponder it for a spell, then come back.

I used three patterns in my solution: Composite, Decorator, and the Null Object. Composite allows a collection of objects to be treated like one of the objects itself. A LEGO construct is a group of individual LEGOs, but as far as attaching another LEGO, the construct can be thought of as being a single, giant, complex LEGO.

The Decorator pattern embellishes the behavior of an object. Wrapping paper can decorate a box and turn it into a gift. A silicone mit can decorate a hand and keep it from getting burned when grabbing a hot pizza pan out of the oven.

The Null Object pattern establishes a definition for a "null" or empty object. It allows us to gracefully handle situations where there’s no special behavior needed.

A parenthetical comment. I used ducats (Ð) as a currency, because it was a historical currency and I wanted to be free to think of alternate currency approaches. The Ð is a capital eth from Icelandic. (Thanks to Old Jack's Guild of Rogues for inspiration.)

I see three key abstractions here: an Item, an ItemGroup (itself a Composite of items), and a PricingRule. Items have a _cost_, the amount needed to buy the item, and a _price_, the amount needed to sell the item. Each key abstraction will become a class.

The simple price is easy. For this scenario, we can use the Null Object StandardPricingRule, which says that the SalesPrice of an Item is simply equal to its Price. The customer gives me Item.Price ducats, and I give them the item. We’re both happy.

The next challenge is three oranges for a ducat. What happens if I need four oranges for a recipe? How much is the fourth orange? I’ll handle this with fractional money. Each orange is 1/3 of a ducat, as given by a PricingRule. Because some transactions are handled with physical coins, rounding is allowed, to the nearest cent. It’s up to the grocer to structure their pricing so they don’t lose money.

Next, we have bananas at Ð1.99 a pound. It’s clear that some items need to be weighed to be sold, so I’m going to introduce a new class, the WeightedItem, which is an Item that has Weight and Unit properties. Furthermore, WeightedItems will know how to price themselves by unit according to weight.

The last one, buy two melons, get one free, will require the use of the PricingRule. A customer’s shopping cart is a big ItemGroup. The PricingRule will get applied to the shopping cart, thereby affecting all the melons in the cart. Every third melon will have it’s price set to 0\. If we’re allowing prices to change, it will therefore become important to know the _SalesPrice_ of an Item, how much it actually sold for. So, I should have said, the price remains the same, but the SalesPrice is set to 0.

The kata comes with some questions, some of which we’ve already answered. As it turned out, there’s nothing special about ducats. Any modern currency (dollars, euros, RMB) will work as well as a ducat, as long as it supports fractional money and allows rounding. (At least that I know of.) (It might be an interesting exercise to come up with an alternate system that didn’t rely on fractional money.)

An audit trail of pricing decisions could be handled by writing to a log whenever a PricingRule is applied. (With the StandardPricingRule, we can require a PricingRule to always be applied.) Are costs and prices the same class of thing? — yes, since I have no need to make them be different.

The last question, about pricing a shelf of cans, is interesting, though. If a shelf of 100 cans is priced using a "buy 2, get 1 free" PricingRule, what’s the value of the shelf? We can apply the PricingRule to the **cost** of each Item on the shelf (which is an ItemGroup, of course). That will yield the value of the shelf.

Readers, let me know what you think of my solution. And Dave, thanks for posting this and other katas to your [blog](http://codekata.com/)!
