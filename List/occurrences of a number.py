# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:49:36 2020

@author: Supriyo
"""

list1 = [15, 6, 7, 10, 12, 20, 10, 28, 10]
print(list1)
n=int(input("enter the number to be to find occurrences "))
def occourrances(list):
    count=0
    for i in list1:
        if n==i:
           count+=1
    return count

print("Number of occurrence of ",n," is ",occourrances(list1))