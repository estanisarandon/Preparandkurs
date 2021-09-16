from turtle import *

# fram
forward(100)
#tillbaka
backward(100)
#rotera höger
right(90)
#rotera vänster
left(45)

#rita en cirkel med radien
circle(100)

#ändra penfärg
pencolor("blue")
circle(75)

#fylla med färg
color("red", "green")
begin_fill()
circle(150)
end_fill()

#pentorlek
pensize(10)
pencolor("black")
forward(200)

#rotera till en viss pos
setheading(180)
forward(50)

#Flytta
penup()
goto(200, 200)
pendown()
forward(100)

done()
