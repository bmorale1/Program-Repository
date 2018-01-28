#Author:    Isaac Morales
#File Name: Morales_Assignment3.py
#Purpose:   To show and calculate the random path a drunken turtle will take
#Date:      September 17, 2015

import turtle

turtle.screensize(600,600)    
turtle.title('The Drunken Turtle Adventure!')
turtle.bgcolor('lightgrey')

#construct cage
turtle.Turtle
turtle.hideturtle()
turtle.shape('turtle')
for n in [1,2,3,4]:
    turtle.forward(50)
    turtle.left(90)

#center turtle
turtle.penup()
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.showturtle()
turtle.pendown()
turtle.color('green')

#Generating a random heading and path
import random
turtle.pencolor('green')
turtle.speed(speed=1)
totalDistance=0

for i in [1,2,3,4,5,6,7,8,9,10]:
    number = random.randint(1,4)
    if number == 1:
     turtle.setheading(0)
    elif number == 2:
     turtle.setheading(90)
    elif number == 3:
     turtle.setheading(180)
    elif number == 4:
     turtle.setheading(270)

    distance = random.randint(50,100)
    turtle.forward(distance)
    totalDistance=totalDistance+distance

finalPos = turtle.pos()
turtle.stamp()

#centering turtle
turtle.hideturtle()
turtle.penup()
turtle.goto(0,-200)
turtle.color('Black')

#printing the results
turtle.write('The total distance is:',align="center",font=("Times New Roman",20))
turtle.goto(0,-225)
turtle.write(totalDistance,align="center",font=("Times New Roman",25))
turtle.goto(0,-251)
turtle.write('The final Position is:',align="center",font=("Times New Roman",20))
turtle.goto(0,-276)
turtle.write(finalPos,align="center",font=("Times New Roman",25))
