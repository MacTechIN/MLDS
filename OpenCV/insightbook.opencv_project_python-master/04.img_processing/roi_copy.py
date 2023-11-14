import cv2
import numpy as np

img = cv2.imread('../img/sunset.jpg')

x=320; y=150; w=50; h=50
roi = img[y:y+h, x:x+w]     # roi 지정

#img2 = roi.copy()           # roi 배열 복제 ---①

cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0)) # 태양 영역에 사각형 표시
cv2.imshow("img", img)      # 원본 이미지 출력

cv2.waitKey(0)


# 키누르면 태양을 하나더 옆에서 만듬 
img[y:y+h, x+w:x+w+w] = roi # 새로운 좌표에 옆에 roi 추가, 태양 2개 듦
cv2.rectangle(img, (x,y), (x+w+w, y+h), (0,255,0))

cv2.imshow("roi", img)     # roi 만 따로 출력
cv2.waitKey(0)

cv2.destroyAllWindows()
cv2.waitKey(1)
