# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 22:09:31 2020

@author: Supriyo
"""

number=input("enter the numbers between 0-9:")
number_list=list()
length=0
for i in range(len(number)):
    number_list.append(number[i])
    length=len(number_list)
    
search=input("Enter the element to be searched")

if (search in number_list):
    print("element found")
else:
    print("element not found ")

print("********************ANOTHER APPROACH *********************\n")

for i in range(length):
    if number_list[i]==search:
        print("elelemt found at position ",i+1)