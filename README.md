# Monopoly simulation

## Purpose

This is to document the process and results of the distribution of where a player lands on a Monopoy board.

## Approach

A Monte Carlo based approach was used to create distributions and probabilities of a player landing on each square of a UK Monopoly board. This involved simulating a person moving around a board over many games and tracking the number of times a player lands on each space.

The spaces a person lands on is influenced by:

* Using two dice - Moving 7 spaces each go is more likely then moving 2 or 12 spaces.
* In-game cards - Community Chest and Chance cards serve to disrupt the normal movement of the game by moving players to specified locations
* Rules - E.g. Going to jail after rolling 3 consecutive doubles

## Assumed Rules

* After rolling 3 consecutive doubles, a player moves directly to jail after the third roll without moving first.
* Once in Jail, a player must roll a double to leave. If a double is not attained on the third roll, the player is then moved to 'Visiting Jail' and the go ends.
* If a player has a 'Get out of jail free' card at their disposal at the time of going to Jail. Then this is used in place of rolling and the go ends.
* If a player lands on a community chest or Chance location and is further directed elsewhere, both spaces are counted, but does not add to the go count. Therefore the total number of spaces visited may be larger than the number of goes.

## Considerations: 

For this project I am considering the spaces 'In Jail' and 'Visiting Jail' as a single space and have combined the number of times on this space together.

Cannot simulate human choices. A person's decision to use a Get out of Jail card may depend on the stage of the game

In the end I limited the scope of the project to calculate probabilities: Without accounting for additional players / Money / Individual decisions 

Each square on the board was assigned a number, starting with 'Go' which was assigned 0. The player starts here at the beginning of each game.



## Notes:

The probabilites are dependant on the game version and the subsequent rules that are applied. This version follows the UK edition, which has 16 Community Chest cards compard to the 17 of the Original.

The space counted for the probabilities is the one the player finishes their go on. For example, if a Player lands on positon 7 (Chance) and is then instructed to move to postion 0 (Go), then it is the final position (0) that is counted and not the Chance space.
This will affect the final probabilities. 

