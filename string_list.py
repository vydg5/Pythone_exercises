# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 12:56:24 2016

@author: Vireak
"""

sentence = input("Enter a string: ")
new_sentence = sentence.replace(" ","")
sentence_rev = new_sentence[::-1]
print(len(sentence))
print(len(new_sentence))
print(len(sentence_rev))

i = 0
while (sentence[i] == sentence_rev[i]):
        i = i+1
        if i == len(sentence):
            break
            print("Palindrome")

if i != len(sentence):
    print("This not a Palindrome")

