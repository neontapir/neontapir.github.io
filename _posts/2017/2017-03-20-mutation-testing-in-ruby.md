---
layout: post
title: Mutation Testing in Ruby
date: 2017-02-10 15:30:00
description: How to perform mutation testing in Ruby
categories:
- professional
tags:
- testing
- mutation
- mutant
- ruby

---

{% include side-image.html image="mutation.jpeg" %}

The value of automated testing is predicated on trust. It begins innocently with
a test suite that reports incorrectly. Maybe the test suite reports a lot of
false positives, or maybe the test suite does catch enough failures. In either
case, people stop running the tests. They stop maintaining the tests, and
eventually the tests no longer function and are discarded.

For tests to remain relevant, this pervasive question runs throughout software
testing: how can I trust that a unit test is actually exercising the code in
question? This post talks about how mutation testing can provide a definitive
answer.

<!--more-->

In my days as a developer, I relied on code inspection to answer this question.
I would go through the red-green-refactor loop as I developed: writing a failing
test,  modifying my code, re-running the test, and ensuring it passes. I would
visually inspect my code, looking for code paths that were not under test. And
so on.

Despite my best efforts, sometimes we would discover bugs. A method would have
an unindented side effect. Some framework method would have a surprising outcome
in edge cases. Or, I would make a mistake in a complicated Boolean statement
that only occurred seldomly. These failures by my unit tests to uncover bugs
would shake my faith in their veracity.

{% include pullquote.html text="The value of automated testing is predicated on
trust" %}

I don't write code for a living any more, but I still code. A program I use
everyday is a set of Ruby scripts that help me log my management notes about my
direct reports. These scripts provide a template to input data, then append it
to a log file.

Last week, I discovered that Ruby has a mutation tester, and it helped me
discover a bug in my code. Here's a portion of my `Team` class:

```ruby
class Team
  def initialize(**params)
      @team = params[:team].capitalize
  end

  def members_by_folder
      Dir.glob("#{EmployeeFolder.root}/#{team}/*")
  end
end
```

And I expected the following to hold true:

```ruby
@avengers = Team.new('Avengers')
# ... some additional setup
expect(@avengers.members_by_folder).to contain_exactly(
        'data/avengers/hank-mccoy',
        'data/avengers/hank-pym' # , ...
      )
```

This script has been functioning this way for months. My tests hard-coded the
member folders to isolate the Team tests from the Employee tests, so they didn't
uncover this issue either.

With just these few lines, it's not hard to see the issue. Instead of a
lowercase folder name, what was actually happening was:

```ruby
@avengers = Team.new('Avengers')
# ... some additional setup
expect(@avengers.members_by_folder).to contain_exactly(
        'data/Avengers/hank-mccoy',
        'data/Avengers/hank-pym' # , ...
      )
```

I discovered this bug during my mutation testing. The idea behind mutation
testing is that if source code changes are made, tests should fail. If a mutant
method returns the same results as the original, there's a good chance that the
behavior of the method isn't being testing as thoroughly as it should. To do
this, I used Mutant, which is a Ruby library, which automates the mutation
testing process. Mutant achieves this through source code manipulation.

I must say, it did take a number of attempts to hit upon the right combination
of libraries.

```ruby
gem 'rspec', '~> 3.5', require: false, group: :test
gem 'simplecov', '~> 0.14', require: false, group: :test
gem 'mutant-rspec', '0.8.11', require: false, group: :test
```

Enough preamble, here's the result of running Mutant.

```bash
$ bundle exec mutant --use rspec -I lib/ -r team Team

# ... bunch of results ...

-----------------------
Mutant configuration:
Matcher:         #<Mutant::Matcher::Config match_expressions: [Team]>
Integration:     Mutant::Integration::Rspec
Jobs:            8
Includes:        ["lib/"]
Requires:        ["team"]
Subjects:        10
Mutations:       317
Results:         317
Kills:           295
Alive:           22
Runtime:         5.30s
Killtime:        26.00s
Overhead:        -79.62%
Mutations/s:     59.82
Coverage:        93.06%
```

In this case, Mutant made 317 modifications to my Team class source code. In
each case, it ran my RSpec tests against that mutation, looking for situations
where all the tests still pass.

Subjects refers to the number of methods being mutated. A mutation is 'killed'
if the tests report a failure, and 'alive' if it does not. As you can see, in 22
cases, the changes Mutant made are not caught by my tests.

Mutant also looks at the number of source code lines that survived mutation, and
reports that as the coverage percentage. In other words, my tests caught
modifications to 93% of the source code lines.

Here's an example of a problem report:

```diff
evil:Team#eql?:/Users/i848350/git/github/neontapir/managertools-logging/lib/team.rb:59:e1a55
@@ -1,6 +1,6 @@
 def eql?(other)
   if other.respond_to?(:team)
-    team == other.team
+    team
   end
 end
```

It turns out that if you replace the equality comparison, my tests still pass! I
looked at my test suite, and indeed, I wasn't testing the `eql?` operator at
all.

In more complicated situations where it isn't obvious from code inspection what
the issue is, manually make the code substitution that Mutant made and re-run
the tests. When you do so, you'll see the error Mutant found, and then you can
track it down using the normal troubleshooting process.

The issue became obvious when I tried to use my script with a multi-word team
name:

```ruby
@justice_league = Team.new('Justice League')
```

That space uncovered a number of subtle bugs, which I squashed by changed spaces
to dashes.

```ruby
expect(@justice_league.members_by_folder).to contain_exactly(
        'data/justice-league/bruce-wayne',
        'data/justice-league/clark-kent'
      )
```

I also found cases where Mutant replaced my "to_s" implementation with something
that gave the same result. In those cases, I simply tested that the two methods
returned the same value. Here's an example from the current code base:

```ruby
def self.to_name(input)
  input = input.tr('-',' ') if input.include? '-'
  input.titlecase
end

def to_s
  Team.to_name(self.team)
end
```

Mutation testing can be a powerful technique for exposing assumptions in your
code base and your unit tests. While I did not address every issue it reported,
I found it to be extremely useful!
