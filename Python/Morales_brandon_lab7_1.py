#Author:    Isaac Morales
#File Name: Morales_brandon_lab7_1.py
#Purpose:   find the sum, average,max,and min of 4 integers
#Date:      September 10, 2015
firstNumber=int(input('Enter a number:'))
secondNumber=int(input('Enter another number:'))
thirdNumber=int(input('Enter yet another number:'))
fourthNumber=int(input('And enter one more number:'))
Max=max(firstNumber,secondNumber,thirdNumber,fourthNumber)
Min=min(firstNumber,secondNumber,thirdNumber,fourthNumber)
Sum=(firstNumber+secondNumber+thirdNumber+fourthNumber)
Avg= Sum/4
print('The maximum is:',Max)
print('The minimum is:',Min)
print('The Sum is:',Sum)
print('The average is:',Avg)
