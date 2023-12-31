# 색상 공간 변환 예제 (c2.cvtColor.py)

# 관련 라이브러리 선언
import numpy as np
import cv2
from imgRead import imgRead
from createFolder import createFolder

# 영상 읽기
img1 = imgRead("./images/img7.jpg", cv2.IMREAD_UNCHANGED, 320, 240)

# 색상 공간 변환
res1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)

# 색상 공간 분할 및 병합
#res1_split = cv2.split(res1)
res1_split = list(cv2.split(res1))
res1_split[2] = cv2.add(res1_split[2], 200)
res1_merge = cv2.merge(res1_split)
res1_merge = cv2.cvtColor(res1_merge, cv2.COLOR_HSV2BGR)

# 결과 영상 출력
displays = [("input1", img1), # Original
            ("res1", res1), # HSV
            ("res2", res1_split[0]), # H
            ("res3", res1_split[1]), # S
            ("res4", res1_split[2]), # V
            ("res5", res1_merge)]  # 밝기가 조정된 BGR
for (name, out) in displays:
    cv2.imshow(name, out)

# 키보드 입력을 기다린 후 모든 영상창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()

#%%
cv2.waitKey(1)

#%%

# 영상 저장
save_dir = './code_res_imgs/c2_cvtColor'
createFolder(save_dir)
for (name, out) in displays:
    cv2.imwrite(save_dir+"/"+name+".jpg", out)
