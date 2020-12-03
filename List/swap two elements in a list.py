# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:40:35 2020

@author: Supriyo
"""

number=input("enter the numbers between 0-9 :")
number_list=list()
length=0
for i in range(len(number)):
    number_list.append(number[i])
    length=len(number_list)
print("Choose one position between 0 to",length)
pos1=int(input())
print("Choose another position except ",pos1)
pos2=int(input())


def swap(number_list):
    number_list[pos1],number_list[pos2]=number_list[pos2],number_list[pos1]
    return number_list
print(swap(number_list))
