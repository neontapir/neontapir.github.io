---
layout: post
comments: true
title: BetaFish Part 3 - Scaredy Cat
categories:
- coding
- professional
tags:
- code exercise
- f-sharp
- F#
- robocode

---
This is article 3 in a series of posts in which I introduced the idea of building an F# robot for Robocode. The last installment showed an improved version of the robot that didn't bump into walls, but did quake at the sight of an enemy.

The twitching behavior I described in the last post is a result of receiving a number of events each turn. When the robot is hit, it tries to evade. However, when it sights an opponent, it turns to attack. Evade, attack, evade, attack... the robot gets stuck in a loop as long as the opponent is facing it and continues to fire. Poor BetaFish. Let's see if we can fix that:

{% highlight fsharp %}  
 namespace Neontapir  
 open Robocode  
 open System

type ActionType =  
 | EndGame  
 | Search  
 | Evade of float  
 | Attack of float  
 | AvoidWall

type BetaFish() =  
 inherit Robot()

let random = Random(DateTime.Now.Millisecond)  
 let defaultFirepower = 3.0  
 let moveUnit = 20.0

let randomTurn amount (robot:Robot) =  
 let direction = random.Next 2  
 match direction with  
 | 1 -> robot.TurnLeft amount  
 | 0 -> robot.TurnRight amount  
 | _ -> failwith "Unexpected direction value"

let shouldEvade enemyBearing =  
 match enemyBearing with  
 | bearing when Math.Abs(bearing : float) < 20.0 -> false  
 | _ -> true

let evade (robot:Robot) =  
 robot |> randomTurn 90.0  
 robot.Ahead moveUnit

let mutable lastEvent : ActionType = Search

override robot.Run() =  
 try  
 while true do  
 match lastEvent with  
 | EndGame -> ()  
 | AvoidWall ->  
 robot.Back moveUnit  
 robot |> randomTurn 30.0  
 lastEvent <- Search  
 | Evade attackerBearing ->  
 match attackerBearing with  
 | bearing when not(shouldEvade bearing) ->  
 lastEvent <- Attack defaultFirepower  
 | _ ->  
 robot |> evade  
 lastEvent <- Search  
 | Attack firepower ->  
 robot.Fire firepower  
 | Search  
 | _ ->  
 robot.Ahead moveUnit  
 robot.TurnRight 40.0  
 with _ ->  
 lastEvent <- EndGame

override robot.OnScannedRobot(event) =  
 match lastEvent with  
 | Attack _ -> () // robot.Out.WriteLine "Scanned robot"  
 | _ ->  
 robot.TurnRight event.Bearing  
 lastEvent <- Attack defaultFirepower

override robot.OnBulletHit(event) =  
 let newEvent =  
 match lastEvent with  
 | Attack strength ->  
 Attack (Math.Min(strength + defaultFirepower, Rules.MAX_BULLET_POWER))  
 | _ -> Attack defaultFirepower  
 lastEvent <- newEvent

override robot.OnBulletMissed(event) =  
 lastEvent <- Search  
 override robot.OnHitByBullet(event) =  
 if (event.Bearing |> shouldEvade) then lastEvent <- Evade(event.Bearing)  
 override robot.OnHitWall(event) =  
 lastEvent <- AvoidWall  
 override robot.OnDeath(event) =  
 lastEvent <- EndGame  
 override robot.OnBattleEnded(event) =  
 lastEvent <- EndGame  
{% endhighlight %}

There are a few minor changes worth mentioning here:

*   I renamed the `DoNothing` `ActionType` to `EndGame`for readability
*   I've encapsulated the `defaultFirepower` and `moveUnit`values for reuse
*   I'm doing more sophisticated pattern matching, like the nested match in `Run`'s `lastEvent` matching for the `Evade`type.
*   I dropped the type specifications on the handlers for Robocode events, since F#'s type inference engine can infer them

To solve the twitching issue, I created a `shouldEvade` method that decides whether to try to evade fire. This version will stand and take it if it's facing an enemy. I found it odd that I had to specify that `bearing` was a `float` type, until I realized that `Math.Abs` has a number of overloads.

I changed the signature of `randomTurn` so I could use the piplining operator (`|>`). This operator allowed to me write `robot |> randomTurn 30.0`, which reads more natually to me than `randomTurn robot 30.0`. With pipelining, I'm able to say "with robot, do a random turn". My code less like Yoda sounds, pipeline it makes.

I wrapped the code in `Run` to solve another nagging issue. In previous versions, when the battle was over, BetaFish would often throw an exception or the battle simulator would have to terminate it. The `try ... with _ -> lastEvent <- EndGame` facility allowed me to catch the `DeathException` I often receive at the end of battle.

This BetaFish version, the one I'm submitting to the code kata, does far better than its predecessors. It almost beats the Fire sample robot. Fire often wins because it turns its gun and its body separately. If we get another go-round, I will try this strategy. I took a quick stab at it, but the first attempt did very poorly.

It still has problems, don't get me wrong. It runs like a scaredy cat if it gets fired upon a lot. It's performs poorly because it moves the whole tank body instead of just the gun or the radar. And it is easily defeated by the C# sample robot, that runs fast along the border and fires towards the middle. BetaFish can't get a lock on it fast enough.

Beyond the robot, there are certainly more F# features to explore. For example, I'm halfway through reading "Real World Functional Programming" by Petricek and Skeet, and a future chapter teases at a better way to handle event registration and waiting on events to fire. I can't wait!

I hope this article series has been of interest. Drop me a line if you found it interesting and would like to see more.
