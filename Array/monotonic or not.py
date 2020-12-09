# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:50:30 2020

@author: Supriyo
"""
def isMonotonic(A): 
  
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
  
# Driver program 
A = [6, 5, 4, 4] 
  
# Print required result 
print(isMonotonic(A)) 
  
# if (isMonotonic(1)):
#     print("Array is monotonic")
# else:
#     print("Array is not monotonic")