# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:12:13 2016

@author: virea_000
"""

import random

#pc = random.sample(range(9),1) #THIS IS a list
pc = random.randint(1,25)
print(pc)

human = 0
old = pc
i = 1
while human < pc or human > pc:
    human = int(input("Give me a guess: "))
    if human < pc:
        print("Too low")
        if human > old and i>1:
            print("hot")
        elif human < old and i>1:
            print("cold")
    elif human > pc: 
        print ("Too high")
        if human > old and i>1:
            print("cold")
        elif human < old and i>1:
            print("hot")
    old = human
    i = i + 1

if (human == pc):
    print("This is it!")

