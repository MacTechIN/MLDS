#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:15:06 2023
시계
LSTM : 
@author: sl
"""

# 라이브러리 설정
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import seaborn as sns
import random

# 랜덤 시드 고정
SEED=12
random.seed(SEED)
np.random.seed(SEED)
tf.random.set_seed(SEED)  


#%%

# 전력거래소 전력거래가격(SMP) 데이터 다운로드 (2018.1.1. ~ 2020.3.31)
# http://epsis.kpx.or.kr/epsisnew/selectEkmaSmpShdChart.do?menuId=040202

#drive_path = "/gdrive/My Drive/"
drive_path = "../../smp/"

smp = pd.read_csv(drive_path + "smp.csv")

# 날짜 데이터를 time series 형식으로 변환
smp['date'] = pd.to_datetime(smp['date'])
# 칼럼추가 : 요일 (0~6) : 0 : 월요일 ~ 6 :일요일 
smp['day_of_week'] = smp['date'].dt.dayofweek

print(smp.shape)   
smp.head()
#%%


# Onehot Encoding
smp['day_of_week'] = smp['day_of_week'].astype('category')

print(smp['day_of_week'])

#%%
smp = pd.get_dummies(smp, columns = ['day_of_week'], prefix='W', drop_first=True)

smp.head()


#%%
fig, axes = plt.subplots(nrows=4,ncols=1, figsize=(20, 20))

print(fig)
print(axes[0])
#%%
axes[0].plot(smp['date'], smp['smp_max'])
axes[0].set_title('smp_max')

axes[1].plot(smp['date'], smp['smp_mean'])
axes[1].set_title('smp_mean')

axes[2].plot(smp['date'], smp['smp_min'])
axes[2].set_title('smp_min')

axes[3].plot(smp['date'], smp['smp_max'], label='smp_max')
axes[3].plot(smp['date'], smp['smp_mean'], label='smp_mean')
axes[3].plot(smp['date'], smp['smp_min'], label='smp_min')
axes[3].set_title('SMP')
axes[3].legend()

plt.show()
#%%
# 3. 모델 학습

# Settings 총 대이터 820개 , 그중 716개 기준으로 Train Input/target 으로 만들기 
# 전체 데이터 : 820건 

train_split_idx = 729   # 2020.1.1. 행 인덱스 번호  
window_size = 10   # 과거 10일 동안의 시계열 데이터를 학습 데이터로 사용
future = 3     # 3일 이후의 타겟을 예측

# Features 
X_test : 716 = 729-10-3 
X_train_len = train_split_idx - window_size - future 
X_train = smp.iloc[:X_train_len, 0:]   
print(X_train_len )
print(len(X_train))

#%%
# Targets
y_train_end =  window_size - future
y_train = smp.iloc[y_train_len :train_split_idx, [3]]  # 'smp_mean' 열

print(X_train.shape, y_train.shape)
#%%
print(X_train)

# 마지막 행 : 715 2019-12-18    88.02    80.62     84.95            2 

#%%

print(y_train.head())



#%%

# X_test
test_start = train_split_idx - window_size - future  # 테스트 데이터의 시작 행  
test_end = smp.shape[0] - window_size - future
X_test = smp.iloc[test_start:test_end, 0:]

# y_test
# label_start =  + future # 테스트 데이터의 첫 번째 타겟 데이터 위치 
y_test = smp.iloc[train_split_idx:, [3]]  # 'smp_mean' 열 선택

print(X_test.shape, y_test.shape)
#%%
X_test.head(15)
#%%
y_test.head(15)
#%%
# date 뺀 나머지 열을 스케일링 해서 0,1 로 표시 하기 위한 전처리 
# 스케일링은  X_train 과 X_test 만 한다. 
 
X_train_scaled = X_train.loc[:, 'smp_max':]
X_test_scaled = X_test.loc[:, 'smp_max':]

from sklearn.preprocessing import MinMaxScaler 

mms = MinMaxScaler()
# X_train.value 값을 먼저 학습해 스케일을 만들고 Transform 을 한다. 
mms.fit(X_train_scaled.values)

X_train_scaled.loc[:,:] = mms.transform(X_train_scaled.values)
X_test_scaled.loc[:,:] = mms.transform(X_test_scaled.values)

#%%

# Mini Batch 크기로 시계열을 변환
from tensorflow.keras.preprocessing import timeseries_dataset_from_array

train_data = timeseries_dataset_from_array( 
    X_train_scaled, y_train, sequence_length=window_size, batch_size=16)
test_data = timeseries_dataset_from_array( 
    X_test_scaled, y_test, sequence_length=window_size, batch_size=16)

print(train_data)
print(test_data)

#%%
for batch in test_data.take(1):
    inputs, targets = batch

print("Input:", inputs.numpy().shape)
print("Target:", targets.numpy().shape)

#%%

inputs[0]

#%%
targets[0]

# 81.46

#%%

