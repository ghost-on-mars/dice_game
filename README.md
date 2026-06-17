## ICS4UdiceGameObjectsFinal
- Each player rolls 2 dice, and earns or loses points depending on the sum. There are 3 types of players: type 1 players win points if the sum of the dice is 6, 7, 8 or 9, type 2 players win points
 if the sum of the dice is 2, 3, 4, 5, 9, 10, 11 or 12, and type 3 players will win points if the sum of the dice is 2, 3, 4, 5, 6, 7 or 8. 
- There is a 30% chance to be type 1, 60% chance to be type 2, and 10% chance to be type 3.
- If the player wins, they earn the amount of points they rolled, and if they don't win, then they lose the amount of points showing on their dice roll.

## dicepart2probability 
This tests the probability of each type of player winning over a certain number of rounds, and creates a graph of the most common sums rolled, as well as each player type's number of wins with matplotlib. This showed that player 3 was most likely to win
## diceprobability3
This tests the probability slightly differently, as it lets you input how many rounds per game you want to play, as well as how many games in total. Doing this makes you able to see that even though player type 
2 wins close to as often as player 1, they get far less points since 6, 7, and 8 are some of the most common sums, and player type 2 gets those subtracted. So the more rounds per game, the less likely 
they are to win that game. (for example, when testing with 1000 rounds per game and 100 games, player 2 didn't win a single game, despite getting roughly equal as many wins as player 1 in each individual game)
