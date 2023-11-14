#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 15:15:52 2023
4-2 확률적 경사 하강법 

1. 데이터 준비 
2. Species 열을 제외한 나머지 열Col을 입력데이터로 , Species 열 은 타깃 데이터로 분류 후 Numpy 화 시킴 
3. train_test_spelit 사이킷 런 함수 하용 훈련세트와 테스트 세트로 나눔 
4. 입력값을 StandardScaler 표준화 전처리.


@author: sl
"""

#%%
# 1. 데이터 준비 

import pandas as pd 
fish = pd.read_csv('https://bit.ly/fish_csv_data')

#%%

fish['Species'].value_counts() 

#%%
# 2. Species 열을 제외한 나머지 열Col을 입력데이터로 , Species 열 은 타깃 데이터로 분류 후 Numpy 화 시킴 

fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()

fish_target = fish[['Species']].to_numpy() 
#%%
# 3. train_test_spelit 사이킷 런 함수 하용 훈련세트와 테스트 세트로 나눔 

from sklearn.model_selection import train_test_split

train_input,test_input, train_target, test_target = train_test_split(fish_input , fish_target, random_state= 42)
#%%

# 4. 입력값을 StandardScaler 표준화 전처리 

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

sc.fit(train_input) 

train_scaled = sc.transform(train_input)
test_scaled = sc.transform(test_input)
 
#%%

 # 5. 학습 1 : 확율적 경사 하강법 대표 클래스:sklearn.linear_model 패키지 안에 SGDClassifier 를 
 # 옵션 : loss='log', max_iter= 10, random_state=42 를 사용 학습 시킨다.

from sklearn.linear_model import SGDClassifier 

sc = SGDClassifier(loss='log_loss', max_iter= 10, random_state=42)

sc.fit(train_scaled,train_target)
#%%
#5-1 학습 검증 

print(sc.score(train_scaled, train_target)) 
print(sc.score(test_scaled,test_target)) 

# 0.7310924369747899
# 0.75

#0.8151260504201681
#0.8

#%%

# 6. 정확도가 너무 낮음. 점진적 학습을위해 SGDClassifier 대신 partial_fit()으로 보강학습을 시킨다.

sc.partial_fit(train_scaled, train_target)

#%%
print(sc.score(train_scaled, train_target)) 
print(sc.score(test_scaled,test_target)) 

# 0.8067226890756303
# 0.8

#%%
# 300번 훈련 을 나는 score를 train_score, test_score 리스트로 만들어 그래프로 만들기  
import numpy as np 

sc = SGDClassifier(loss='log', random_state= 42 )
train_score = []
test_score = [] 

classes = np.unique(train_target)

for _ in range(0, 300):
    sc.partial_fit(train_scaled , train_target , classes= classes)
    train_score.append(sc.score(train_scaled,train_target))
    test_score.append(sc.score(test_scaled, test_target))
#%%
# 7. 훈련 그래프 생성 
import matplotlib.pyplot as plt 

plt.plot(train_score)
plt.plot(test_score)

plt.show() 
#%%
# 8. 그래프를 분석해보면 100 훈련이 적합한 데이터를 만든다는 것을 확인 하였고, 
# SGDClassifier 에 max_iter = 100으로 다시 훈련 하고 검검증 한다.

sc = SGDClassifier(loss='hinge', max_iter=100, tol=None, random_state=42)

sc.fit(train_scaled, train_target)
#%%
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

# 0.9495798319327731
# 0.925

#%%























 
