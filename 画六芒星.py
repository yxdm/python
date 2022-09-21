import turtle
from turtle import *

pendown()
color("red")
width("5")
i=1
j=1
while i<=3:
    forward(100)
    left(120)
    i=i+1

penup()
setx(0)
sety(53)
pendown()
while j<=3:
    forward(100)
    right(120)
    j=j+1

done()

