from turtle import *


# Def coords values
X1 = -200
X2 = 0
X3 = 200
YA = 125
YB = -75
YC = -275


# Draw circle
def draw_circle():
    pendown()
    pencolor("black")
    pensize(3)
    setheading(0)
    circle(75)


# Do selection
def do_circle(value):
    penup()
    if value == "1A":
        goto(X1, YA)
        draw_circle()
    elif value == "1B":
        goto(X1, YB)
        draw_circle()
    elif value == "1C":
        goto(X1, YC)
        draw_circle()
    elif value == "2A":
        goto(X2, YA)
        draw_circle()
    elif value == "2B":
        goto(X2, YB)
        draw_circle()
    elif value == "2C":
        goto(X2, YC)
        draw_circle()
    elif value == "3A":
        goto(X3, YA)
        draw_circle()
    elif value == "3B":
        goto(X3, YB)
        draw_circle()
    elif value == "3C":
        goto(X3, YC)
        draw_circle()
