import numpy as np
import cv2

#%%

img = cv2.imread('../../images/img_6_0.png')
print(img.shape)

height = img.shape[0]
width = img.shape[1]
rgb = img.shape[2]

print('height :', height)
print('width :', width)
print('RGB :', rgb)


for y in range(0, height):
    img.itemset(y, int(width/2), 0, 0 )
    img.itemset(y, int(width / 2), 1, 0)
    img.itemset(y, int(width / 2), 2, 255)

for x in range(0, width):
    img.itemset(int(height/2), x, 0, 255)
    img.itemset(int(height/2), x, 1, 0)
    img.itemset(int(height/2), x, 2, 0)

cv2.namedWindow("image")
cv2.imshow('image', img)

cv2.waitKey(1)
cv2.destroyAllWindows()
