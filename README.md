# Monopoly game script

Approach:

A Monte Carlo based approach was used to estimate the probablilty of a player landing on each square of a standard Monopoly board.
This involved simulating a person moving around a board over many games and counting the number of times a player lands on each space.

This is influenced by:

* Two dice - Moving 7 spaces each go is more likely then moving 1 or 12 spaces.
* Game cards - Community Chest and Chance cards serve to disrupt the normal movement of the game by moving players to specified locations


Considerations: What constitutes landing on a square? For example, The Jail space consists of two spaces that have different rules to apply. For this simulation I will combine the time spent in either of these cases as one

Cannot simulate human choices. A person's decision to use a Get out of Jail card may depend on the stage of the game

In the end I limited the scope of the project to calculate probabilities: Without accounting for additional players / Money / Individual decisions 

Each square on the board was assigned a number, starting with 'Go' which was assigned 0. The player starts here at the beginning of each game.


