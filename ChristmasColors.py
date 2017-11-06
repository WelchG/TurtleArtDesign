import turtle
import random
turtle.colormode(255)
from RGSFunction import*#Import everything from RGF file(RegGreenFunction).
t=turtle.Turtle()

t.hideturtle()

t.speed(0)

y=-550#Making x and y variables that stores a value
x=-800

for times in range(11):
    circle(t,x,y,100,50)#Calling the function circle and sending values to it.
    y=y+100

for times in range(11):
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    
    x=random.randint(-750,750)#Choosing a random number between -750 and 750.
    y=random.randint(-450,450)#Choosing a random number between -450 and 450.
    snowflake(t,x,y,red,green,blue)
