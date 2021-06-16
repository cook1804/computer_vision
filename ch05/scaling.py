import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt


src = cv2.imread('rose.bmp') # src.shape=(320, 480)

if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)  #INTER_NEAREST
dst2 = cv2.resize(src, (1920, 1280))                                         #cv2.INTER_LINEAR(default)
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)          #INTER_CUBIC
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)       #INTER_LANCZOS4
 



plt.subplot(231), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('dst1')
plt.subplot(232), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('dst2')
plt.subplot(233), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('dst3')
plt.subplot(234), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('dst4')
plt.show()
# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1[500:900, 400:800])
# cv2.imshow('dst2', dst2[500:900, 400:800])
# cv2.imshow('dst3', dst3[500:900, 400:800])s
# cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()
