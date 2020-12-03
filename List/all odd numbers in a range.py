# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:35:33 2020

@author: Supriyo
"""

starting=int(input("Enter starting range: "))
ending=int(input("Enter ending range: "))
even=[]
odd=[]
for i in range(starting,ending+1):
    if i%2!=0:
        odd.append(i)        
    else:
        even.append(i)        
print("Odd numbers ",odd)
print("Even numbers ",even)