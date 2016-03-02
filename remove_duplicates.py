# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 12:26:27 2016

@author: Vireak
"""

def rm_duplicates(my_list):
    #my_list = set()
    #my_list.add("Michelle")
    return print("Your new list is:" + str(set(my_list)))
    
a = str(input("Enter your full list: "))
a = a.split() #Discredit space as an element
rm_duplicates(a)