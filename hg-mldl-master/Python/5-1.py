#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 20:21:26 2023
01. 데이터로딩 address : ttps://bit.ly/wine_csv_data' , type: csv . 
02. DF head확인 
03. 데이터 확인 shape info() describ() 
04. feature , target 분리 
05. 학습 셋, 테스트 셋 split () 
06.

@author: sl
"""
import pandas as pd 

wine = pd.read_csv('https://bit.ly/wine_csv_data')

#%% 
# 02. DF head확인 

print(wine.head(5))
print(wine.shape)
# 총 4개의 열로 구성되어 있음. 
# column name : alcohol  sugar    pH  class
#%%
# 03. 데이터 확인
# 3-1 D.F. 구조 

print(wine.shape)
# 0 : red wind , 1 : white wine 

#3-2. 결손값 확인 
wine.info()  

# 3-3. wind데이터 통계
wine.describe() 

#%%
# 04 data, target으로 분리  

data = wine[['alcohol', 'sugar','pH']].to_numpy()
target = wine[['class']].to_numpy() 

#%%
# 05. sklearn.model_selection train_test_split 으로 train, test 데이터 나눔 

from sklearn.model_selection import train_test_split  

train_input, test_input , train_target, test_target = train_test_split(data,target, random_state= 42 )


#%%
# 06 전처리 Standard Scaler 사용 

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()

ss.fit (train_input, train_target)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)
    
#%%
# 07 Logistic Regression 로 훈련 

from sklearn.linear_model import LogisticRegression 

lr = LogisticRegression()

lr.fit(train_scaled,train_target)

print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))

# 0.7859195402298851 과소적합 
# 0.7655384615384615

#%%

# 08 coefficient , interception 확인 

print(lr.coef_, lr.intercept_)
# [[ 0.53273869  1.67940585 -0.7090217 ]] [1.84713933]

#%%

# 09 DecisionTreeClassifier  사용 다시 학습하기 

from sklearn.tree import DecisionTreeClassifier 

dt = DecisionTreeClassifier()

dt.fit(train_scaled, train_target)

print(dt.score(train_scaled, train_target))
print(dt.score(test_scaled,test_target))

# 0.9973316912972086(과대적합)
# 0.8492307692307692

#%%
# 10 plot_tree() 로 그림 출력 하기 

import matplotlib.pyplot as plt 
from sklearn.tree import plot_tree

plt.figure(figsize= (10,7))

plot_tree(dt)
plt.show()

#%%
# 10-1 잘볼수 있게 표시하기  
plt.figure(figsize= (10,7))

plot_tree(dt, max_depth= 1, filled= True, feature_names= ['alcohol','sugar','pH'] )

plt.show()

#%%
# 11 가지치기 
dt = DecisionTreeClassifier(max_depth=3, random_state=42)

dt.fit(train_scaled, train_target)

print(dt.score(train_scaled, train_target))
print(dt.score(test_scaled,test_target))

# 0.8499589490968801
# 0.8363076923076923

#%%

plt.figure(figsize= (20,15))

plot_tree(dt, filled= True, feature_names= ['alcohol','sugar','pH'] )

plt.show()
