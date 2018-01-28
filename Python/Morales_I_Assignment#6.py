#Author:    Isaac Morales
#File Name: Morales_I_Assignment#6.py
#purpose:   create a TV remote simulator
#Date:      October 28, 2015

#initialize variables
tvPower= 0
tvChannel=1
tvVolume=0
mute = 0
userChoice = 0

#printing Tv state
def TvState():
        if tvPower == 1:
            if mute ==1:
                print('Tv is: on Channel:', tvChannel,'Volume: mute')
            else:
                print('Tv is: on Channel:', tvChannel,'Volume:', tvVolume)
        elif tvPower == 0:
            print('Tv is off')
            
#processing user input
def processCommand(x):
        global tvPower
        global tvChannel
        global tvVolume
        global mute
#power command        
        if x == 'P':
                if tvPower==0:
                    tvPower=1
                else:
                     tvPower=0                  
#Volume up command
        if x == 'V+':
                if tvPower==0:
                        print('turn on the tv first')
                else:        
                       if tvVolume >= 5:
                            tvVolume= 5
                       else:
                            tvVolume +=1
#Volume down command
        elif x == 'V-':
                if tvPower==0:
                       print('turn on the tv first')
                else:
                       if tvVolume <= 0:
                            tvVolume = 0
                       else:
                            tvVolume -=1
#Channel up command
        elif x == 'C+':
                if tvPower==0:
                        print('turn on the tv first')
                else:
                        if tvChannel > 4:
                             tvChannel=1
                        else:
                             tvChannel +=1
#Channel down command
        elif x =='C-':
                if tvPower==0:
                        print('turn on the tv first')
                else:
                        if tvChannel < 2:
                             tvChannel = 5
                        else:
                             tvChannel -=1
#mute command
        elif x == 'M':
                if tvPower==0:
                        print('turn on the tv first')
                else:
                        if mute == 0:
                             mute =1
                        else:
                             mute =0
                             tvVolume=3

def validInput(x):
#loop untill valid input is given
    while x!= 'P' and x!= 'M' and x!= 'V+' and x!= 'V-' and x!= 'C+' and x!= 'C-' and x!='X':
        x=str(input('invalid,enter a valid choice please.'))
#process command once input is valid
    if x== 'P' or x== 'M' or x=='V+' or x=='V-'or x=='C+' or x=='C-' or x=='X':
        processCommand(x)    
     
def main():
#loop prompting for input until exit        
    print('This is a TV Remote simulator')
    print('Valid Inputs: "P"(Power), "V+"(Vol. up), "V-"(Vol. Down),\n "C+"(Chan. up)/n,"C-"(Chan. Down), "M",(Mute),X to end')
    userChoice= input('please enter your choice.')
    while userChoice != 'X':
        validInput(userChoice)
        TvState()
        userChoice= input('please enter your choice.')
    print('Exiting simultion')

main()
