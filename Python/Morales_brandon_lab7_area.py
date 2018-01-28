#Author:        Isaac Morales
#File Name:     Area.py
#Date:          September 8,2015
#Description:   Calculates the total area of a house,
#               And how much carpet will be needed
w=int(input('Enter a value for W:'))
x=int(input('Enter a value for X:'))
y=int(input('Enter a value for Y:'))
z=int(input('Enter a value for Z:'))

#collecting the user's values

Room1=w*y
Room2=(w*z)/2
Room3=x*y
Room4=x*z

#calculating the seperate room's area

totalArea=Room1+Room2+Room3+Room4
carpetArea=Room2+Room3

#calculating the total area and the area needed to be carpeted

print('the total area of the house is:',totalArea,'square feet')
print('the area needing to be carpeted is:',carpetArea,'square feet')

    
