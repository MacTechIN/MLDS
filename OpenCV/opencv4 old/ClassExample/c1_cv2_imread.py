import cv2

print(cv2.__version__)

# 4.8.1

#%%

img = cv2.imread("../images/img_6_0.png")

cv2.namedWindow("Image") #이름을 가진 윈도우 창 생성
cv2.imshow('Image',img)

cv2.waitKey()
cv2.destroyAllWindows() #열려 있는 모든 윈도우 닫기
