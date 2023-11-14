#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:05:35 2023

@author: sl
"""

import cv2
import numpy as np
#%%
# Load input image and convert to grayscale

image = cv2.imread('../images/WaldoBeach.jpg')
cv2.imshow('Where is Waldo?', image)
cv2.waitKey(0)
# gray 로 저장 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template = cv2.imread('../images/waldo.jpg',0)
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)

# Min Max Location함수는 최소 포인터, 최대 포인터, 최소 지점, 최대 지점을 반환합니다.
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)


top_left = max_loc
bottom_right = (top_left[0]+ 50, top_left[1]+50)
#%%

cv2.rectangle(image, top_left, bottom_right,(0,0,255), 5)

cv2.imshow('Where is Waldo?', image)

cv2.waitKey(0)
cv2.destroyAllWindows()


#%%

print(f"min_val : max_val = ({min_val} : {max_val})") 
print(f"min_loc : max_loc = ({min_loc} : {max_loc})") 

# min_loc 은 tuple x,y 로 구성되어 있다. 
print(f"x1:({min_loc[0]}) ,  y1 :({max_loc[1]})") 


#%%
cv2.destroyAllWindows()
cv2.waitKey(1)
