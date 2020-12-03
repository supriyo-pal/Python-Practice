# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 21:57:25 2020

@author: Supriyo
"""
number=input("enter the numbers between 0-9:")
number_list=list()
length=0
for i in range(len(number)):
    number_list.append(number[i])
    length=len(number_list)
    
print("Choose one position between 0 to",length)
pos1=int(input())
print("Choose another position except ",pos1)
pos2=int(input())

def swapPositions(list, pos1, pos2): 
      
    # popping both the elements from list 
    first_ele = list.pop(pos1)    
    second_ele = list.pop(pos2-1) 
     
    # inserting in each others positions 
    list.insert(pos1, second_ele)   
    list.insert(pos2, first_ele)   
      
    return list
  
# Driver function   
print(swapPositions(number_list, pos1-1, pos2-1)) 