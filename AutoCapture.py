# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import time 
from PIL import ImageGrab
from PIL import ImageEnhance 
import pyautogui
 
sharpness_level = 2.2

def screenshot (wait_time , interval_time, page_number):
    time.sleep(wait_time)
    pyautogui.click(x=1684,y=577)
    
    for  i in range(page_number):
        current_time = time.strftime('%Y%m%d$H%M%S')
        time.sleep(interval_time)
    
        img = ImageGrab.grab((445,40,1280,1115))
        enhancer = ImageEnhance.Sharpness(img)
        
        sharpened_img = enhancer.enhance(sharpness_level)
        
        file_path = r'./capture/'
        sharpened_img.save(f'{file_path}img_{current_time}.png')
        print(f'{i}이미지 저장완료')
        time.sleep(interval_time/2)
        pyautogui.click(x=1684,y=577)
        


   
#%%
screenshot(2, 1, 1)
    
#%%    
pyautogui.click(x=1684,y=577) #수원사이버도서관
img = ImageGrab.grab((469,45,1260,1115))

pyautogui.click(x=1207,y=1086) #교보
