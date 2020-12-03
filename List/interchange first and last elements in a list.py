# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 20:11:49 2020

@author: Supriyo
"""
number=input("enter the numbers between 0-9:")
number_list=list()
for i in range(len(number)):
    number_list.append(number[i])n
print("Before Swap ",number_list)
def swap_element(number_list):
    size=len(number_list)
    first=number_list[0]
    number_list[0]=number_list[size-1]
    number_list[size-1]=first
    return number_list
print("After swap ",swap_element(number_list))    
    