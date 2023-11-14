# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:19:45 2023

@author: Solero
"""

# 마우스 이벤트 활용

import cv2
import numpy as np

def draw_rectangle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # 왼쪽 마우스 더블 클릭
        # 사각형 도형 출력
        cv2.rectangle(img, (x,y), (x+50, y+50), (0,0,255), -1) # BGR: Red
        
img = np.zeros((512,512,3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rectangle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
cv2.destroyAllWindows()    