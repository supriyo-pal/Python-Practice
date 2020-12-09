# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 19:55:13 2020

@author: Supriyo

STEP 1: Declare and initialize an array.
STEP 2: Variable n will denote the number of times an array should be rotated toward its left.
STEP 3: The array can be left rotated by shifting its elements to a position prior to them which can be accomplished by looping through the array and perform the operation arr[j] = arr[j+1].
STEP 4: The first element of the array will be added to the last of the rotated array.

"""
def leftRotate(arr,d,n):
    for i in range(d):
        leftRotateByOne(arr,n)
        

def leftRotateByOne(arr,n):
    temp=arr[0]
    for i in range(n-1):
        arr[i]=arr[i+1]
    arr[n-1]=temp
    
def printArray(arr,size):
    for i in range(size):
        print(arr[i],end=" ")


arr=[1,2,3,4,5,6,7,8]
leftRotate(arr,2,7)
printArray(arr,7)

# arr=[1,2,3,4,5,6,7,8]

# n=3

# print("Original Array ")
# for i in arr:
#     print(i)

# for i in range(0,n):
#     first = arr[0]
    
#     for j in range(0,len(arr)-1):
#         arr[j]=arr[j+1]
#     arr[len(arr)-1]=first

# print("Aray after left rotation ")
# for i in range(0,len(arr)):
#     print(arr[i])
    
    