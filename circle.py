from turtle import *

speed(0)

def move(A,B):
    penup()
    goto(A,B)
    pendown()

def redondo(size):
    circle(size)
    right(5)
begin_fill()
color("sea green")
for i in range(72):
    if i >18:
        begin_fill()
        color("dark slate gray")
        end_fill()
    elif i > 36:
        begin_fill()
        color("light sea green")
        end_fill()
    elif i > 54:
        begin_fill()
        color("light slate gray")
        end_fill()
    redondo(100)

done()
