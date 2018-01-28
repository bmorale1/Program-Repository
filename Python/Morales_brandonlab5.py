# Program Name:  BMI.py
# Purpose:  	This program accepts the name and weight in pounds, height in
#                inches of a user and outputs the BMI for the user along with their #                name
# Author:   	Isaac  Morales
# Date:     	Sep 1, 2015

#weightInKg=weight*0.45359237
#converting weight in pounds to kg
#One inch= .0254m
#converting inches to meters

Name=input("What is your name?")
Height=int(input("How tall are you in Ft?"))
Weight=int(input("How much do you weigh in pounds?"))
HeightInMeters=Height*12*.0254
WeightInKg=Weight*0.45359237
BMI=WeightInKg/HeightInMeters**2
print(Name,"Your BMI is",BMI)
  

