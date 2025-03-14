import random


print("Welcome to Going to Town.")
print("The goal of the game is to get the highest score in a set number of rounds. ")
print("You roll three die and take the highest of those. Roll two die, take the highest of those, and roll one more and take that score.")
def roll():
    roll_value = random.randint(1,6)
    return roll_value
#setting players
while True:
    players = input("How many players do you want? Minimum of 2. ")
    if players.isdigit() and int(players)>1:
        players=int(players)
        break
    print("Invalid input. Please re-enter")
#setting rounds
while True:
    rounds = input("How many rounds do you want to play? Minimum of 1. ")
    if rounds.isdigit() and int(rounds) > 0:
        rounds = int(rounds)
        break
    print("Invalid input. Please re-enter")
#scores set to 0
scores=[]
for i in range(players):
    scores.append(0)

#playing the game
for j in range(rounds):
    for i in range(players):
        # three die rolled
        # reset this each time
        dice1 = roll()
        dice2 = roll()
        dice3 = roll()
        max_roll = max(dice1, dice2, dice3)
        scores[i] += max_roll
        print("Player " + str([i + 1]) + " rolled a " + str(dice1) + ", a " + str(dice2) + ",and a " + str(
                dice3) + "!")
        # two die rolled
        dice1 = roll()
        dice2 = roll()
        max_roll = max(dice1, dice2)
        print("Player " + str([i + 1]) + " rolled a " + str(dice1) + " and a " + str(dice2) + "!")
        scores[i] += max_roll
        #1 dice rolled
        dice1 = roll()
        print("Player " + str([i + 1]) + " rolled a " + str(dice1) + "!")
        scores[i] += dice1
    print("End of Round Summary: ")
    for j in range(players):
        print("Player " + str(j) + " :" + str(scores[j]) + " points")

    #asking to reroll
    reroll=input("Would you like to re-roll or quit the game(yes/quit)? ")
    while reroll.lower()!="yes" and reroll.lower()!="quit":
        print("Invalid input. Please re-enter. ")
        reroll = input("Would you like to re-roll or quit the game(yes/quit)? ")
    if reroll.lower()=="quit":
        quit()
    elif reroll.lower()=="yes":
        pass
print("GAME SUMMARY: \n")

for k in range(players):
    print("Player " +str(k+1)+"Score: "+str(scores[k]))

print("Player "+str(scores.index(max(scores))+1)+" with a score of "+str(max(scores)))


