# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 19:03:55 2016
Solution by Vireak
No list involved--quite fast
"""
import math
def get_integer(text):
    return int(input(text))
    
human_number = get_integer("Enter a number ")
My_list = [2,3,5,7]

if  human_number%math.sqrt(human_number) == 0.0 or human_number%2 == 0\
    or human_number%3 == 0 or human_number%5 == 0 or human_number%7 == 0:
    if human_number in My_list: 
        print("This is a prime number")
    else: print("This is NOT a prime number")
else: print("This is a prime number")    

print(human_number%math.sqrt(human_number))


"""
Another solution involved making a list: could take a long time if the number is high
"""
#num = get_integer("This is an example: ")
#a = [x for x in range(2,num) if num%x == 0]
#print(a)
#if len(a)==0:
#    print("Prime")
#else: print("Not a prime")
