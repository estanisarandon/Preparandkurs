from turtle import *
from colors import colors


# Draw square
def square(x, y, side, c):
    penup()
    goto(x,y)
    pendown()
    color(c)
    begin_fill()
    for i in range(4):
        forward(side)
        right(90)
    end_fill()

x = -800
y = 300
style = ("Courier", 8, "normal")
for c in colors:
    square(x, y, 10, c)
    penup()
    pencolor("black")
    goto(x + 20, y - 10)
    pendown()
    write(c, font = style, align = left)
    y -= 10
    if y < -360:
        y = 300
        x += 150

done()
