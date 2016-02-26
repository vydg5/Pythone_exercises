# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:22:17 2016

@author: Vireak
"""

import random

x1 = random.sample(range(10),9)
x2 = random.sample(range(10),7)

a = []
[a.append(x2[i]) if x2[i] in x1 else 0 for i in range(0,len(x2))]

print(x1)
print(x2)
print(a)
if 10 in x1:
    print("It's true")
else: print(str(10) + " is not in x1")