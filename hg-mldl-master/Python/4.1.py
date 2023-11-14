#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04-1 로지스틱 휘귀 

Created on Mon Oct 23 16:09:15 2023

@author: sl

<전체프로세스>
01. fish.csv 읽어 오기 (판다스)
02.데이터 셋에서 물고기의 종류 7가지 확인
03. 데이터 셋에서 fish_input과  fish_target 을 numpy array로 나눠서 보관 
04. rain_test_split() 
05. input data size 확인
06. 표준화 처리 : standardScaler를 사용 훈련세트의 통계값으로 테스트 세트  변환 (중요!!)
07. K-nearest neighbors classifier 클래스 이용 객체를 만들고 , train_input셋트로 훈련 하고 훈련셋트와 테스트세트의 점수 확인 하기 
08. train set 과 test set scorea 비교하기
09. test_scaled 로 예측 한 결과 확인 하기 

 
#로지스틱 회귀 
이진 부류 문제 클래스 확율을 예측 합니다.


"""

#%%
# 01. fish.csv 읽어 오기 (판다스)

import pandas as pd 

fish = pd.read_csv("https://bit.ly/fish_csv_data")

print(fish.head())
#%%

# 02 데이터 셋에서 물고기의 종류 7가지 확인

print(pd.unique(fish['Species']))

#%%
# 03 데이터 셋에서 fish_input과  fish_target 을 numpy array로 나눠서 보관 

fish_input = fish[['Weight', 'Length',  'Diagonal',   'Height',   'Width']].to_numpy()
fish_target=fish[["Species"]].to_numpy()
#%%

print(fish_input.shape)

print(fish_target.shape)
#
#%%
# 04rain_test_split() 데이터셋 테스트셋 으로 데이터셋 분류 하기 

from sklearn.model_selection import train_test_split

train_input , test_input , train_target, test_target = train_test_split(fish_input, fish_target, random_state= 42 ) 

#%% 05 Input data Size 확인  
print(train_input.shape, train_target.shape)
print(test_input.shape, test_target.shape)

#%% 06 훈련셋트와 테스트 세트 표준화 전처리 
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

#%%
print(train_scaled[:5])
print(test_scaled[:5])
#%%
# K-Nearest Neighbors Classifier 
# 07 K-nearest neighbors classifier 클래스 이용 객체를 만들고 , train_input셋트로 훈련 하고 훈련셋트와 테스트세트의 점수 확인 하기 
from sklearn.neighbors import KNeighborsClassifier

kn = KNeighborsClassifier(n_neighbors= 3)

kn.fit (train_scaled, train_target)

#%% 
#08 rain set 과 test set scorea 비교하기 

print(kn.score(train_scaled, train_target))
print(kn.score(test_scaled, test_target))
#%%
#09 다중분류시 타깃값의 배열 classes_로 확인 
print(kn.classes_) 

# 처음 pd.unique(fish['Species']) 목록과는 다름. ['Bream' 'Roach' 'Whitefish' 'Parkki' 'Perch' 'Pike' 'Smelt']
# 알파벳 순으로 매겨짐 ['Bream' 'Parkki' 'Perch' 'Pike' 'Roach' 'Smelt' 'Whitefish']
#%%
#테스트 예측값 확인 예제 

print(kn.predict(test_scaled[:5]))

#['Perch' 'Smelt' 'Pike' 'Perch' 'Perch']
#%%
#확율 확인 
import numpy as np

proba = kn.predict_proba(test_scaled[:5])

print(np.round(proba, decimals=4))
#%%

distances , indexes = kn.kneighbors(test_scaled[1:2])

print(distances,train_target[indexes])

"""
[[['Roach']
  ['Perch']
  ['Perch']]]
"""

#%%
import numpy as np 
import matplotlib.pyplot as plt 

z = np.arange(-5,5,0.1)
print(z)

#%%
phi = 1 / (1 + np.exp(-z))
#%%
plt.plot(z, phi)
plt.xlabel('z')
plt.ylabel('phi')

plt.show()

#%% 
bream_smelt_indexes = (train_target == "Bream") | (train_target == 'Smelt') 
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]

#%%
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()

lr.fit(train_bream_smelt, target_bream_smelt)




