# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:30:37 2016

@author: Vireak
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c = int(input("Enter a number:"))
b = []
[b.append(a[i]) if a[i] < c else 0 for i in range(0,len(a))]    
print("The following number(s): " + str(b) + " are from list a and are smaller than " + str(c))
