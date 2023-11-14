#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 12:57:35 2023

@author: sl
"""
#%%
# 01 데이터 읽어 오기 

import csv

f = open('data.csv')
data_py = csv.reader(f)

#%%
#Data 화면에 출력하기 
for row in data_py:
    print(row)
    


#%%
import matplotlib.pyplot as plt 

plt.title("plotting")
plt.plot([10,20,30,40],color= 'skyblue', label = 'asc')
plt.plot([40,30,20,10],color= 'pink', label = 'desc')
plt.legend(loc=6)
plt.show()

#%%

f = open('data.csv')
data_py = csv.reader(f)

next(data_py)
result = []
for row in data_py:
    if row[-1] =='':
        row[-1] = 0
    result.append(float(row[-1]))
    
print(len(result))

plt.figure(figsize = (10,2))
plt.plot (result , 'r')

plt.show()
#%%
#aosus 2/14 최고 기온 데이터 추출 하기 

result = []

for row in data_py:
    if row[-1] !=''and row[-2] != '':
        if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14':
                result.append(float(row[-1]))
    
print(len(result))

plt.figure(figsize = (10,2))
plt.plot (result , '')

plt.show()
#%%
#연도에 '/t' 제거 하기 

# 01 데이터 읽어 오기 
import csv
import matplotlib.pyplot as plt 

f = open('data.csv')

data = csv.reader(f)
next(data)
high = []
low = []

print(data)

#%%
for row in data: 
    if row [-1] != '' and row[-2] != '':
        if int(row[0].split('-')[0]) >= 1983:
            if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14':
                high.append(float(row[-1]))
                low.append(float(row[-2]))
            
        
plt.plot(high, 'hotpink')
plt.plot(low, 'skyblue')

plt.show()

#%%

f.clo