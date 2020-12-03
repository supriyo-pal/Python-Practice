# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 10:41:08 2020

@author: Supriyo
"""
list=[34,5,-1,-5,-9,23,56,76,9,-64]
list_pos=[]
list_neg=[]
for i in list:
    if i>=0:
        list_pos.append(i)
    else:
        list_neg.append(i)
print("Positive Numbers ",list_pos)
print("Negetive numbers ",list_neg)
        


