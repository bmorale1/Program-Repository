#Author:    Isaac Morales
#File name: Morales_brandon_lab10_dateChecker.py
#Purpose:   To check if the date the user enter is valid
#date:      September 16, 2015



month =int(input('enter the number of a month.'))
day = int(input('enter a day of the month.'))
year = int(input('enter a year.'))

print('you entered',day,'/',month,'/',year)

leapYear=False
if(year%400==0) or (year%4==0 and year%100!=0):
    leapYear=True
   

   
if (0>month)or(month>12):
    print('not a valid date')
elif(month == 1) and ( 0>day or 31<day):
    print('not a valid date.')
elif(month == 3) and ( 0>day or 31<day):
    print('not a valid date.')
elif(month == 5) and ( 0>day or 31<day):
    print('not a valid date.')
elif(month == 7) and ( 0>day or 31<day):
    print('not a valid date.')
elif(month == 8) and ( 0>day or 31<day):
    print('not a valid date.')
elif(month == 10) and ( 0>day or 31<day):
    print('not a valid date.')
elif(month == 12) and ( 0>day or 31<day):
    print('not a valid date.')
elif(month == 4) and ( 0>day or 30<day):
    print('not a valid date.')
elif(month == 6) and ( 0>day or 30<day):
    print('not a valid date.')
elif(month == 9) and ( 0>day or 30<day):
    print('not a valid date.')
elif(month == 11) and ( 0>day or 30<day):
    print('not a valid date.')
elif(month==2)and(leapYear==True)and (0>day or 29<day):
    print('not a valid date.')
elif(month==2)and(leapYear==False) and (0>day or 28<day):
    print('not a valid date.')
else:
    print('the date is valid.')
        
