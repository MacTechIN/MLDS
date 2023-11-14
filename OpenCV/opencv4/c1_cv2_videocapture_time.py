# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:52:30 2023

@author: Solero
"""

# 동영상 파일

import cv2
import time

CAMERA_ID = 0

cam = cv2.VideoCapture("./images/video2.mp4")

# cam = cv2.VideoCapture(CAMERA_ID)
if cam.isOpened() == False:
    print('Can not open the(%d)' % (CAMERA_ID) )
    exit()

cv2.namedWindow("CAM_Window") 

while (True):
    ret, frame = cam.read()
    if ret:
        now = time.localtime()
        str = "%d. %d. %d. %d:%d:%d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    
        cv2.putText(frame, str, (0, 50), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 1, (0,0,255))
        cv2.imshow('CAM_Window', frame)
            
        if cv2.waitKey(10) >= 0:
            break
    else:
        break
        
cam.release() # 카메라 해제

cv2.destroyWindow("CAM_Window") # 창 닫기
        