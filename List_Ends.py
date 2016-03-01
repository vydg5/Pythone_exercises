# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 22:44:10 2016

@author: virea_000
"""

def re_list(my_list):
    new_list = [int(my_list[0]), int(my_list[len(my_list)-1])] #list containing numbers as integers not char
    return print(new_list)


a = input("Enter a list: ")
a = a.split() #Take the space out
re_list(a)

b = [2,3,4,5,6]
re_list(b)
