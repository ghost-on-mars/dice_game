#finished April 17, 2026
import random

class dice:
    #constructer
    def __init__(self, d1, d2): #this is unnecessary
        self.d1=d1
        self.d2=d2

    def rolldice(self): #rolls the dice and returns the sum
        dice1 =(random.randint(1, 6))
        dice2 =(random.randint(1, 6))
        return dice1+dice2

class player:
    #constructer
    def __init__(self, types):
        self.types=types #i think this ended up being unnecessary since it uses ptype and not types from itself

    def taketurn(self, playernum,ptype): #rolls the dice and returns the outcome
        sum=dice.rolldice(self)
        withcolon=str(ptype)+':'
        print( 'numbers needed to win for type', withcolon,  *dicesums[ptype-1], '. sum of the dice:',sum, )
        if sum in dicesums[ptype-1]: #if the sum is one of the numberes the player can win from
            playerpoints[playernum]+=sum
            return '\nwin \ntotal points:'+str(playerpoints[playernum])
        else:
            playerpoints[playernum]-=sum
            return '\nlose \ntotal points:'+str(playerpoints[playernum])

    def display(self, playernum, rounds, ptype): 
        turnoutcome=self.taketurn(playernum, ptype) #
        print('player', (playernum+1), '\nplayer type:', ptype, '\nrolls made:', rounds, turnoutcome,'\n')
        print("all player's points:", *playerpoints, '\n')

playerpoints=[]
types=[]
dicesums=[[6,7,8,9], [2,3,4,5,9,10,11,12], [2,3,4,5,6,7,8]]
print('Type 1 Players will win points if the sum of the dice is 6, 7, 8 or 9\nType 2 Players will ' \
'win points if the sum of the dice is 2, 3, 4, 5, 9, 10, 11 or 12\nType 3 Players will win points ' \
'if the sum of the dice is 2, 3, 4, 5, 6, 7 or 8\nThere is a 30% chance to be type 1, 60% chance to ' \
'be type 2, and 10% chance to be type 3\nIf the player doesn’t win, then they lose the ' \
'amount of points showing on their dice roll')
rounds=int(input('\nHow many rounds do you want to play? '))
playernum=0 #starts at 0
howmany=int(input('How many players are there? '))
roundcounter=0

types = random.choices((1, 2, 3), weights=(30, 60, 10), k=howmany) #generates a list of random types for teh numebr of players

for i in range(rounds): #repeats for the number of rounds
    roundcounter+=1
    playernum=0
    for i in range(howmany):
        if roundcounter==1: #only does it for the first round so it doesnt keep adding 0s
            playerpoints.append(0) 
        #print(types, 'types', types[playernum])
        p1=player(types)
        p1.display(playernum, roundcounter, (types[playernum]))
        playernum+=1 #updates the player number so the next player can take their turn

print('The winner is player', (playerpoints.index(max(playerpoints)))+1, 'with a total of', max(playerpoints), 'points')