# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 11:50:11 2020

@author: Supriyo
"""

test_list=[5,6,20,8,[],89,[],98]

print("The original list is :",test_list)

res=[ele for ele in test_list if ele!=[]]

print("List after removing the empty lists ",res)


# Initializing list  
test_list1 = [5,6,20,8,[],89,[],98] 
print("\n***********ANOTHER APPROACH***********\n")  
# printing original list  
print("The original list is : " + str(test_list1)) 
  
# Remove empty List from List 
# using filter 
res1 = list(filter(None, test_list1)) 
  
# printing result  
print ("List after empty list removal : " + str(res1)) 
