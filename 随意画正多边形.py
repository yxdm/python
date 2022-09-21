from turtle import done, forward, right


import turtle
from turtle import *
distance = 100
i=1
num=int(input("请输入多边形需要几条边: "))
while i<=num:
    forward(distance)
    right(360/num)
    i=i+1
done()



