#player 2 is about as likely ot win as player 1, but when player 1 loses it loses more points (6, 7, or 8)

import random
import matplotlib.pyplot as plt
class dice:
    #constructer
    def __init__(self, d1,d2):
        self.d1=d1
        self.d2=d2

    def rolldice(self): #rolls the two dice and returns the sum
        dice1 =(random.randint(1, 6))
        dice2 =(random.randint(1, 6))
        return dice1+dice2

class player:
    #constructer
    def __init__(self, types):
        self.types=types

    def taketurn(self, playernum,ptype):
        sum=dice.rolldice(self)
        rolllist[sum-2].append(sum)
        if sum in dicesums[ptype-1]: #if the sum is one of the numberes the player can win from
            playerpoints[playernum]+=sum
            winslist[playernum]+=1
            print('Player type', ptype, 'rolled a', sum, 'and won! list of wins:', winslist) #only prints when someone wins, i didnt add it if they lose
        else:
            playerpoints[playernum]-=sum

    def display(self, playernum): #this is only for the final turns of each player
        print('\nPlayer', (playernum+1))
        print('Points:', playerpoints[playernum])
        print('Wins:', winslist[playernum])

    def plot(self): #plots the 2 graphs
        checkdicerolls=0
        rollsprint=''
        yplot=[]
        xplot=[]
        expectedy=[]
        for i in range(11):
            expectedy.append((rounds*3)*(problist[i]))

            xplot.append(i+2)
            yplot.append(len(rolllist[i]))

            rollsprint+=(str(i+2)+': ' + str(len(rolllist[i])) + '     ')
            checkdicerolls+=len(rolllist[i])
        print('\nPoints of each player:', *playerpoints)
        print('Wins of each player:', *winslist)
        print('\nSums rolled:', rollsprint) # to make it on one line
        print('Times die were rolled:', checkdicerolls) #to check the number of rolls is correct
        plt.subplot(1, 2, 1)
        plt.plot(xplot, expectedy, marker='o') 
        plt.plot(xplot, yplot, marker='o') 
        plt.xlabel('Sum of the die')
        plt.ylabel('Times rolled')
        plt.text(0.5, 0.5, 'Orange: actual sums of dice\nBlue: expected sums of dice',color='black', fontsize=9)
        plt.title('Dice rolls')

        plt.subplot(1, 2, 2)
        plt.bar([1,2,3], winslist, width=0.6) 
        plt.xlabel('Players')
        plt.ylabel('Wins')
        plt.title('Wins per player type')
        plt.show()


problist=[1/36, 2/36, 3/36, 4/36, 5/36, 6/36, 5/36, 4/36, 3/36, 2/36, 1/36] #this is just for plotting the expected probability of the dice sums
rolllist=[[], [], [], [], [], [], [], [], [], [], []]
winslist=[0,0,0]
playerpoints=[0,0,0]
dicesums=[[6,7,8,9], [2,3,4,5,9,10,11,12], [2,3,4,5,6,7,8]] #the sums that each player type requires to win
print('Player 1 will win points if the sum of the dice is 6, 7, 8 or 9\nPlayer 2 will ' \
'win points if the sum of the dice is 2, 3, 4, 5, 9, 10, 11 or 12\nPlayer 3 will win points ' \
'if the sum of the dice is 2, 3, 4, 5, 6, 7 or 8\nIf the player doesn’t win, then they lose the ' \
'amount of points showing on their dice roll')
rounds=int(input('\nHow many rounds do you want to play? (Higher numbers are recommended for a more accurate graph) '))
playernum=0 #starts at 0
roundcounter=0
types = [1, 2, 3] 

for i in range(rounds): 
    roundcounter+=1
    playernum=0
    for i in range(3): #repeats once for each player
        if roundcounter==rounds: #only on the last round
            p1.display(playernum)#, roundcounter, (types[playernum]))
            playernum+=1
        else: #every other round
            p1=player( types)
            p1.taketurn(playernum,(types[playernum]))
            playernum+=1
p1.plot()


