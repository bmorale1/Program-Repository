#Author:    Isaac Morales
#purpose:   Convert strings into ASCII
#file name: IsaacMoralesLab14.py
#date:      October 1, 2015

userString = str(input('enter a phrase or characters:'))

for i in (userString):
    print(ord(i))

myName = [73,115,97,97,99]

for i in(myName):
    print(chr(i),end='')
