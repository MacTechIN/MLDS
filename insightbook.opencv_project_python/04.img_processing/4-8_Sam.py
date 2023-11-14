#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 20:12:04 2023

@author: sl
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt 


#이미지를 Gray로 로딩

img = cv2.imread('../img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

#%%
# numpy 연산으로 바이너리 만들기 
threshhold_np = np.zeros_like(img)
threshhold_np[ img > 127] = 255

#%%
# OpenCV 함수로 바이너리 이미지 만들기 

ret, threshhold_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
print(ret) # <127.0> 바이널리 이미지에 사용된 경계 값 반환 

#%%

# 원본과 결과물 출력하기 

# 1.이미지여러개를 딕셔너리호 만든다. 
images = {'Original': img, 'Numpy API':threshhold_np, 'cv2.threshold':threshhold_cv}

#plot로 화면에 출력하기 , 그래프가 아니더라도 Plot 이용하면 표현 가능함. 

for i , (key, value) in enumerate(images.items()):
    plt.subplot(1, 3, i+1) #i 갯수를 enumerate() 는 (0, 값) 반환 인덱스 자동생성 , 코드 줄임, plot 하나씩 늘려감 총 3개 
    plt.title(key) #각각의 제목 불러옴 
    plt.imshow(value, cmap='gray') #plot 의 imshow() 그림을 그래프에 넣어줌 
    plt.xticks([])
    plt.yticks([])
plt.show()
#%%
    
