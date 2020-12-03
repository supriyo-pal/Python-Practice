# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 12:44:30 2020

@author: Supriyo
"""

list1 = [11, 5, 17, 18, 23, 50]

list2=[i for i in list1]

def Cloning(list):
    list2=[i for i in list1]
    return list2

list3=Cloning(list1)
print(list2)
print(list3)