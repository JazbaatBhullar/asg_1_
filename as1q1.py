#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Asus
#
# Created:     06-01-2022
# Copyright:   (c) Asus 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#answer 1
#taking input from user of numbers whose average is to be calculated
n1=input("enter your first number here :")
n2=input("enter your second number here :")
n3=input("enter your third number here :")

#printing the average of numbers as final output
print("#average of given numbers is = " + str((int(n1)+int(n2)+int(n3))/3))


#answer 2
#taking inpts from user egradinging their income and no. of dependents
income=input("enter your yearly income in dollars here : ")
dependents=input("enter your number of dependents here : ")

#calculating taxable income
taxable_income=int(income)-10000-(3000*int(dependents))

#calculating tax and printing it as final output
tax=taxable_income*20/100
print(tax)

#answer 3
#taking inputs from users
SID=input("enter your SID here : ")
name=input("enter your name her : ")
gender=input("enter your gender here in M,F,U: ")
course_name=input("enter your course name here :")
CGPA=input("enter your CGPA here :")

#printing our inputs in a list format
print[SID,name,gender,course_name,CGPA]

#answer 4
#marks of 5 student in random order
m1=69
m2=96
m3=90
m4=12
m5=35

#taking L as a list
L=[m1,m2,m3,m4,m5]

#sorting list in an increasing order
L.sort()
print(L)

#sorting list in decreasing order
L.sort(reverse=True)
print(L)

#answer5-a
#writing list as L
L=['Red' , 'Green' , 'White' , 'Black' , 'Pink', 'Yellow' ]

#using .remove function to remove undesired element
L.pop(3)

#printing fianl obtained list as our output
print(L)


#answer5-b
L.pop(2),L.insert(3,'Purple') #removing undesired element and adding 'Purple' instead of it
print(L)