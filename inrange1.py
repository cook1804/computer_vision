import sys
import numpy as np
import cv2


# src = cv2.imread('candies.png')    # 밝은 사진
src = cv2.imread('candies2.png')     #어두운 사진

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))    #밝은 사진일때는 RBG가 좋지만 어두운 사진일때는 HSV가 성능이 좋다.
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()
