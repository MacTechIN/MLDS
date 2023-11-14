
import cv2

file_path = '../../images/video8.mp4'

cap = cv2.VideoCapture(file_path)

if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    print("FPS: %f, Delay: %dms" %(fps, delay))

    #무한루프로 비디오 가지고옴(비디오 끝나면 Break
    while True: # 비디오가끝날때 까지 무한 루프
        ret, img = cap.read()
        if ret:
            cv2.imshow('video',img)
            cv2.waitKey(delay) # 25ms 지연 (40 FPS 인경우)
        else:
            break

else:
    print("비디오 파일을 열수 없습니다.")

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)

