#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:52:10 2023

Contours¶  정렬 
 
<순서>

01. 이미지 로드 
02. 로드한 image 그레이 로 변환시키기 
03. 엣지 찾기  


@author: sl
"""

import cv2
import numpy as np

#%%
# 1.shapes.jpg이미지를 image에 로드하기 
image = cv2.imread('./images/shapes.jpg')
cv2.imshow('Input Image', image)
cv2.waitKey(0)

#%%
# 2.로드한 image 그레이 로 변환시키기
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#%%
# 3.엣지 찾기 
# Canny : 엣지 검출 함수, Return :엣지이미지,  
edge = cv2.Canny(gray, 30, 200 )

# 

#%%
# 4. 엣지검출 이미지 확인 
cv2.imshow('edge',edge)
cv2.waitKey(0)

#%%
contours, hierachy = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 


#%%

#%%
cv2.destroyAllWindows()
cv2.waitKey(1)
