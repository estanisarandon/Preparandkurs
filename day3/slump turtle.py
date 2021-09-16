from turtle import *
import random
from typing import List

speed(0)

def square(side):
    for _ in range(4):
        forward(side)
        right(90)


colors = ['yellow', 'orange', 'green', 'lightgreen', 'lightblue', 'pink']

for _ in range(1000):
    x = random.randrange(-200, 201)
    y = random.randrange(-200, 201)
    c = random.choice(colors)
    r = random.randrange(0, 360)

    setheading(r)
    penup()
    goto(x,y)
    color(c)
    pendown()
    begin_fill()
    square(25)
    end_fill()

done()
