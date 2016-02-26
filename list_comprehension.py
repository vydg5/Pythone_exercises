# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 12:15:56 2016

@author: Vireak
"""
"""
order of if and for matters
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = [test if (test%2==0) else 0 for test in a]
print(new_list)

b = [test for test in a if test % 2 == 0]
print(b)

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
ages = [2014 - i for i in years_of_birth]
print(ages)

  
