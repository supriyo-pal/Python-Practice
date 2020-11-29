# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:23:41 2020

@author: Supriyo
"""

a=[i for i in range(8)]
def sum():
    sum=0
    for i in a:
        sum=sum+a[i]
    return sum
print("sum of list is ",sum())