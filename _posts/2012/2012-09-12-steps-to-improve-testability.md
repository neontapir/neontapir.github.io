---
layout: post
comments: true
title: Steps To Improve Testability
date: 2012-09-12 09:11:36 -06:00
categories:
- coding
- professional
tags:
- design
- testing
---
Last time, I talked about testability and why it's important. Today, I continue the conversation with techniques to improve testability. 

![Steps Forward](/assets/IMG_0130.png)

Though I've used different technologies through my career to achieve these benefits, I use examples from my current team.

### Learn the application and the business

All but one of us is new to the team, so we've had to learn how contract pricing works and how our application implements it. We take every opportunity to talk to support personnel, trainers, product owners and customers to learn more about the domain.

As we do so, we imagine new ways to test the application. We're starting to ask better questions, and that is leading to more meaningful tests.

### Defining a standard test data set

The current automated test suite does not offer adequate scenario coverage. For example, there are manual steps required to set up simulated customer data feeds. The team has been working on a comprehensive gold standard data set that can be used for tests, as well as automated setup and teardown of test data.

The thought is, if the database is in a known state prior to testing, we'll have less test failures due to abberant data conditions. For this application, with the nature of its data and number of existing tests, I feel confident that we'll continue to use this technique. However, there are other ways to inject data into tests, discussed below.

### Write tests for new features and defect fixes

This almost goes without saying. Even though there is a speed cost in doing so, we avoid incurring additional test debt by making sure our new code is tested. These tests conform to our latest thinking around how to test the application.

### Beginning to form a regression test suite

The system uses standard data file formats to import data. Today, we take a scrubbed copy of the production database, look for a customer with a similar data scenario, and writing the tests to use that customer.

This strategy fails as we wish to refresh from production. Sometimes, a customer's business model changes and their data no longer fits the profile a test scenario needs. In other cases, the contracts have been renewed or have expired, so we need to find new data scenarios and retrofit the tests to use the new data.

To lessen our dependence on external data imports for current records, the team has invested in tools to assist in the creation of simulated data import files. For example, it will be invaluable to be able to take one customer's data set, tweak it, and then import it as a different customer. Another tool to update the effective dates of some contracts in bulk according to some data scenario rules will similarly prove its worth.

### Using the best testing technologies for the testing scenario

