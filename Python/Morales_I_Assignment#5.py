#author:    Isaac Morales
#filename:  Morales_I_assignment#5.py
#purpose:   to create a visually appealing pattern using functions
#           and user input values 
#date:      october, 18, 2015

import random

#Set user input function
def inputValidate():
    user_number = input("Enter the side size of the hexagons(10-200): ")
    if user_number.isdigit():
        while int(user_number)<10 or int(user_number)>200:
            user_number=int(input('invalid, please re-enter(10-200)'))
        global number
        number = int(user_number)  
    else:
        while user_number.isdigit() == False or int(user_number)<10 or int(user_number)>200:
            user_number = input('invalid, please re-enter(10-200)')
        number = int(user_number)  
      

#Set turtle design function
def patternCons():
    import turtle
    megan = turtle.Turtle()
    turtle.bgcolor('grey')
    megan.hideturtle()
    megan.speed(10)
    for i in range(18):
        megan.begin_fill()
        megan.color(random.random(),random.random(),random.random())
        for i in range(5):
            megan.forward(number)
            megan.left(60)
        megan.forward(number)
        megan.left(40)
        megan.penup()
        megan.forward(30)
        megan.pendown()
        megan.end_fill()

#define main function
def main():
    print('This program makes a ring of hexagons,\nthe number you enter determines the size of the hexagons')
    inputValidate()
    print('Constructing pattern..')
    patternCons()
#call main
main()
