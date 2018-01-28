#Author:    Isaac Morales
#file name: Morales_brandon_lab20.py
#purpose:   draw a row squares that alternate being filled and not
#date:      October 27, 2015

import turtle


def drawSquare(x,y):
    turtle.hideturtle()
    count=0
    for i in range (8):
        count+=1
        if count==1 or count==3 or count == 5 or count == 7:
            turtle.color(y)
            turtle.begin_fill()
        for i in range (4):
            turtle.forward(x)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(x)
        turtle.color('black')
    turtle.penup()
    turtle.goto(0,-50)
    turtle.write('Thanks, goodbye!')
            


def main():
    num=int(input('please enter a number between 20 and 30:'))
    while num >30 or num<20:
        num=int(input('invalid, please enter a number between 20 and 30'))
    color=input('enter a basic color')
    drawSquare(num,color)

main()
