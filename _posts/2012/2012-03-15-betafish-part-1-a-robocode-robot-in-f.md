---
layout: post
comments: true
title: BetaFish Part 1 - a Robocode robot in F#
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
  email: neontapir@gmail.com
  display_name: Chuck
  first_name: Chuck
  last_name: Durfee
---
The group here at work chose to compete via Robocode for our next code kata, and this post is the first in a series that describes how I wrote an F# robot for that challenge.

[Robocode](http://robocode.sourceforge.net/) is a programming game in which a platform is provided, including an abstract Robot battle tank class, and competitors write concrete implementations. Those robots compete in real-time on-screen. The battle simulator has decent graphics, and the platform exposes a few dozen events that robots can subscribe to in their quest to be the last robot standing. For example, when the robot sees an opponent or hits a wall, an event is fired.

Robocode itself is written in Java, but there is a library called JNI (Java-.NET interface) that allows .NET robots to take part in the fun. Since I'm learning F#, it seemed like the language to choose.

First, I visited the site and downloaded the Java platform. I then followed the instructions for [creating a .NET robot](http://robowiki.net/wiki/Robocode/.NET/Create_a_.NET_robot_with_Visual_Studio), which including installing JNI and some helper libraries. The instructions were written for C#, and being F#, there were some subtle nuances that I missed which cost me a couple of hours:

I followed the Visual Studio debug setup instructions included, but found that if I set a breakpoint prior to hitting F5, I got a fatal exception loading the JNI jar file. A colleague wasn't having this problem, and we figured out he wasn't setting breakpoints right away. Now, I use this workflow:

*   Disable my breakpoints
*   Hit F5 and let the Robocode battle simulator load
*   Enable my breakpoints
*   Start the battle

I found [a post on Zamboch's blog](http://zamboch.blogspot.com/2010/07/clr-40-for-robocode.html) showing a very basic F# robot. It was enough to get me over the hump. Here's the first version of the robot:

{% highlight fsharp %}  
 namespace Neontapir  
 open Robocode  
 open System

type BetaFish() =  
 inherit Robot()

let random = Random(DateTime.Now.Millisecond)  
 let mutable firepower = 1.0 // TODO: handle this immutably instead?

let randomTurn (robot:Robot) amount =  
 let direction = random.Next 2  
 match direction with  
 | 1 -&gt; robot.TurnLeft amount  
 | 0 -&gt; robot.TurnRight amount  
 | _ -&gt; failwith "Unexpected direction value"

override robot.Run() =  
 while true do  
 robot.TurnRight 40.0  
 robot.Ahead 20.0

override robot.OnScannedRobot(event : ScannedRobotEvent) =  
 robot.Fire firepower  
 override robot.OnBulletHit(event) =  
 robot.Ahead 20.0  
 firepower &lt;- 1.0 + firepower

override robot.OnBulletMissed(event) =  
 robot.Back 20.0  
 firepower &lt;- 1.0  
 override robot.OnHitByBullet(event : HitByBulletEvent) =  
 randomTurn robot (90.0 - event.Bearing)  
{% endhighlight %}

You can see, it has a lot of similarity to Zamboch's sample robot. The new piece for me was the `randomTurn` method. This was the first occasion I'd had to use the pattern matching (`match`...`with`) construct.

Pattern matching is a little like regular expressions for code. Instead of writing a switch statement or a series of if/then blocks, I can use pattern matching to conditionally execute code. In the case above, I'm getting a random result between 0 and 1, and using that to decide whether to turn left or right. The F# compiler won't allow me to specify an incomplete pattern, so I use the "match anything" (\_) symbol to complete the pattern. The underscore is analogous to a default case in a switch statement.

You'll notice that I have a mutable variable in this robot, `firepower`. Although F# supports mutables, I wanted to get rid of it. Typically, I'd do this by having a method that returns a new `BetaFish` robot. However, because the Robocode battle simulator expects a single instance of the Robot, this strategy won't work. At my present knowledge level, I'll need at least one mutable variable.  
 This robot isn't very smart. In fact, it can be thwarted by running into a wall. In the next article, I'll add some more basic functionality.
