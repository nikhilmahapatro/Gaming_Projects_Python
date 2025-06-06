
#------------------------------------TURTLE RACING--------------------------------------#

import turtle
import time
import random

#__________________________________________________________________________________________________________________

# FUNCTIONS

# constant value (capital letters)
# define the width and height of the turtle screen
WIDTH , HEIGHT= 700 , 700
# Possible Colours of Turtles
COLOURS = ['Red','Cyan','Green','Orange','Yellow','White','Purple','Blue','Pink','Brown']
#print(colours)

# Function to get no of racers from the user
def get_no_of_racers():
    no_of_racers = 0
    while True:
        # Check if the input is a number
        no_of_racers = input("Enter the no of racers (2-10):- ")
        if no_of_racers.isdigit():
            no_of_racers = int(no_of_racers)
        else:
            print("Invalid Input..................Please try again.")
            continue

        # Check if the input is in range
        if 2<=no_of_racers<=10:
            return no_of_racers
        else:
            print("Invalid Input.....Enter a number in range [2,10]")
            continue

# Conducting the race
def race(colours_to_select):
    Cars = create_turtles(colours_to_select)
    while True:
        for racer in Cars:
            distance = random.randrange(0,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y>= HEIGHT//2-10:
                return colours_to_select[Cars.index(racer)]


# Function to set up the turtles for the race
def create_turtles(colours_to_select):
    Cars = []
    spacing_x= WIDTH//(len(colours_to_select)+1)
    for i,colour in enumerate(colours_to_select):
        racer = turtle.Turtle()
        racer.color(colour)
        racer.shape('turtle')
        racer.left(90)                            # Coz they are pointed to the right by default
        racer.penup()
        # Setting up a starting position for the turtles
        racer.setpos(-WIDTH//2 + (i+1)*spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        Cars.append(racer)
    return Cars

# Function to set up the turtle screen
def init_turtle():
    # Setting up the turtle screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    # Changing the title of the screen
    screen.title("Turtle Racing!!!")
    # Changing the background colour from white
    screen.bgcolor('Black')

#_____________________________________________________________________________________________________________________

# MAIN CODE

race_input = get_no_of_racers()
# select random colours from the COLOURS array
random.shuffle(COLOURS)
colours_to_select = COLOURS[:race_input]

init_turtle()
#Cars = create_turtles(colours_to_select)

# Declaring the winner of the race
winner = race(colours_to_select)
print(winner)
turtle.done()

#-------------------------------------------------------------------------------------------------------------

# DEMO MOVEMENTS
'''
racer1 = turtle.Turtle()
racer1.color('Cyan')                       # Colour of racer
racer1.shape('turtle')                     # Shape of racer
racer1.speed(1)
racer1.penup()                             # for no lines during movement
racer1.backward(200)                       # No of pixels
racer1.left(60)                            # Angle in degrees
racer1.forward(100)
racer1.right(45)
racer1.pendown()                           # re-initializing appearance of lines
racer1.forward(100)
racer1.left(30)
racer1.forward(100)
#time.sleep(200)

racer2 = turtle.Turtle()
racer2.color('Red')                        # Colour of racer
racer2.shape('turtle')                     # Shape of racer
racer2.speed(5)
racer2.penup()                             # for no lines during movement
racer2.backward(150)                       # No of pixels
racer2.left(75)                            # Angle in degrees
racer2.forward(200)
racer2.right(40)
racer2.pendown()                           # re-initializing appearance of lines
racer2.forward(100)
racer2.left(90)
racer2.forward(100)
'''




