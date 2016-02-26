# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 14:40:18 2016

@author: Vireak
"""

import random


while True:
    yorn = input("Do you want to play again? y or n: ")
    if yorn == "n":
        break
    else:
        human = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
        while (human>3 or human<1):
            human = int(input("Enter again! 1, 2 or 3: "))

        mylist = [1, 2, 3]
        mylist2 = ['rock', 'paper', 'scissors']
        pc = random.choice(mylist)
        print("Human picked " + str(human) + " which is " + mylist2[mylist.index(human)])
        print("PC randomly picked " + str(pc) + " which is "+ mylist2[mylist.index(pc)])

        if (human-pc) == 1 or (human-pc) == -2:
            print("Human wins")
        elif human-pc == 0:
                print("It's a tie")
        else: print("pc won because pc picked " + mylist2[mylist.index(pc)] +" and human picked "+ mylist2[mylist.index(human)])

