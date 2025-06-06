import random

print("Welcome to the GUESS ME NOT.")

# Name of the player
player_name=input("GUESSBot this side. And you are?:- ").upper()

playing= input(player_name+ ", do you want to play (Yes/No):- ").lower()
if playing!='yes':
    print("Maybe next time then. See you soon")
    quit()

# Explaining rules of the game to the user
print("\nOk!! " + player_name + ", let me walk you through the rules")
print("You & I will both enter random numbers in range [0,9].")
print("If your number is same as my number, GAME'S OVER.")
print("Scoring will be: 10 points for 0, then increasing by 1 point for each subsequent score (e.g., 1 point for 1, 2 points for 2, etc.)\n")
print("Lets play " + player_name + ".")

# Evaluation
score=0
no_of_rounds=0

while True:
    user_input = input("Enter your number (0 to 9):- ")

    if not user_input.isdigit():
        print("Invalid Input. Try again to select a number between 0 to 9.")
        continue

    user_input = int(user_input)

    if user_input > 9 or user_input < 0:
        print("Invalid Input. Try again to select a number between 0 to 9.")
        continue

    comp_input = random.randint(0, 9)
    # print(comp_output)

    if user_input == comp_input:
        print("\n\tGAME OVER!!!!\n")
        break

    if user_input==0:
        score+=10
    else:
        score+=user_input

    no_of_rounds+=1

print("Levels Crossed= "+ str(no_of_rounds))
print("Your Score= "+ str(score))
if no_of_rounds>0:
    score_to_round_ratio = score / no_of_rounds
    print("Your score-to-round ratio was " + str(score_to_round_ratio))

print("\nHOPE WE MEET AGAIN SOON mon ami :)")


