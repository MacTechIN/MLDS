# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:03:08 2023

@author: Solero
"""

# filename : c1_cv2_imread.py

import cv2 

print(cv2.__version__) # 4.8.1

#%%
img = cv2.imread("./images/img_6_0.png") # 그림 읽기

cv2.namedWindow("image") # 이름을 가진 윈도우 생성
cv2.imshow("image", img)

cv2.waitKey()

cv2.destroyAllWindows() # 열려있는 모두 윈도우 닫음