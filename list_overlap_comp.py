# -*- coding: utf-8 -*-
"""
Created on Mon Feb 29 14:44:27 2016

@author: Vireak
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


result_overlaps = [ y for y in a if y in b]
#result = [i for i in result_overlaps if result_overlaps.count(i) == 1]
result = list(set(result_overlaps))
print(result)
