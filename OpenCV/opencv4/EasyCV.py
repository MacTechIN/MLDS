#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 10:07:14 2023

@author: sl
"""

import cv2
import pandas as pd
import numpy as np 

FONT_FACE = cv2.FONT_HERSHEY_COMPLEX
FONT_COLOR = (0,0,255)
DEFAULT_NAME = "Image"

# 날짜출력하기 
from datetime import datetime as dt

# 현재시간 얻기
def getTimeAndDate():
    displayFormat = '%Y-%m-%d %H:%M:%S'
    currentDateAndTime = dt.now().strftime(displayFormat)    
    return currentDateAndTime

#문자열 출력 
def displayText(image, inputStr):
    height, width, channel = image.shape
    x1 = int(width - (width-10))  
    y1 = int(height - (height-20))
    cv2.putText(image, inputStr, (x1,y1), FONT_FACE, 0.5, FONT_COLOR)


def displayTextXY(image, x,y, inputStr):
        cv2.putText(image, inputStr, (x,y), FONT_FACE, 0.5, FONT_COLOR)

def displayDateAndTime(image):
    dateAndTime = getTimeAndDate()    
    displayText(image, dateAndTime)
    
# ===== 이미지 프로세싱 관련 함수 === #
#ROI 설정하기 

def setROI(img, x,y,h,w):
    roi = img[y:y+h, x:x+w]
    return roi
    
    
# <이미지 관련>

# 이미지 로딩 
def imageScaleRead(imgPath, imgReadType, imgResWidth, imgResHeight):
    img = cv2.imread(imgPath, imgReadType)
    if imgResHeight != 0 | imgResWidth != 0:
        img = cv2.resize(img, (imgResWidth, imgResHeight))
    
    return img

def imageReadByOriginalSize(imgPath, imgReadType):
    img = cv2.imread(imgPath,imgReadType)

    return img

# 얼굴검색 함수 
def detectFaceCordination(img):
    grayConvertedSrc = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
    detectedFacesOri = face_cascade.detectMultiScale(grayConvertedSrc,scaleFactor= 1.1, minNeighbors= 5,  minSize=(10,10)) 
    return detectedFacesOri


    
    return detectedFacesOri

# 사각형그림 
def showRectOnImage(img,cord):
    for x, y, w, h in cord:
        cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0),thickness= 2)

#얼굴찾고 눈찾기 
def showRectForFaceAndEyes(img,cord):
    eyes_cascade = cv2.CascadeClassifier('./models/haarcascade_eye.xml')
    for x, y, w, h in cord:
        cv2.rectangle(img, (x,y), (x+w, y+h),(0,255,0),thickness= 2)
        faceROI = setROI(img,x,y,h,w)
        eyes = eyes_cascade.detectMultiScale(faceROI)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(img[y:y+y, x:x+w],(ex,ey) ,(ex+ew, ey+eh),(255,0,0), 2)
        

# 사각형아래 문자열 삽입하기           
def showFaceTextOnImage(img, cord, inputStr,color):
    i = 0 
    for x, y, w, h in cord:
        i = i + 1 
        #cv2.rectangle(img, (x,y), (x+w, y+h),color,thickness= 2)
        faceNumber = inputStr + str(i)
        displayTextXY(img, (x-5), (y+h+18), faceNumber)
        
def showImage(windowTitle, img):
    cv2.imshow(windowTitle, img)
    cv2.waitKey(0)
    cv2.destroyWindow(windowTitle)
    cv2.waitKey(1) 

# 동영상 파일 열기 
def loadVideo(filePath):
    videoFile = filePath 
    videoCapture = cv2.VideoCapture(videoFile)
    return videoCapture

def playVideo(cap):
    while cap.isOpened():
        success, frame = cap.read()
        if success:
            displayDateAndTime(frame)
            
            cv2.imshow('image', frame)
            key = cv2.waitKey(1) & 0xFF
            if(key == 27):
                break 
        else:
            break 
    cap.release()
    
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    cv2.waitKey(1)

def detectFaceOnTheVideo(cap, needRecord):
    if cap.isOpened():
        if needRecord == True:
            file_path = './record.avi'
            fps = 25.40
            width =  cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            size = (int(width)* int(height))
            # 이부분 부터 작업 다시 해야함. 
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(file_path, fourcc, fps, size)
        while True : 
            success, frame = cap.read()
            if success:
                displayDateAndTime(frame)
                detectedFaceCord = detectFaceCordination(frame)
                showRectForFaceAndEyes(frame, detectedFaceCord)
                showFaceTextOnImage(frame, detectedFaceCord,"face",(0,255,0))
            
                cv2.imshow('image', frame)
                key = cv2.waitKey(1) & 0xFF
                if(key == 27):
                    break 
                else:
                    break
            out.release()
    else:
        cap.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    cv2.waitKey(1)
    

       
#%%
# Face Detect TEST

imagePath = './images/img_6_6.jpg'

imageSource = imageReadByOriginalSize(imagePath,cv2.IMREAD_COLOR)
detectedFaceCord = detectFaceCordination(imageSource)
showFaceTextOnImage(imageSource, detectedFaceCord,"face",(0,255,0) )

displayDateAndTime(imageSource)

showImage('Result', imageSource)

#%%

# Face and eyes Detect TEST

imagePath = './images/children.jpg'

imageSource = imageReadByOriginalSize(imagePath,cv2.IMREAD_COLOR)
detectedFaceCord = detectFaceCordination(imageSource)
showRectForFaceAndEyes(imageSource,detectedFaceCord)
showFaceTextOnImage(imageSource, detectedFaceCord,"face",(0,255,0) )
displayDateAndTime(imageSource)

showImage('Result', imageSource)

#%%
videoPath = './images/video2.mp4'

cap =loadVideo(videoPath)
playVideo(cap) 
#%%

cv2.destroyAllWindows('image') 
cv2.waitKey(1)
#%%
# Face Detect Test on Video 1

videoPath = './images/head-pose-face-detection-female.mp4'

cap =loadVideo(videoPath)
detectFaceOnTheVideo(cap)


#%%

# Face Detect Test on Video 2

videoPath = './images/head-pose-face-detection-female-and-male.mp4'
            
cap =loadVideo(videoPath)
detectFaceOnTheVideo(cap, True)

#%%
