0#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:35:00 2023

@author: sl
"""

#Pands's DataFrames02: Coditional Filtering

import pandas as pd 

df = pd.read_csv('/Users/sl/Workspace/MLDS/Pandas/python_pandas-master/sample_data/02 Introduction to Pandas/intel.csv')

#%%
Open = df['Open']

# print(type(Open))   # <class 'pandas.core.series.Series'>

#%%

new_open = Open.values

print(type(new_open))  # >> class 'numpy.ndarray'>

# Pandas -> Series -> values is numpy 

#Numpy array 

print(new_open)


#%%
import numpy as np 
# Createing DF from Numpy

new_array = np.arange(0,10).reshape(2,5)
print(new_array)
#%%

df = pd.DataFrame(new_array,columns=['a','b','c','d','e'])
print(df)
