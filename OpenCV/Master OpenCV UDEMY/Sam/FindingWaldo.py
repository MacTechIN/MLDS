"""Created on Fri Oct 27 16:21:42 2023
Waldo 를 찾아라 
@author: SamLEE
"""

import cv2
import numpy as np

# Load input image and convert to grayscale

image = cv2.imread('./WaldoBeach.jpg')
cv2.imshow('Where is Waldo?', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load Template image
template = cv2.imread('./waldo.jpg',0)
#Coordinating  
result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#Create Bounding Box
top_left = max_loc #X1,Y1
bottom_right = (top_left[0] + 50, top_left[1] + 50) #X2,Y2
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

#스패이스키를 누르면 다음으로 진행된다. 
cv2.imshow('Where is Waldo?', image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#창이 안닫히면 다시 한번 아래 부분 실행 
cv2.waitKey(1)


# 이코드를 받았고 돌려 봤으면 해야 할일
# WaldoBeach.jpg 에서 그림 일부를 스크린샷 한다음 weldo.jpg를 바꾸워서 실험 해본다.
# rectangle 을 원으로 바꿔본다. (구글링 해..)
# 어떻게 찾아 해는지 자세히 문서화 해본다. 
