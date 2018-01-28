#author:    Isaac Morales
#purpose:   keeps a running total of vowels and consonants from
#           user input strings
#file name: Morales_brandon_lab16.py
#date:      October 8,2015
vowels=0
consonants=0
userstr=str(input('please enter a string'))

while userstr!='The end':
    for i in userstr:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y':
            vowels+=1
        else:
            consonants+=1
    userstr=str(input('please enter a string'))

print('total number of vowels:',vowels)
print('total number of consonants:',consonants)

