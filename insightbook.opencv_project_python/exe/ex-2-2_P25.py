import cv2

img_file = '../../images/img1.jpg'
# Gray Scale 로 익어오기
img = cv2.imread(img_file,cv2.IMREAD_GRAYSCALE)

# Error checking for  exception
if img is not None:
    cv2.imshow("image", img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.waitKey(1)

else:
    print("Image loaing error !!")