[NUnit](http://nunit.org) may not be the best vehicle for testing data-intensive applications. Rather than use NUnit as a database script automation engine, the team has researched frameworks like [dbUnit](http://www.dbunit.org/), which allow creation of more direct tests in SQL, a more suitable language.

We've also been looking into using [FitNesse](http://fitnesse.org) to automate business logic tests. This will allow QA and Product to help developers improve our automated test coverage through writing test specifications on the Wiki.

### Use a continuous integration solution to automate test execution

We've been expanding the role of [TeamCity](http://www.jetbrains.com/teamcity/) in our development environment. From running just the unit tests, the team has added builds that:

*   deploy database revisions to our shared development environment

*   deploy the application to shared development

*   run code coverage using [dotCover](http://www.jetbrains.com/dotcover/), which is bundled with TeamCity

*   run a code duplication detection tool

*   run the FitNesse test suite periodically

If you haven't looked into the automation capabilities of a continuous integration tool, I suggest you do so.

### Use transactions in unit tests to avoid causing side effects

As mentioned before, a number of our unit tests do not restore the database to its initial state, which creates timing dependencies in our test suite. Database transactions can solve this problem if the tests are batched inside a transaction. If the transaction is not committed, then the changes are never written to the database.

A database testing framework like dbUnit does this automatically. I've done this manually in some cases, though I've found that writing tests by hand that read a value, update a value, then read it again in a single transaction can be tricky.

To avoid failures from bad data conditions, some of our older tests wipe the entire database clean and loading seed data from scratch. While effective, in a suite of a thousand tests, this is time-consuming and often is overkill! Worse, other tests don't concern themselves with data setup at all and just expect the database to be in a certain state by the time they run!

When we encounter errant tests, we've been ensuring that the tests set up their own data and call appropriate clean-up scripts. Work includes getting subsequent tests to do their own data setup instead of relying upon the side effects of previous tests. Although it is slow, at least the tests are independent of each other. We also consider bundling the data setup of tests into feature sets, to reduce the number of times the data in the tables needs to be wiped and reloaded. If we decide to adopy dbUnit, we'll use the list of poorest performing tests as a place to start.

### Use a separate database for unit testing to avoid causing side effects

As you might expect, setting up and tearing down the database would make the user interface almost unusable. Since we also need to do exploratory testing and other groups need to integrate with us, we set up independent database that the unit tests run against.

With multiple databases in multiple environments, change management is a concern. We write database change scripts in SQL, both forward and backward versions. Each database has a table that contains database version information. We have a C# module that knows how to upgrade or downgrade a database given a database and a target version number. For the most part, this strategy works very well.

Having the application itself keep track of the different database contexts is complicated. In some test suites I've seen, a base class is used to provide configuration and test data for a suite of tests. Because C# does not allow multiple inheritance, this design can be a drawback when testing different parts of the application under the same data conditions. Tests for the contract expiration algorithm might appear in multiple test suites, for example.

To combat this, we use [Ninject](http://www.ninject.org/) as an [IoC container](http://martinfowler.com/articles/injection.html) to separate configuration from usage. Inversion of control is a powerful technique that deserves its own article, so I'll delve into this topic later.

### Mock the data access layer to remove the database dependency

For logic that lives in the C# code atop the database, rather than setting up data in the database and performing an integration test all the way down into the database, we can mock the data access components. We're using [Moq](http://code.google.com/p/moq/) as our mocking framework. Mostly through constructor injection, but also through other [Ninject injection patterns](http://ninject.codeplex.com/wikipage?title=Injection%20Patterns), we provide our domain objects with mock data access layers.

A growing fraction of our tests don't need to talk to the database at all. Most of our newly-authored tests follow this doctrine, though adoption has been slow as we do need to be cognizent of the risks of refactoring for testability without tests in place to validate the refactoring itself.

### Move business logic into the domain layer where practical

We have also found several cases where business logic was placed in the database because it was the language previous teams were more comfortable with, not because it was the most natural place for the logic to reside.

This manifests in our code as several lookup queries that get repeated throughout stored procedures. These queries gather data for what should be domain objects. Then, these stored procedures modify the data as methods on an object would do. The insidious part of this design is that the stored procedures modify the data in different ways that often should logically be equivalent, except when there's a business need for variance. As a result, subtle bugs emerge on occasion.

I believe in [Command-Query Separation (CQS)](http://martinfowler.com/bliki/CommandQuerySeparation.html). I think that commands with their complicated decision trees are often better expressed in an object-oriented language like C# or Java than a record-based relational database query language like SQL. Conversely, I think queries and other set-based operations are best expressed in SQL -- this is what database engines are optimized for.

With the advent of [LINQ](http://msdn.microsoft.com/en-us/library/bb397926.aspx), though, I find myself making more use of database views for filtering and transforming data instead of stored procedures. I reserve SQL stored procedures for more advanced situations, especially where performance is a concern.

By consolidating our business algorithms into the domain layer of the application rather than the database, we gain multiple benefits. Separating commands from queries makes the algorithms less complex. We lessen the number of lines of code we support through elimination of duplication. Where variations are necessary, we highlight the differences and the resulting algorithms become clearer. And, through isolation of algorithms into independent objects, we make the algorithms themselves easier to test.

## Conclusion

I've discussed how lack of testability can affect the ability of teams to move their product forward. I discussed some of the challenges faced by the application throughout its life. Then, I used a job experience to illustrate strategies teams can use to get their application under test.

In the past, these strategies have been effective in taming the savage untested beast. For further reading, I recommend [_Working Effectively With Legacy Code_](http://www.amazon.com/Working-Effectively-Legacy-Michael-Feathers/dp/0131177052) or [_Emergent Design: The Evolutionary Nature of Professional Software Development_] by Scott Bain (http://www.amazon.com/Emergent-Design-Evolutionary-Professional-Development/dp/0321509366/).

What strategies have you used? Which were effective?
