# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:27:58 2020

@author: Supriyo
"""
list1=[12,34,56,45,35,23,78,56,123]
list2_even=[]
list2_odd=[]
for i in list1:
    if i%2==0:
        list2_even.append(i)
    else:
        list2_odd.append(i)
print("Previous List \n",list1)
print("Even numebrs in the list \n",list2_even)
print("Odd numebrs in the list \n",list2_odd)
