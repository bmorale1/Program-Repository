#Author:    Isaac Morales
#File Name: Morales_brandon_lab9.py
#Purpose:   To choose the best deal between cereals
#Date:      September 15,2015
print('Thank you for using cereal chooser,\nPlease answer to the following questions.')
#cereal1
cerealOne=str(input('Please enter the name of a cereal.'))
priceOne=int(input('Please enter its price.'))
sizeOne=int(input('please enter its size.'))
cpuOne=priceOne/sizeOne
#cereal2
cerealTwo=str(input('Please enter the name of a cereal'))
priceTwo=int(input('Please enter its price.'))
sizeTwo=int(input('please enter its size.'))
cpuTwo=priceTwo/sizeTwo
#cereal3
cerealThree=str(input('Please enter the name of a cereal'))
priceThree=int(input('Please enter its price.'))
sizeThree=int(input('please enter its size.'))
cpuThree=priceThree/sizeThree

#selection process
if (cpuOne<cpuTwo):
    if(cpuOne<cpuThree):
        print('the best deal is:',cerealOne)
    else:
        if(cpuThree<cpuTwo):
            print('the best deal is:',cerealThree)
else:
    if(cpuTwo<cpuThree):
        print('the best deal is:',cerealTwo)
    
        
            
