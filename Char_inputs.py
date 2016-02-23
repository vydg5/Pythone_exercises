# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 12:13:03 2016

@author: Vireak
"""

# Asking name and age

import numpy as np
import numpy.matlib
import matplotlib.pyplot as plt
import math
import time
from datetime import date

#name = input("What is your name: ")
#print("Your name is " + name)
now = date.today()
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((now.year - age)+100)
print(name + " will be 100 years old in the year " + year)
print("today date is: " + str(now))
print("Your type" + str(type(now.year)))

times = input("how many times: ")
print ("times type: " + str(type(times)))
for i in range (0, int(times)):
    print("Your name is " + name)
    print("Your age is: " + str(age))
