# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 20:21:46 2016

@author: Vireak
"""

number = int(input("Enter a number: "))
rest = number % 4
if rest==0:
    print("this is an even and multiple of 4 number")
elif rest == 2:
    print("this is just an even number") 
else:
    print("this is an odd number")
    

num, check = input("Enter two numbers here: ").split()
rest1 = int(check) % int(num)
if rest1 == 0:
    print("number is divided nicely by check")
else:
    print("number is NOT divided nicely by check")