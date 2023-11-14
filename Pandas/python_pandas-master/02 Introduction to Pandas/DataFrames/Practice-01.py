0#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 23:35:00 2023

@author: sl
"""

#Pands's DataFrames 

import pandas as pd 

df = pd.read_csv('./sample_data/02 Introduction to Pandas.csv')

#How to check df shape 
print(df.shape)

print(df.columns)

#%%

# Inspec forst rows in data frame
print(df.head(2))

# Inspect last rows of data frame 
print(df.tail(2))


#%%
print(df.info())
#%%
open = df['Open']

print(open.head())
#%%

# View one or more columns side by side
print(df[["Open","Close"]].head())


#%%
print(df.describe())

#%%

print(df['Open'].min())

print(df["Open"].mean())