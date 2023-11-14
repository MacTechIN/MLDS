#Video Capture

import cv2

cap = cv2.VideoCapture('../../images/video7.mp4')
#cap = cv2.VideoCapture(0) # default camera

while cap.isOpened():
    success, frame = cap.read()
    if success:
        cv2.imshow('image',frame)

        key = cv2.waitKey(1) & 0xFF

        if(key == 27): # ESC key = 27
            break
    else:
        break
cap.release()
#%%
cv2.destroyAllWindows()
cv2.waitKey(1)
