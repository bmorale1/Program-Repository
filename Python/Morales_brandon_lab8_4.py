#Author:    Isaac Morales
#File name: Morales_brandon_lab8_4.py
#purpose:   To calculate the distance between two points
#date:      September 10, 2015
pointOneX=int(input('Enter the first point X value:'))
pointOneY=int(input('Enter the first point Y value:'))
pointTwoX=int(input('Enter the second point X value:'))
pointTwoY=int(input('Enter the second point Y value:'))

print('Point 1 is:',pointOneX,',',pointOneY)
print('Point 2 is:',pointTwoX,',',pointTwoY)

distance=((pointTwoX-pointOneX)**2+(pointTwoY-pointOneX)**2)**.5
print('the distance is:',distance)

pointOne=(pointOneX,pointOneY)
pointTwo=(pointTwoX,pointTwoY)

import turtle
turtle.Turtle
turtle.forward(distance)
