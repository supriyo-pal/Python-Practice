# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 00:04:34 2020

@author: Supriyo
"""

number=input("enter the numbers between 0-9:")
number_list=list()
length=0
for i in range(len(number)):
    number_list.append(number[i])
    length=len(number_list)
    

def sum(list):
    sum1=0
    for i in range(length):
        sum1=sum1+int(number_list[i])
    return sum1
print("Summation of the list element is ",sum(number_list))