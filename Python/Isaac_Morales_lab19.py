#Author:    Isaac Morales
#purpose:   tells the user if their input values are prime or not
#File Name: Isaac_Morales_lab19.py
#date:      October 22, 2015

def isPrime(x):
    if x > 1:
       for i in range(2,x):
           if (x % i) == 0:
               return False
               break
       else:
           return True
    else:
        return False

def main():
    print('I can tell you if the number you input is prime.')
    number = int(input('please enter an integer greater than one'))
    while number > 0:
        print(isPrime(number))
        number=int(input('enter another integer'))
    print('Thank you')

main()
