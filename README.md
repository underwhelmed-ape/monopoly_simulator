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



Notes:
The probabilites are dependant on the game version and the subsequent rules that are applied. This version follows the UK edition, which has 16 Community Chest cards compard to the 17 of the Original.

The space counted for the probabilities is the one the player finishes their go on. For example, if a Player lands on positon 7 (Chance) and is then instructed to move to postion 0 (Go), then it is the final position (0) that is counted and not the Chance space.
This will affect the final probabilities. 