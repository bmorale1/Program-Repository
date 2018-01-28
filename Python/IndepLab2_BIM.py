#Author:    Isaac Morales
#Purpose:   prompt user to donate to charity with thank you message and gift
#FileName:  IndepLab2_BIM.py
#Date:      November 10, 2015

def validate(x):
    while x<0 :
        x=float(input('invalid,please try again'))
    gift(x)

def gift(x):
    if x<=25 and x>0:
        print('thank you for donating\nYou will recieve a Thank-You card!')
    elif x>25 and x<=50:
        print('thank you for donating\nYou will recieve a Thank-You mug!')
    elif x>50 and x<=100:
        print('thank you for donating\nYou will recieve a Thank-You tote!')
    elif x>100 and x<=250:
        print('thank you for donating\nYou will recieve a Thank-You toaster!')
    elif x>250 :
        print('thank you for donating\nYou will recieve a Thank-You sweater and your name will be in the newsletter!')

def main():
    print('Thank you for choosing the donator 2000, press 0 to exit')
    donation=float(input('please enter a donation (can not be negative)'))
    while donation!=0:
        validate(donation)
        donation=float(input('please enter a donation (can not be negative)'))
    print('Good Bye!')

main()
        
        
    
