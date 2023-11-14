#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:57:35 2023

@author: sl
"""
#%%
# 01 데이터 읽어 오기 

import csv

f = open('data_all.csv')
data_py = csv.reader(f)

#%%
#Data 화면에 출력하기 
for row in data_py:
    print(row)
    
f.close()




