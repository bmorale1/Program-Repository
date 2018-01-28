#author:    Isaac Morales
#file name: brandon_morales_lab26.py
#purpose:   Plays the "giberish" game
#date:      November 19, 2015
readingList=['Catch 22','Time Machine']
validChoices='QqLlAaNnRrIi'
empty=[]

def printMenu():
    print('List all (l)')
    print('add(a)')
    print('Number of books(N)')
    print('Remove(R)')
    print('insert(I)')
    print('Quit(Q)')

def printlist(x):
    if x==empty:
        print('No titles on list')
    else:
        for i in x:
            print(i,end='\n')

def main():
    print('hello!')
    printMenu()
    choice=input('enter a selection')
    while choice not in validChoices:
        choice=input('invalid, try again.')
    while choice!='Q' and choice!='q':
        if choice=='L'or choice=='l':
            printlist(readingList)
        elif choice=='A'or choice=='a':
            book=input('enter a book')
            readingList.append(book)
        elif choice=='N'or choice=='n': 
            print(len(readingList)) 
        elif choice=='R'or choice=='r':
            remBook=input('enter the book you want to remove')
            if remBook in readingList:
                readingList.remove(remBook)
            else:
                print('The given book title is not in the reading list')                         
        elif choice=='I'or choice=='i':
            insBook=input('enter the book title you want to insert')
            if insBook in readingList:
                print('That book is already on the list')
            else:
                index=int(input('at what index do you want it?'))
                while index<0 or index>len(readingList):
                    index=int(input('invalid try again'))
        printMenu()
        choice=input('enter a selection')
        while choice not in validChoices:
            choice=input('invalid, try again.') 
    print('Bye!')
    print('End of program.')

main()
