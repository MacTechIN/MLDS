#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:37:00 2023

@author: sl
"""

#%%
# Pandas , Numpy 사용하기 

import pandas as pd 
import numpy as np 

#판다스로 CSV 읽어 오기 

column_name = {'Date','Location','AVE','MIN','MAX'}

data_df = pd.read_csv('data_all.csv')

print(type(data_df))

data_df.head()
data_df.info()

#%%

# Remov '\t' at Data Col Rows 


data_df['Date']= data_df['Date'].str.replace('\t','')

data_df.info()

#%%
data_df['Date'] = pd.to_datetime(data_df['Date'])


data_df.info()

#%%
# Location 에 floate type -> int 변환 

data_df['Location'].value_counts()

data_df.info()


#%%
print(data_df)

#%%
# Make location as 108 int 
data_df['Location'] = data_df['Location'].astype('str')
data_df[['Location']] = "108"
data_df['Location'].value_counts()
data_df['Location'] = data_df['Location'].astype('int')
#%%
#Mean, AVE , MAX 결측값 평균으로 대처하기 

data_df.mean()

data_df.fillna(data_df.mean())
#%%
#결측값 대체 확인하기 
# True 값 : 없음 
data_df.drop(41952, axis = 0, inplace = True )

#%%
data_df.dropna(axis=0)
#%%

data_df.isnull().value_counts()


#%%
#서울에 최고 기온 ? 
# Unit03-01 
# Max데이터 결손값 정리(-999)

Max_temp= data_df[data_df.loc[:,'MAX'] == 39.6]

Max_temp["Date"][40051]

#%%
print(data_df.head())

data_df.to_csv('data.csv', index = False)

