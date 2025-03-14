import random

def roll():
    roll_value = random.randint(1, 6)
    return roll_value

print("As the name indicates, in this dice game, the object is to avoid rolling a seven. Doing so will end your turn and give your opponent(s) a chance to get to the highest score first. And that’s it! This one is blissfully simple and easily played with as many people as you have around.")

#setting players
while True:
    try:
        players = int(input("Enter the number of players: Recommended to have 10 or less with a minimum of 2. "))
        if players < 2:
            print("Invalid input. Must have at least 2 players.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")
#setting max score
while True:
    try:
        max_score = int(input("Enter the max score: "))
        if max_score < 2:
            print("Invalid input. Max score must be at least 2.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

scores = [0] * players
winner = False
#playing game
while not winner:
    #each player's turn
    for i in range(players):
        sevens = False
        while not sevens:
            dice1 = roll()
            dice2 = roll()
            if dice1 + dice2 == 7:
                print(f"Player {i + 1} rolled a {dice1} and a {dice2}. That's a 7. No points!")
                sevens = True
            else:
                scores[i] += dice1 + dice2
                print(f"Player {i + 1} rolled a {dice1} and a {dice2}. That's {dice1 + dice2} points")
                print(f"Player {i + 1} now has {scores[i]} points.")
                if scores[i] >= max_score:
                    print(f"Player {i + 1} has won the game with "+str(scores[i])+" points !")
                    winner = True
                    break
        if winner:
            break
            #round summary
    if not winner:
        print("\n--- End of Round Summary ---")
        for j in range(players):
            print(f"Player {j + 1}: {scores[j]} points")
        while True:
            roll_again = input("Roll again or quit? (yes/quit): ").lower()
            if roll_again == "quit":
                winner = True
                break
            elif roll_again == "yes":
                break
            else:
                print("Please enter 'yes' or 'quit'.")