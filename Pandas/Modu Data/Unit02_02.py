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

header = next(data_py)

print(header)

f.close() 

#%%
#서울에 최고 기온은 언제 ?
# Unit03-01 
# Max데이터 결손값 정리(-999)

max_temp = -999
max_data = ''

f = open('data_all.csv')
data_py = csv.reader(f)
header = next(data_py)
for row in data_py :
    if row[-1] == '':
        row[-1] = -999
    row[-1] = float(row[-1])
    if(max_temp < row[-1]):
        max_data = row[0]
        max_temp = row[-1]
f.close()

print("최고 기온 : ", max_temp, ' @날짜 :', max_data)
#%%