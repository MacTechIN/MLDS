import cv2
import time

#%%
CAMERA_ID = 0

cam = cv2.VideoCapture(CAMERA_ID)

if cam.isOpened() == False:
    print("can not open the Camera(%d)"%(CAMERA_ID))
    exit()

cv2.namedWindow("CAM_Window")

while(True):
    ret, frame = cam.read()

    now = time.localtime()
    str = "%d. %d. %d. %d:%d:%d" %(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min,now.tm_sec)
    cv2.putText(frame, str, (10,500), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,255))

    cv2.imshow('CAM_Window', frame)

    if cv2.waitKey(10) >= 0:
        break
cam.release()

cv2.destroyAllWindows()
cv2.waitKey(1)