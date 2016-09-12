---
layout: post
title: "Video Post-Processing Using FFmpeg and SoX"
date: 2016-05-17 09:00:00
categories:
- personal
tags:
- board-game
---

{% include side-image.html image="audio_processing.jpg" %}

I like board games. Specifically, designer board games. Mass market games are
designed to appeal to general audiences. If you target a more narrow audience,
though, you can tailor the game to suit. I don't dislike **Monopoly**. However, if I
am going to play an area control and resource management game, there are other
games that I'd prefer.

Let me give an example. Area control is an example of a game mechanic. Perhaps
the simplest example of an area control game is **Tic-Tac-Toe**. The game board
consists of 9 squares, arranged in a 3x3 grid. Players take turns claiming
control of squares, until the victory condition is met or all squares are taken.
Tic-Tac-Toe is simple enough that it's routinely taught to young children.

Resource management is the key mechanic in Monopoly. A player wins by forcing
all other players to lose all their money, so players must weigh the risk and
rewards of buying properties. However, Monopoly also uses area control. Players
pay "rent" to other players whenever they land on a space that other player
controls. The two mechanics are connected, because Monopoly rewards players with
higher rents for collecting all properties of the same type: color, railroad, or
utility. The game is designed so that earning money is harder than losing money.

Most people would prefer to play Monopoly over Tic-Tac-Toe. Even so, the game
has a few drawbacks: random movement and player elimination. Unfortunate dice
rolls can prolong a game -- in fact, Monopoly can take a notoriously long time
to play! One reason is that a property cannot be purchased before a player lands
on it. In some games, this means that a property can go many turns before
becoming available, thus preventing some players from being able to execute
their collection strategy through no fault of their own. During the middle and
later parts of the game, an unlucky player can get a disproportionate amount of
money taken from them -- again, through no fault of their own. (This luck aspect
is magnified by two decks of event cards.) Monopoly also features player
elimination, by which I mean that the game can end for a player while others
continue to play. This can be rob the game of fun for a player whose eliminated
early.

Now let me describe a designer board game I enjoy that features the same area
control and resource management game mechanics. In **Power Grid**, players are
power plant owners vying for the ability to power cities on a map. The winner is
the player that can power the most cities. The end of the game is triggered by
the player who gain control of a certain number of cities, depending on the
number of players. (These are often, but not always, the same player.) Each
turn, players can buy new power plants, buy fuel, expand their territory, and
earn money by burning fuel to power cities.

To succeed at Power Grid, players must manage three kinds of resources: money,
power plants, and fuel. Money is earned in this game by powering cities, which
is where area control comes in. To expand, players have to pay for a place in
the city and a connection cost between cities. In the beginning of the game,
cities can only be powered by one player, so players compete for places with low
connection costs.

Players start the game by buying power plants at an auction, similar to the
mechanic that Monopoly uses when the active player lands on a space and declines
to buy it. Each turn, players can buy a new power plants. The most costly plants
are more efficient, and can power more cities with less fuel. This game also
features a market with four kinds of fuel: coal, oil, trash, and uranium.
Successful players find ways to power their cities with the least expenditure
for fuel, often by picking a fuel that isn't being utilized as much by the other
players.

What separates Power Grid from Monopoly are built in checks and balances that
prevent the issues I mentioned above. Except for picking the starting turn
order, there's no randomness in Power Grid. Turn order changes based on the
number of cities you control. Players with more cities can earn more money and
get to pick power plants before players with fewer cities, but play goes in
reverse order when buying resources and expanding. This gives players who are
behind an opportunity to catch up. Another mechanism that helps is that in the
middle phase of the game, two players can claim a city.

A drawback of Power Grid is that a player's choice of starting
location can have a large impact on the middle game.
