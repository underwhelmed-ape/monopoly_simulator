# Monopoly simulation

## Purpose

This is to document the process and results of the distribution of where a player lands on a Monopoly board.

## Approach

A Monte Carlo based approach was used to estimate the probability of a player landing on each square of a UK Monopoly board during a game. This involved simulating a player moving around a board 100 times over 10,000 games and taking the mean number of times a player lands on each space.

The spaces a person lands on is influenced by:

* Using two dice - Moving 7 spaces each go is more likely then moving 2 or 12 spaces.
* In-game cards - Community Chest and Chance cards serve to disrupt the normal movement of the game by moving players to specified locations
* Rules - E.g. Going to jail after rolling 3 consecutive doubles

## Assumed Rules

* After rolling 3 consecutive doubles, a player moves directly to jail after the third roll without moving first.
* Once in Jail, a player must roll a double to leave. If a double is not attained on the third roll, the player is then moved to 'Visiting Jail' and the go ends.
* If a player has a 'Get out of jail free' card at their disposal at the time of going to Jail. Then this is used in place of rolling and the go ends.
* If a player lands on a community chest or Chance location and is further directed elsewhere, only the final space is counted. This may affect probabilities.

## Considerations: 

For this project I am considering the spaces 'In Jail' and 'Visiting Jail' as a single space and have combined the number of times on this space together.

Cannot simulate human choices. A person's decision to use a Get out of Jail card may depend on the stage of the game

In the end I limited the scope of the project to calculate probabilities: Without accounting for additional players / Money / Individual decisions 





## Notes:

The probabilites are dependant on the game version and the subsequent rules that are applied. This version follows the UK edition, which has 16 Community Chest cards compard to the 17 of the Original.


