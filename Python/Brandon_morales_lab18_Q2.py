#Author:    Isaac Morales
#filename:  Brandon_morales_lab17_Q2.py
#purpose:   to create a square using user input length and color
#date:      October 20, 2015
import turtle

def square(x,y): 
    turtle.color(y)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)
    turtle.end_fill()

def main():
    length=int(input('Please type an integer:'))
    color=input('please enter a basic color')
    square(length, color.lower())
    
    
main()
