
import cv2



cap = cv2.VideoCapture(0) # 0 : 내장 비디오 카메라

if cap.isOpened():
    file_path = './video_record.avi'
    fps = 25.40
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))
    out = cv2.VideoWriter(file_path, fourcc, fps, size)

    #무한루프로 비디오 가지고옴(비디오 끝나면 Break
    while True: # 비디오가끝날때 까지 무한 루프
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recording',frame)
            out.write(frame)
            if cv2.waitKey(int(1000/fps)) !=- 1:
                break
        else:
            print("프레임 에러!!!")
            break
    out.release()
else:
    print("카메라 연결에 문제가  있습니다.")
cap.release()
cv2.destroyAllWindows()
cv2.waitKey(1)

