from turtle import *

def square(side):
    for i in range (4):
            forward(side)
            right(90)

speed(0)
for x in range(10):
    color("firebrick")
    begin_fill()
    square(70)
    right(36)
    end_fill()

for x in range(10):
    color("red")
    begin_fill()
    square(60)
    right(36)
    end_fill()

for x in range(10):
    color("orange red")
    begin_fill()
    square(50)
    right(36)
    end_fill()

for x in range(10):
    color("dark orange")
    begin_fill()
    square(40)
    right(36)
    end_fill()

for x in range(10):
    color("orange")
    begin_fill()
    square(30)
    right(36)
    end_fill()

for x in range(10):
    color("gold")
    begin_fill()
    square(20)
    right(36)
    end_fill()

for x in range(10):
    color("yellow")
    begin_fill()
    square(10)
    right(36)
    end_fill()

done()
