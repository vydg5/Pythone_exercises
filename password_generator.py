# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 16:45:28 2016

@author: Vireak
"""

import random
import string

def pw_generator(length):
    special_list = list(string.punctuation)
    upper_list = list(string.ascii_uppercase)
    lower_list = list(string.ascii_lowercase)
    number_list = [ i for i in range(1,9)]
    all_list = special_list + upper_list + lower_list + number_list
    your_pw = [random.choice(all_list) for i in range(0,length-1)]
    print(your_pw)    
    return your_pw

def weak_pw():
    weak_list = ['tata', 'qwertyuiop', '123456']
    your_pw = random.choice(weak_list)
    return your_pw

human = input("Weak or strong?: ")
if human == 's':
    a = int(input("How long do you want your pw to be: "))
    new_display = "".join(pw_generator(a))
    print("Here is your pw: "+new_display)
else: print("Here is your weak password: " + weak_pw())


#print(type(special_list))
#print(lower_list)
#print(upper_list)
#print(type(number_list))
#print(all_list)
