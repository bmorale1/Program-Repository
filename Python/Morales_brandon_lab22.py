#Author:    Isaac Morales
#File name: Morales_brandon_lab22.py
#purpose:   
#date:      Novemeber 3, 2015

#section 1

name=str(input('enter you first and last names'))
index=name.find(' ')
print(name[0],'.',name[int(index+1)],'.')
print(name[index+1:],',',name[:index])

#section 2

userWord=str(input('enter a word please:'))
userInt= int(input('enter an integer please:'))
newLet=0
for i in userWord:
    newChar=ord(i)+(userInt)
    newLet=str(newLet)+str(chr(newChar))

print(newLet)
#section 3
#im not even going to pretend like i finished the hangman program
guesses=''
incorrect=0
word= 'apples'

print('lets play a game...hangman\n ------')
while incorrect<7:
    char=str(input('enter a single letter'))
    while char.isdigit() or len(char)>1:
        char=str(input('invalid, try again'))
    guesses=str(char)+str(guesses)
    if char!='a'or char!='p'or char!='l'or char!='e'or char!='s':
        incorrect+=1
    else:
        if guesses=='a':
            print('a-----')
        elif guesses=='p':
            print('-pp---')
        elif guesses=='l':
            print('---l--')
        elif guesses=='e':
            print('----e-')
        elif guesses=='s':
        
   
    print(guesses)

