# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 23:14:52 2016

@author: virea_000
"""

def fibonacci(number):
    b = [1 for i in range (0,number)]

    for i in range(2,number):
        b[i] = b[i-1]+b[i-2]
        print(b[i-2])
    return print("Here is your Fibonacci list: " + str(b))
        
a = int(input("How many Fibonnaci do you need? "))
fibonacci(a)