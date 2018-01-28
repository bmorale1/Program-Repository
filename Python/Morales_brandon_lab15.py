#author:    Isaac Morales
#purpose:   Create a program that prints numbers 1-120 and multiples of 3, 5, and 7
#            as "zap", "zop", or "ZipZap" respectively
#filename:  Morales_brandon_lab15.py
#date:      october 6, 2015

ittiration=0

for i in range(1,121):
    ittiration=ittiration+1
    if i%3==0 and i%5 ==0 and i%7==0:
        print('ZipZapZop',end=' ') 
    elif i%3==0 and i%5 ==0:
        print('ZipZap',end=' ')
    elif i%3==0 and i%7 ==0:
        print('ZapZop',end=' ')
    elif i%5==0 and i%7==0:
        print('ZipZop',end=' ')
    elif i%3 == 0:
        print('zip',end=' ')
    elif i%5 == 0:
        print('Zap',end=' ')
    elif i%7 == 0:
        print('Zop',end=' ')
    else:
        print(i,end=' ')
    if ittiration%10==0:
        print('\n')
