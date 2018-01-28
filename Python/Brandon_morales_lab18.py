#Author:    Isaac Morales
#filename:  Brandon_morales_lab18.py
#purpose:   creating a function that takes a random integer and returns one of six
#           responses based off the value
#date:      October 20, 2015
import random

def Magic(x):
    if x == 1:
        print('nah brah nah!')
    elif x == 2:
        print('HMMMM...perhaps')
    elif x == 3:
        print('That is impossible')
    elif x == 4:
        print('YASSSSSSSS')
    elif x == 5:
        print('JUST DO IT!')
    elif x == 6:
        print('The stars are unclear tonight')

def Main():
    response=input('please enter a yes or no question(type end to stop)')
    while response != 'end':
        randNum=random.randint(1,6)
        Magic(randNum)
        response=input('please enter a yes or no question')
        

Main()
