#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:57:35 2023

@author: sl
"""
#%%
# 01 데이터 읽어 오기 

import csv
import matplotlib.pyplot as plt 

f = open('data.csv')
data_py = csv.reader(f)

header = next(data_py)
next(data_py)

aug = []
jan = []

maxtemp = 0.0 
mintemp = 0.0

maxtemp_date = ''
mintemp_date = ''

for row in data_py:
    if row[-1] != '' : 
        if int(row[0].split('-')[1]) == 8:
            aug.append(float(row[-1]))
        if int(row[0].split('-')[1]) == 1:
            jan.append(float(row[-1]))
            
plt.hist(aug, bins= 100, color = 'r')
plt.hist(jan, bins= 100, coloor = 'b')
plt.legend()
plt.show()

