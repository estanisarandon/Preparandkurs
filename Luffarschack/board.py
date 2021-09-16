from turtle import *

title("Luffarschack")
window_size = Screen()
window_size.setup(1000,800)


# print board
def show_board():
    pensize(5)
    screen = getscreen()
    screen.tracer(False)
    for x in range(-100,101,200):
        penup()
        goto(x,300)
        setheading(270)
        pendown()
        forward(600)
    for y in range (-100, 101, 200):
        penup()
        goto(-300,y)
        setheading(0)
        pendown()
        forward(600)

    penup()
    goto(0,0)
    pendown()
    pencolor("black")
    screen.tracer(True)

# Red line winner
def red_line1():
    pendown()
    setheading(270)
    pencolor("red")
    pensize(10)
    pendown()
    forward(620)

def red_line2():
    pendown()
    setheading(0)
    pencolor("red")
    pensize(10)
    pendown()
    forward(620)

def red_diagonal1():
    pendown()
    setheading(315)
    pencolor("red")
    pensize(10)
    pendown()
    forward(890)

def red_diagonal2():
    pendown()
    setheading(225)
    pencolor("red")
    pensize(10)
    pendown()
    forward(890)


if "__name__" == "__main__":
    show_board()
    done()
