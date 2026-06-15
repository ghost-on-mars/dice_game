#the more rounds in a game, the lower player 2's score is. cause theres more chances for them to roll a 7 8 or 9, which are most common and also subtract a lot of points
#player type 3 is most likely to win

import random
class dice:
    #got rid of the constructor cause it wasnt being used for anything
    def rolldice(self):
        dice1 =(random.randint(1, 6))
        dice2 =(random.randint(1, 6))
        return dice1+dice2

class player:
    #constructer
    def __init__(self, types):
        self.types=types

    def taketurn(self, playernum,ptype): #rolls the dice and updates the points
        sum=dice.rolldice(self)
        if sum in dicesums[ptype-1]: #updates the points and the wins for this game
            playerpoints[playernum]+=sum
            winslist[playernum]+=1
        else:
            playerpoints[playernum]-=sum

totalwins=[0, 0, 0]
dicesums=[[6,7,8,9], [2,3,4,5,9,10,11,12], [2,3,4,5,6,7,8]]
print('Player 1 will win points if the sum of the dice is 6, 7, 8 or 9\nPlayer 2 will ' \
'win points if the sum of the dice is 2, 3, 4, 5, 9, 10, 11 or 12\nPlayer 3 will win points ' \
'if the sum of the dice is 2, 3, 4, 5, 6, 7 or 8\nIf the player doesn’t win, then they lose the ' \
'amount of points showing on their dice roll')
rounds=int(input('\nHow many rounds in each game? '))
totalrounds=int(input('How many total games to play '))
playernum=0
roundcounter=0
totalroundcounter=0
types = [1, 2, 3] 

for i in range(totalrounds): 
    #resets the wins and points at the start of every individual game
    winslist=[0,0,0]
    playerpoints=[0,0,0]
    for i in range(rounds): 
        #each game
        roundcounter+=1
        playernum=0
        for i in range(3):
            p1=player(types)
            p1.taketurn(playernum,(types[playernum]))
            playernum+=1
    #after the game it prints the winner of that game and updates the total wins
    totalroundcounter+=1
    print('game', totalroundcounter, 'wins:', winslist, ', points:', playerpoints, ', the winner of game', totalroundcounter, 'is player', (playerpoints.index(max(playerpoints)))+1)
    totalwins[playerpoints.index(max(playerpoints))]+=1
    print(totalwins, 'total wins per player')
