#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:26:03 2023

@author: sl
"""

#!/usr/bin/env python
# coding: utf-8

# # 1. 환경 설정

# In[1]:


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


# # 2. 데이터셋 준비

# In[2]:


# IMDb 영화 리뷰 데이터셋
from tensorflow.keras import datasets
imdb = datasets.imdb
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=10000, index_from=3)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape) 

#%%
print(X_train[0])
print(len(X_train[0]))


#%%
word_index = imdb.get_word_index()
word_index['zeon']

#%%
# def decode_review_vector(review_vector): 분해 
review_vector = X_train[0]

"""
# 숫자 벡터를 텍스트로 변환
def decode_review_vector(review_vector):
    index_to_word = {value:key for key, value in word_index.items()}
    index_to_word 
    index_to_word = {value:key for key, value in word_index.items()}
    
    decoded_review = ' '.join([index_to_word.get(idx - 3, '?') for idx in review_vector])
    return decoded_review
"""

index_to_word = {value:key for key, value in word_index.items()} 
q = index_to_word.get(1-3, '?')
print(q)

# 인덱스로 디코딩 된 데이터에서 인덱스 값을 꺼냄 
# 인덱스 - 3 을 하여 그 값으로 키와 dict {인덱스 : 단어}에서 단어를 추출 해 핸다. 
# 리스트에서 각 단어를 하나씩 꺼내 공백 을 넣어 문자열로 구성 
# 결과 영화 리뷰 데이터로 복원 
# 문장에 맨 처음은 ? 가 시작 부호로 ㅊ

decoded_review = ' '.join([index_to_word.get(idx - 3, '?') for idx in review_vector])

print(decoded_review)

# 첫번째 리뷰 디코딩
#decode_review_vector(X_train[0])
#%%
# 숫자 벡터를 텍스트로 변환
def decode_review_vector(review_vector):
    # {단어:인덱스} -> {인덱스:단어} 로 교체 
    index_to_word = {value:key for key, value in word_index.items()}
    #키가 없는 경우 ? 처리 
    decoded_review = ' '.join([index_to_word.get(idx - 3, '?') for idx in review_vector])
    return decoded_review

# 첫번째 리뷰 디코딩
decode_review_vector(X_train[0])

#%%
y_train[0]


#%%
# 각 리뷰의 단어 개수 분포
review_length = [len(review) for review in X_train]
sns.displot(review_length);


#%%
print(review_length)


#%%

# Padding
from tensorflow.keras.preprocessing import sequence
X_train_pad = sequence.pad_sequences(X_train, maxlen=250)
X_test_pad = sequence.pad_sequences(X_test, maxlen=250)

print(X_train_pad[0])  #250 -218  = 32 

#%%# 모델 정의
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import Embedding, SimpleRNN, LSTM, GRU

def build_model(model_type='RNN'):
    model = Sequential()
    # Embedding
    model.add(Embedding(input_dim=10000, output_dim=128))
    
    # RNN
    if model_type=='RNN':
        model.add(SimpleRNN(units=64, return_sequences=True)) # 층하나더 추가 
        model.add(SimpleRNN(units=64)) 
    # LSTM
    elif model_type=='LSTM':
        model.add(LSTM(units=64, return_sequences=True)) 
        model.add(LSTM(units=64)) 
    # GRU
    elif model_type=='GRU':
        model.add(GRU(units=64, return_sequences=True)) 
        model.add(GRU(units=64))    

    # Dense Classifier
    model.add(Dense(units=32, activation='relu'))
    model.add(Dropout(rate=0.5))
    model.add(Dense(units=1, activation='sigmoid'))

    # Compile
    model.compile(optimizer='adam', 
                loss='binary_crossentropy', 
                metrics=['accuracy'])

    return model

#%%

rnn_model = build_model('RNN')
rnn_model.summary()

""" Summery 출력 
 Layer (type)                Output Shape              Param #   
=================================================================
 embedding (Embedding)       (None, None, 128)         1280000    
 
1280000  =  10000(((input_dim=10000) * 128 (output_dim=128) 
                                                                 
 simple_rnn (SimpleRNN)      (None, None, 64)          12352     
  
12352  = 128 * 64+ 64*64 + 64 
                                                               
 simple_rnn_1 (SimpleRNN)    (None, 64)                8256  

    8256   = (64*64)+64
    
                                                                 
 dense (Dense)               (None, 32)                2080      
                                                                 
 dropout (Dropout)           (None, 32)                0         
                                                                 
 dense_1 (Dense)             (None, 1)                 33        
                                                                 
=================================================================
Total params: 1302721 (4.97 MB)
Trainable params: 1302721 (4.97 MB)   = 1280000 + 12352 + 8256 + 200+ 33 
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________
"""


#%%
rnn_history = rnn_model.fit(X_train_pad, y_train, batch_size=32, epochs=10,
                        validation_split=0.1, verbose=2) 

#%%
# 20 epoch 까지 손실함수와 정확도를 그래프로 나타내는 함수

def plot_metrics(history, start=1, end=20):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    # Loss: 손실 함수
    axes[0].plot(range(start, end+1), history.history['loss'][start-1:end], 
                label='Train')
    axes[0].plot(range(start, end+1), history.history['val_loss'][start-1:end], 
                label='Validation')
    axes[0].set_title('Loss')
    axes[0].legend()
    # Accuraccy: 예측 정확도
    axes[1].plot(range(start, end+1), history.history['accuracy'][start-1:end], 
                label='Train')
    axes[1].plot(range(start, end+1), history.history['val_accuracy'][start-1:end], 
                label='Validation')
    axes[1].set_title('Accuracy')
    axes[1].legend()
plt.show()

# 그래프 그리기
plot_metrics(history=rnn_history, start=1, end=10)    


#%%

# LSTM 모델 적용
lstm_model = build_model('LSTM')

lstm_history = lstm_model.fit(X_train_pad, y_train, batch_size=32, epochs=10,
                        validation_split=0.1, verbose=0) 

plot_metrics(history=lstm_history, start=1, end=10)   
