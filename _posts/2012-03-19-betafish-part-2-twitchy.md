---
layout: post
title: BetaFish Part 2 - Twitchy
categories:
- coding
- professional
tags:
- code exercise
- f-sharp
- F#
- robocode
status: publish
type: post
published: true
author:
  login: Chuck
  email: chuck@neontapir.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
Last time, I introduced the idea of building an F# robot for Robocode. The second iteration contains some improvements:

{% highlight fsharp %}
 namespace Neontapir
 open Robocode
 open System

type ActionType =
 | DoNothing // end of game
 | Search
 | Evade of float
 | Attack of float
 | AvoidWall

type BetaFish() =
 inherit Robot()

let random = Random(DateTime.Now.Millisecond)
 let firepower = 1.0

let randomTurn (robot:Robot) amount =
 let direction = random.Next 2
 match direction with
 | 1 -&gt; robot.TurnLeft amount
 | 0 -&gt; robot.TurnRight amount
 | _ -&gt; failwith "Unexpected direction value"

let mutable lastEvent : ActionType = Search

override robot.Run() =
 while true do
 match lastEvent with
 | DoNothing -&gt; ()
 | AvoidWall -&gt;
 robot.Back 20.0
 randomTurn robot 30.0
 lastEvent &lt;- Search
 | Evade(bearing) -&gt;
 randomTurn robot (90.0 - bearing)
 lastEvent &lt;- Search
 | Attack firepower -&gt;
 robot.Fire firepower
 | Search | _ -&gt;
 robot.Ahead 20.0
 robot.TurnRight 40.0

override robot.OnBulletHit(event) =
 let newEvent = match lastEvent with
 | Attack strength -&gt; Attack (strength + 1.0)
 | _ -&gt; Attack 1.0
 lastEvent &lt;- newEvent

override robot.OnScannedRobot(event : ScannedRobotEvent) = lastEvent &lt;- Attack 1.0
 override robot.OnBulletMissed(event) = lastEvent &lt;- Search
 override robot.OnHitByBullet(event : HitByBulletEvent) = lastEvent &lt;- Evade(event.Bearing)
 override robot.OnHitWall(event) = lastEvent &lt;- AvoidWall
 override robot.OnDeath(event) = lastEvent &lt;- DoNothing
 override robot.OnWin(event) = lastEvent &lt;- DoNothing
{% endhighlight %}

You may recall me saying that the first version of this robot could be defeated by a wall. While trying to implement this feature, it became clear that `firepower` didn't represent enough state for the BetaFish robot to care about. There were a number of intermediate versions between last post's code and the above, as I experimented with created a class to encapsulate state.

While trying to use multiple classes, I was stymied for a time by Visual Studio. In an F# project, it wasn't clear to me how to spread my solution over multiple source files. I couldn't reference my other classes. I discovered that in a functional language, it's necessary to order the source files to resolve dependencies, so that items do not depend on other items that are compiled afterward. It turned out that the classes I wanted to use came after the main class in alphabetical order. In Visual Studio, you can reorder source files in an F# project by right-clicking the source file in Source Explorer and moving it up or down.

After a number of iterations, I discarded that secondary class in favor of a **discriminated union**, which I called `ActionType`. Conceptually, a discriminated union is kind of like a generic C# enumeration, but of course much more useful. For example, notice that the `Evade` and `Attack` elements take a `float` argument, whereas the others don't. And pattern matching provides a more robust way to examine the contents of an `ActionType` than C# enumeration's ever would. To accomplish this in C#, you'd need a hierarchy of classes.**

**

The `Run` method has become more sophisticated also, now matching against the `AttackType` instead of just a scalar value. Notice that I'm able to name the union type's argument inline, such as in the case of `Evade`'s `bearing`. This is a feature of pattern matching, not discriminated unions, as you can see with `strength` in the `OnBulletHit` event handler.

**

_NOTE: While this code looks more impressive, it actually stinks in battle. If you try this robot, you'll find that once BetaFish engages the enemy, the robot freezes in battle as soon as it's hit, twitching until it is annihilated. Can you see why? The next article in the series contains the answer._
