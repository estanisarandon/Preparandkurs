from turtle import *

speed(0)

def write_text (text, x, y, color):
    style = ("Courier", 8, "normal")
    penup()
    goto(x,y)
    pencolor(color)
    write(text, font=style, align="center")


#<----------->
#-     0     +
def show_coords():
    screen = getscreen()
    screen.tracer(False)
    for x in range (-300, 301, 10):
        penup()
        if x % 100 == 0:
            write_text(x, x, -320, "red")
            if x == 0:
                pencolor("black")
            else:
                pencolor("black")
        else:
            pencolor("lightgray")
        goto(x,300)
        setheading(270)
        pendown()
        forward(600)

    # Y
    for y in range (-300, 301, 10):
        penup()
        if y % 100 == 0:
            write_text(y, -320, y, "red")
            if y != 0:
                pencolor("black")
        else:
            pencolor("lightgray")
        goto(-300,y)
        setheading(0)
        pendown()
        forward(600)

    penup()
    goto(0,0)
    pendown()
    pencolor("black")
    screen.tracer(True)

