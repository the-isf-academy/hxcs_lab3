# /////////// INSTRUCTIONS /////////////////

# 🤔 This program has a lot of potential, but so far it can only generate two drawings

# 🪾 Add at least two more branches to the conditional 
#    so that the program can draw more than just a square and a circle

# ❗️ An elif statement will probably be useful here.

# 🔺 For example, your program could also draw a triangle and a pentagon.

# ////////////////////////////////////////////

# Don't delete this line! 
from turtle import *
from turtle import *

drawing = input("What would you like me to draw? ")
size = int(input("How big should I draw it? "))

if drawing == "square":
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
        
elif drawing == "circle":
    circle(size)

else:
    print("Sorry, I don't know how to draw that...")