import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dx = cv2.Sobel(src, -1, 1, 0) #delta=128)# delta 값을 안주면 디폴트가 0이기때문에 변화하는 것을 보기가 어렵다. 변화하는 상황을 잘 보게끔 하기위해 delta=128로 줌!
dy = cv2.Sobel(src, -1, 0, 1) #delta=128)

cv2.imshow('src', src)
cv2.imshow('dx', dx)
cv2.imshow('dy', dy)
cv2.waitKey()

cv2.destroyAllWindows()
