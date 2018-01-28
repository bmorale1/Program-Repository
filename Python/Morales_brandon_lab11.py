#Author:    Isaac Morales
#File Name: Morales_brandon_lab11.py
#Purpose:   print all, odd, and even numbers between 1-100 using a loop
#Date:      September 22, 2015

num=int(input('Please enter a number.'))

#printing numbers 1-num
print('numerical order.')
x=0
for i in range(0,num):
    x=x+1
    print(x,end=' ')


#printing numbers num-1
print('\nreverse order.')
y=num+1
for i in range(0,num):
    y=y-1
    print(y,end=' ')

#even number prints
print('\neven numbers.')
num=num//2

z=0
for i in range(0,num):
    z=z+2
    print(z,end=' ')

#odd number print
print('\nodd numbers.')
number=-1
for i in range(0,num):
    number=number+2
    print(number,end=' ')
    
