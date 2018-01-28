#Author:    Isaac Morales
#File Name: Morales_brandon_lab21.py
#purpose:   testing out string functions
#Date:      October 29, 2015

#Section 1
print("Hello, World!".upper())
#i-hello world was printed in all uppercase.
#ii- yes, it was exactly what i expected.
#iii- it happened because the point of the .upper function is to convert a string
#     into all capitals
string= "Hello, World"
print(string.lower())
print(string.lower().upper())
#i-the string was printed once in all lowercase, and once in all uppercase.
#ii- yes, it was exactly what i expected.
#iii-the first print statement took the string to lowercase, and then the
#    second print statement took it to lowercase, then uppsercase.

#Section 2
print("     a".strip())
string="b    "
print(string.strip())
stringTwo=("Hello,   World!")
print(stringTwo.strip())
#i- in part C the space between hello and world was not removed
#ii- no, it was the exact opposite of my expectations.
#iii- i have no clue why the space between the two words was not stripped

#Section 3
def myCount(x,y):
    count=0
    for i in x:
        if y == i:
            count+=1
    return count


def main():
    string=input("please enter a string")
    char = input('enter the character you want to find')
    print(myCount(string,char))
    
main()

#Section 4
abeSpeech='Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'
print(abeSpeech.replace('a','e'))
#i- no, because the replace function would replace all instances of 'a' with 'c'
#and then it would replace all instances of 'c' with 'a'
