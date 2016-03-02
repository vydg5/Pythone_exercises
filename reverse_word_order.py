# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:08:41 2016

@author: Vireak
"""

def reverse_string(my_string):
    my_string = my_string.split()
    return print(my_string[::-1])

a = input("Enter your string and I will reverse it: ")
reverse_string(a)