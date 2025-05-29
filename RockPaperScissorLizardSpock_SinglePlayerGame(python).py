print("Anecdotal evidence suggests that in a game of Rock_Paper_Scissors players familiar with each other will tie"
      " 75-80% of the time due to the limited number of outcomes.\n"
      "I suggest Rock_Paper_Scissors_Lizard_Spock. (Invented by SHELDON COOPER)\nIt's very simple\nRULE:\n\t"
      "# SCISSORS cuts PAPER\n\t# PAPER covers ROCK\n\t# ROCK crushes LIZARD\n\t# LIZARD poisons SPOCK\n\t"
      "# SPOCK smashes SCISSORS\n\t# SCISSORS decapitates LIZARD\n\t# LIZARD eats PAPER\n\t# PAPER disproves SPOCK\n\t"
      "# SPOCK vaporizes ROCK\n\t# ROCK crushes SCISSORS  ")
print("Press the keys corrensponding to you choices :\n\t* Rock=r\n\t* Paper=p\n\t* Scissors=x\n\t"
      "* Lizard=l\n\t* Spock=s")
print("So Let's Go !!!\nROCK PAPER SCISSORS LIZARD SPOCK !!!!!!")


import random

def winner(Computer,Player):
    if Computer==Player:
        return None
    elif Computer=='r':
        if Player=='x'or Player=='l' :
            return False
        elif Player=='p' or Player=='s':
            return True
    elif Computer=='p':
        if Player=='r' or Player=='s':
            return False
        elif Player=='x'or Player=='l':
            return True
    elif Computer=='x':
        if Player=='p' or Player=='l':
            return False
        elif Player=='r' or Player=='s':
            return True
    elif Computer=='l':
        if Player=='p' or Player=='s':
            return False
        elif Player=='r' or Player=='x':
            return True
    elif Computer=='s':
        if Player=='r' or Player=='x':
            return False
        elif Player=='p' or Player=='l':
            return True


RandNum= random.randint(1,5)                                    # Chooses any random number between 1,2,3,4,5

if RandNum==1:
    Computer='r'
elif RandNum==2:
    Computer='p'
elif RandNum==3:
    Computer='x'
elif RandNum==4:
    Computer='l'
elif RandNum==5:
    Computer='s'

Player=input("Player   --> Rock(r) Paper(p) Scissors(x) Lizard(l) Spock(s)? --->")
                                              # The brackets mean Rock=r , Paper=p , Scissor=x , Lizard=l , Spock=s.

Game=winner(Computer,Player)

if Game==None:
    if Player=='r' or Player=='p' or Player=='x' or Player=='l' or Player=='s':
        print("Its a TIE.")
    else:
        print("Error Input.")

elif Game:
    print("Woooohhhhooooo , YOU CHAMP!!\nLet's do it again. ")
else:
    print("Ooooooopsiee , looks like YOU LOST \n Let us try one more time.")

print("Your Choice       ---->",Player,"\nComputer's Choice ---->",Computer )





