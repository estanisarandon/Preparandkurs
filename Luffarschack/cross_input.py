from turtle import *


# Def values
X1 = -275
X2 = -75
X3 = 125
YA = 275
YB = 75
YC = -125

# Draw cross
def draw_cross():
    pendown()
    pencolor("black")
    pensize(3)
    right(45)
    forward(200)
    setheading(90)
    penup()
    forward(150)
    left(135)
    pendown()
    forward(200)


# Do selection
def do_cross(value):
    penup()
    if value == "1A":
        goto(X1,YA)
        draw_cross()
    elif value == "1B":
        goto(X1,YB)
        draw_cross()
    elif value == "1C":
        goto(X1,YC)
        draw_cross()
    elif value == "2A":
        goto(X2,YA)
        draw_cross()
    elif value == "2B":
        goto(X2,YB)
        draw_cross()
    elif value == "2C":
        goto(X2,YC)
        draw_cross()
    elif value == "3A":
        goto(X3,YA)
        draw_cross()
    elif value == "3B":
        goto(X3,YB)
        draw_cross()
    elif value == "3C":
        goto(X3,YC)
        draw_cross()



