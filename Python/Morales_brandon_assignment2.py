#Program name:  Morales_brandon_assignment2.py
#Purpose:       To use entered values to calculate the amount of paint and money
#               needed to cover a "Dumscrum" field.
#Date:          September 4, 2015
#Author:        Isaac Morales


sideA=int(input('what is one side of the field in Ft.?'))
sideB=int(input('what is another side of the field in Ft.?'))
sideC=int(input('what is the distance between two not connected points in Ft.?'))

S = ( sideA + sideB + sideC ) / 2

triArea= (S*(S-sideA)*(S-sideB)*(S-sideC))**(.5)
recArea= sideC*sideA
totalArea= (2*(triArea)+(recArea))
paintCost=(.1*(totalArea))*10

totalArea=round(totalArea,2)
paintCost=round(paintCost,2)

print('The total area is',totalArea,'square Ft.\n so, the total cost of painting the field is:',paintCost,'dollars.')
