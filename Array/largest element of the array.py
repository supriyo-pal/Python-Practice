# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:23:05 2020

@author: Supriyo
"""

arr=[1,2,3,4,5,6,7,8,9]


def largest(arr):
    largest=arr[0]
    for i in range(0,len(arr)):
        if arr[i]>largest:
            largest=arr[i]
    return largest

print(largest(arr))

print("Another way\n")
print(max(arr))