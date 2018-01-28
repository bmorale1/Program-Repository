#author:    Isaac Morales
#file name: Morales_brandon_assignment#7.py
#purpose:   Plays the "giberish" game
#date:      November 12, 2015
alphabet='abcdefghijklmnopqrstuvzwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ*'

def gibberish(x,y,z):
    #initializing lists and vars
    firstvowel=False
    list1=[]
    list2=[]
    list3=[]
    gibWord=''
    prevVowel=''
    index=0
    index2=0
    index3=0
    vowels='aeiouAEIOU'
    length=len(x)
    numVowels=0
    prevChar=''
    #creating lists
    for i in x:
        list1.append(i)
    for i in y:
        list2.append(i)
    for i in z:
        list3.append(i)            
    for i in range(length):
        #inserting the syllables
        if x[index] in vowels:
            prevVowel=x[index]
            print(prevVowel)
            for i in list2:
                if i=='*':
                    y=list2.insert(index2,prevVowel)
                index2+=1
            if firstvowel==False:
                list1.insert(index+numVowels,y)
                numVowels+=1
                firstvowel=True
            else:
                list1.insert(index+numVowels,z) 
        index+=1
    for i in list1:
        gibWord=gibWord+i
    print(gibWord)



def validate(x):   
    length=len(x)
    index=0
    while index!=length:
        #checking for valid characters
        if x[index] not in alphabet:
            index=0
            x=input('invalid, enter a correct entry')
            length=len(x)
        else:
            index+=1

    return x



def clear():
    #clearing variables for restart
    list1=list()
    gibWord=''
    index=0
    word=''    

    
def main():
    #printing opening statement and commencing game
    choice='Y'
    while choice == 'Y':
        print('Welcome to gibberish, this game will take syllables and words\nand combine them into a funny word!')
        #collecting data and validating
        word=input('please enter a word to commence the game.')
        valword=validate(word)
        syllable1=input('please enter a syllable(no numbers,*wildcard)')
        valsyl1=validate(syllable1)          
        syllable2=input('enter another syllable(no numbers,*wildcard)')
        valsyl2=validate(syllable2)
        #creating gibberish word with validated data
        gibberish(valword,valsyl1,valsyl2)
        clear()
        #prompt for continue and validate
        choice=input('continue playing? (Y/N)')
        while choice != 'Y' and choice != 'N':
            choice = input('please enter Y to contine or N to exit')
    print('GoodBye')

main()
