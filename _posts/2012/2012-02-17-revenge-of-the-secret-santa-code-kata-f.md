---
layout: post
comments: true
title: Revenge of the Secret Santa Code Kata - F#
categories:
- coding
- professional
tags:
- code exercise
- f-sharp
- F#

---
Here’s another solution to the [Secret Santa code kata](http://rubyquiz.com/quiz2.html), this time a scouting mission into functional programming with F#.

To recap:

*   My [first solution]({% post_url 2012-01-25-secret-santa-code-kata-in-powershell %}), written in PowerShell, relied on selecting random pairs of people and using a “hill-climbing” algorithm to avoid getting stuck.
*   My [second solution]({% post_url 2012-02-10-secret-santa-code-kata-redux-in-c %}) I constrained to be deterministic — no randomness.

This one was more about trying to write something meaningful in F# using a problem I’m by now familiar with. Take a look at the code:

{% highlight fsharp %}
 open System  
 open System.IO

// TODO: what's the accepted way to configure an F# program at runtime, App.config?  
 let lines = File.ReadAllLines(@"names_santa.txt") |> List.ofArray

let surname (x : string) = (x.Split ' ').[1]

// TODO: how do I make this generic enough to use in both cases below?  
 let lastItem (a : string[]) = a.[a.Length - 1]

let randomizer = new Random(DateTime.Now.Millisecond)

let swap (a: _[]) x y =  
 let tmp = a.[x]  
 a.[x] <- a.[y]  
 a.[y] <- tmp

// shuffle an array (in-place), borrowed from a code snippet site  
let shuffle a =  
 let len = Array.length a  
 Array.iteri (fun i _ -> swap a i (randomizer.Next(i, len))) a

let linesArray = Array.ofList lines

// TODO: this "do-while" loop, I should be able to rewrite it as a recursive function, but how?  
shuffle linesArray  
 while surname linesArray.[0] = surname linesArray.[(Array.length linesArray) - 1] do shuffle linesArray

let rec pairings = linesArray  
 |>  Seq.windowed 2  
 |>  Seq.choose (fun (x:string[]) ->
 match x with  
 | x when surname x.[0] < >surname x.[1] -> Some(x)  
 | _ -> None  
 )

let pairingsList = List.ofSeq pairings

List.append pairingsList [[|pairingsList.[pairingsList.Length - 1].[1]; pairingsList.[0].[0]|]] |>
 Seq.iter (fun (x:string[]) -> printfn "%s gives a gift to %s" x.[0] x.[1])

Console.WriteLine "Done, press Enter to exit"  
 Console.ReadLine() |> ignore  
{% endhighlight %}

As you can see, I left myself a few to-do items. I boxed the effort at three hours, which is why I went ahead and borrowed the shuffle logic from the internet.

The first hour was learning to speak F# again, especially the method signatures. I played with F# when it was in beta, so I didn’t go into the kata stone cold. However, it took me a while to troubleshoot why my methods didn’t have the signature I expected.

I spent the most time writing the `pairings` function. Once I had the insight of using the match operator, the algorithm came together very quickly. I decided that I wasn’t happy with it being deterministic. I found that if I provided a file that was already in an appropriate order, `pairings` regurgitated the list. Dissatisfied, I went about trying to shuffle the array. Not being familiar with unit testing in F#, I used the F# Interactive console. I got frustrated with trying to implement the shuffle algorithm, so I decided to study a working copy.

The hard part came in integrating it with my code. I resorted to using a while loop, which I know from reading about functional programs means that I’m not thinking of the problem through. I believe I couldn’t convert this into a recursive function because `shuffle` returns a `unit` (that is, it does the work inline). If it returned an array, I bet I’ve have more luck. I’ll have to experiment further.

My attempts to rewrite the loop badly broke the program. I used comments as poor man’s source control, and I got lucky. I really should have check in the first working version into my local Subversion repository.

Some time passed. I managed to look at the do-while problem again, and after about 90 minutes, I solved both it and another issue that bugged me.

Here’s the second revision:  
{% highlight fsharp %}  
open System  
open System.IO

let randomizer = new Random(DateTime.Now.Millisecond)

let surname (x : string) = (x.Split ' ').[1]  
 let lastItem (a : 'a list) = a.[a.Length - 1]

let shuffle items =  
 let upperBound = (List.length items) * 100  
 let randomlyWeightedItems = List.map (fun item -> item, randomizer.Next(0, upperBound)) items  
 let sortedByWeight = List.sortWith (fun (_, leftWeight) (_, rightWeight) -> leftWeight - rightWeight) randomlyWeightedItems  
 List.map (fun (item, _) -> item) sortedByWeight

let shuffleUntilEndsDiffer theList =  
 let rec loop a =  
 let shuffled = shuffle a  
 if surname shuffled.Head = surname (lastItem shuffled) then  
 loop shuffled  
 loop theList

// Main part of the program, need to find out how to separate code into files

let lines = List.ofArray (File.ReadAllLines(@"names_santa.txt"))

shuffleUntilEndsDiffer lines

let rec pairings = lines  
 |> Seq.windowed 2  
 |> Seq.choose (fun (x:string[]) ->
 match x with  
 | x when surname x.[0] <> surname x.[1] ->  Some(x)  
 | _ ->  None  
 )  
 |> List.ofSeq

let veryFirstPerson = pairings.Head.[0]  
 let veryLastPerson = (lastItem pairings).[1]

List.append pairings [[|veryLastPerson; veryFirstPerson|]]  
 |> Seq.iter (fun (x:string[]) -> printfn "%s gives to %s" x.[0] x.[1])

Console.ReadLine()  
 |> ignore  
{% endhighlight %}

The do-while loop was solved by making the shuffling function return the shuffled contents instead of unit (void in C# parlance).

The second change was to get away from arrays. Arrays in F# are mutable, and I wanted to only use immutable data structures as much as possible.

The shuffler was the main barrier. Once I hit upon the idea to associate each person with external data, in this case a random weighting, the rest fell into place. You may also notice some language usage improvements, such as using `a.Head` instead of `a.[0]`

Questions? Comments?
