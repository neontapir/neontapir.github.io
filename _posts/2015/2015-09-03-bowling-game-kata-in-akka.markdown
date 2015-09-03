---
layout: post
title: "Bowling Game Kata in Akka"
date: "2015-09-03 10:02"
---
Fresh from Typesafe's "Fast Track to Akka in Java", I decided to apply Akka to a
problem I know well, the bowling game kata. <img src="/assets/Akka_toolkit_logo.svg.png" style="float:right" />

Although I'll be using some code snippets to illustrate my journey, the full
solution is [on GitHub](https://github.com/neontapir/code-katas/tree/master/BowlingGame/java-akka).

## Bowling Game kata

For those of you know aren't familiar with it, the kata was created by Uncle Bob
Martin and involves the creation of a class that can score a game of bowling.
While bowling does have a couple of "business rules", if you will, it's pretty
straightforward. A game of bowling requires a ball, some pins and a long, narrow
floor called a lane. The game consists of ten rounds called "frames", and each
frame involves rolling the ball up to two times with the goal of keeping the
ball in the lane and knocking down the ten pins at the end of the lane.

## Akka

Akka is a toolkit for abstracting away asynchronous code so you can think about
your code in a single-threaded, synchronous way. Akka is an actor-based system,
so designs are comprised of a handful of actor types (the "nouns") and a group
of message types (the "verbs"). Interactions between classes are conducted
through messages, which is reinforced by the fact that you can't get to an
instance of an actor. Actors are created in a hierarchy, with a system actor
called a guardian at the root. If you are intrigued as I was, visit
[akka.io](http://akka.io/).

Let's dig in....

<!--more-->

## Application of Akka

I started by asking myself how to incorporate Akka into the bowling game kata.
The problem doesn't lend itself to concurrency, which is where Akka shines as a
toolkit. Part of the fun here is the constraint.

I decided to get going and to figure it out as I went alone. Being an
actor-based system, Akka has a mantra that "everything is an actor".  Embracing
this, I made my `Game` class inherit the `AbstractLoggingActor` class from the
Akka actor package. I immediately ran into issues.

The Java implementation of Akka is not as well used nor documented as its Scala
sibling. I had trouble finding examples of what I was trying to achieve. In
particular, I was stuck for a while getting a test to run with the framework. I
even resorted to asking [Stack
Overflow](http://stackoverflow.com/questions/32120369/uncaught-error-from-default-dispatcher-causes-fatal-error-with-javatestkit).

It turned out in my Maven POM, the Akka testkit package required a different version of
Scala than the Akka actor package. After that hiccup, my test suite started
working as expected. I suddenly understood what the version numbers in the
package names were trying to tell me!

Problems solved, I started the kata by implementing the gutter game use case and
the open frame use cases. These are simple because the final score is simply the
sum of the pins knocked down.

## Including Akka

However, when I started the spare frame case, I realized how I could pull Akka
into the kata. Scoring gets complicated -- by complicated, I mean some pins
count double -- when all the pins are knocked down in a frame. To do that, the
scoring class needs to understand what pins were knocked down in which frame.

The canonical implementation of this kata in Java, the one that Uncle Bob
teaches, illustrates that premature decomposition of problems into objects can
result in extraneous code. However, I realized that if I did create a `Frame`
class, I'd have a second type of actor and a reason for actors to collaborate.

## The design

When an actor wants the `Game` to score a game, it sends the `ScoreGame`
message. This message contains an array with the number of pins knocked down
during each attempt.

In the original algorithm, the scoring method parses such an array into frames
and iterates through the frames. In this Akka implementation, the `Game` handles
it like this:

{% highlight java %}
private void calculateScore(int[] attempts) {
    for (int n = 1; n <= 10; n++) {
        ActorRef frame = getContext().actorOf(Frame.props(attempts, n));
        frame.tell(new ScoreFrame(), self());
    }
}
{% endhighlight %}

In order to describe the work of this method, I need to talk about Akka actors.

## Inside an Akka actor

In contrast to the plain `Game` class in the canonical version, there's some
extra plumbing involved in getting an Akka actor to work. In fact, this extra
code is why many people prefer the Scala implementation.

### Factory method

For an Akka actor, it's recommended that you create a Factory method called
`create()`. For the `Game` class, it looks like this:

{% highlight java %}
public static Props props() {
    return Props.create(new Creator<Game>() {
        private static final long serialVersionUID = 1L;

        @Override
        public Game create() throws Exception {
            return new Game();
        }
    });
}
{% endhighlight %}

In it, we're creating a `Creator<>` class inline that calls the default
constructor. If you need arguments, it looks like:

{% highlight java %}
public static Props props(int[] attempts, int number) {
    return Props.create(new Creator<Frame>() {
        private static final long serialVersionUID = 1L;

        @Override
        public Frame create() throws Exception {
            return new Frame(attempts, number);
        }
    });
}
{% endhighlight %}

### Message handler

The second thing an Akka actor needs to do is to accept messages from other
actors. To do that, we override the `receive()` method. Here is the example from
`Game`:

{% highlight java %}
@Override
public PartialFunction<Object, BoxedUnit> receive() {
    return ReceiveBuilder
            .match(ScoreGame.class, o -> {
                querent = sender();
                calculateScore(o.attempts);
            })
            .match(ScoredFrame.class, o -> {
                frameScores.put(o.frameNumber, o.score);
                // TODO: If we have all of them, send a ScoredGame result
                if (checkReceivedAllFrames()) {
                    querent.tell(new ScoredGame(sumFrames()), self());
                }
            })
            .matchAny(this::unhandled)
            .build();
}
{% endhighlight %}

In Akka, it's typical to create a class for each message type. These classes are
simply plain old Java objects (POJO). However, because they need to be
serialized and there will be multiple instances of them, there's a lot of
plumbing code:

{% highlight java %}
public class ScoredGame {
    public int result;

    public ScoredGame(int result) {
        this.result = result;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        ScoredGame that = (ScoredGame) o;

        return result == that.result;

    }

    @Override
    public int hashCode() {
        return result;
    }

    @Override
    public String toString() {
        return "ScoredGame{" +
                "result=" + result +
                '}';
    }
}
{% endhighlight %}

If you have been thinking, "who needs Scala anyway?", here's an equivalent class in Scala:

{% highlight scala %}
object BowlingGame {
  case class ScoredGame(result: Int)
}
{% endhighlight %}

## Back to the design

To recap, here's how the `Game` class starts to score a game:

{% highlight java %}
private void calculateScore(int[] attempts) {
    for (int n = 1; n <= 10; n++) {
        ActorRef frame = getContext().actorOf(Frame.props(attempts, n));
        frame.tell(new ScoreFrame(), self());
    }
}
{% endhighlight %}

I say 'start' because this is an asynchronous operation. Actors are powerful
because they allow you to subdivide work and conquer tasks in parallel. In this
case,  the `Game` actor is spawning ten child `Frame` actors and telling each
one of them to score their particular frame, which is passed in the frame's
initialization properties.

When a Frame is done with its work, it sends a `ScoreFrame` message back to the
`Game` class. When the `Game` has received all ten `ScoredFrame` responses, it
composes a `ScoredGame` message that it sends back to... wait, the last message
it received should be from a `Frame` child. That's why the `receive()` method
has to save off the original sender into the `querent` field. In our case, the
sender is always a test actor.

## Testing the Actors

There are a couple styles of Akka testing in Java. I kept examples of both in
the `FrameTest` class. These are the two helper methods I use to perform the
testing. Here, `frame` is a field that contains a `TestActorRef<Frame>`
instance.

{% highlight java %}
// sync testing model
private void getFrameFromFrameActor(GetFrame frameSignal, int[] expected) throws Exception {
    new JavaTestKit(system) { {
        Future<Object> future = Patterns.ask(frame, frameSignal, 1000);
        assertTrue(future.isCompleted());

        GotFrame actual = (GotFrame)Await.result(future, Duration.Zero());

        assertArrayEquals(expected, actual.frame);
    } };
}
{% endhighlight %}

In this case, we're sending a `GetFrame` message to the `Frame` class using
`ask()`. In contrast to the `tell()` method introduced earlier, `ask()` deals in
possible futures. This paradigm uses a `Future<>` object that will hold the
result when the operation is complete. By wrapping the result in a `Future`, it
allows the caller to interact with the `Future` the same way whether it's done
or not. This prevents a lot of boilerplate exception-throwing, null-object
handling logic duplicated in each receiver. (If you have done any programming in
JavaScript, think Promises.)

In this test, we set up the `Future` and wait zero time for it to complete. We
can do this because `TestActorRef<>` handles messages in a synchronous way
suitable for testing. While this works, I prefer the asynchronous testing model,
because it more closely resembles the way that actors are used in production
code and it doesn't require understanding `Future`.

{% highlight java %}
// async testing model
private void getScoreFromFrameActor(TestActorRef<Frame> frame, ScoreFrame frameSignal, ScoredFrame expected) throws Exception {
    new JavaTestKit(system) { {
        frame.tell(frameSignal, getRef());
        expectMsgEquals(FiniteDuration.apply(500, TimeUnit.MILLISECONDS), expected);
    } };
}
{% endhighlight %}

Like in the `Game` and `Frame` classes, we're using `tell()` here rather than
`ask()`. `getRef()` gets a reference to the anonymous `JavaTestKit` actor, which
is how the tests interact with its subjects. The Akka toolkit offers a lot of
useful assertions to handle message verification, so there is no need to extract
the values in the messages and compare them directly as we did in the
synchronous case. In this case, the assertion will pass only if the message is
the equivalent of the expected one and is received within 500 milliseconds.
