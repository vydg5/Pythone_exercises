# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 11:55:26 2016

@author: Vireak
"""

num = int(input("Enter a number: "))

[print(str(i) + " is a divisor") if (num%i) == 0 else 0 for i in range(1, int(num/2 + 1))]

