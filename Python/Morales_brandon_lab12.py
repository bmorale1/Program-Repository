#Author:    Isaac Morales
#file name: Morales_brandon_lab12.py
#purpose:   plays an interactive guessing game with the user
#date:      September 24, 2015

import random

correctNumber = random.randint(0,50)

userNumber = int(input('enter a guess between 0 and 50'))

numTrials = 0

while userNumber != correctNumber:
    numTrials = numTrials+1
    if userNumber>correctNumber:
        userNumber = int(input('too high guess again'))
    elif userNumber<correctNumber:
        userNumber = int(input('too low guess again'))
    if numTrials == 7:
        print('Sorry, too many tries.')
        break
    
if userNumber == correctNumber:
    print('you got it')
