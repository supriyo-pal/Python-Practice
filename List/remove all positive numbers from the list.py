# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:27:35 2020

@author: Supriyo
"""

list1 = [11, 5, 17, 18, 23, 50] 
list_pos=[]

for ele in list1:
    if ele%2==0:
        list1.remove(ele)
print("Old List contains ",list1)

#print("All the Positive numbers are ",list_pos)
    