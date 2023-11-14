#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:29:11 2023

@author: sl
"""
import pandas as pd
import numpy as np 


a = np.array([1,2,3])
b = np.array([2,3,4])

print( a + b )
print( a * b )
print( a % b )

#%%

arr = np.array([10,20,30])

print(arr > 10)

#%%
arr = np.array([10,20,30])

print(arr[[False,True,True]])


#%%

arr = np.array([10,20,30])
cond = arr > 10 

print(arr[cond])

print(arr[arr>10])

#%%

arr = np.array([10,20,30])

cond = arr > 10 

arr[cond] = 1  # [10, 1,1]
arr[~cond] = 0  # [0,1,1]

print(arr)

#%%
arr = np.array([10,20,30])

arr = np.where(arr > 10, 1, 0)

print(arr)

#%%
arr = np.array([10,20,30])
cond = arr >  10 
arr[cond] = arr[cond] + 10 
arr[~cond] = arr[~cond] - 10
print(arr)

#%%
arr = np.array([10,20,30])
arr = np.where( arr>10 , arr+10 , arr-10 ) 
print(arr)

#%%

lge = np.array([93000, 82400,99100, 81000,72300])

result = lge[ lge <= 85000]

print(result)








































