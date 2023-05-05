import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Images/R2.jpg')
b, g, r = cv2.split(img)         # 分离颜色通道
img = cv2.merge((r, g, b))       # 改变颜色通道为RGB

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)      # src，阈值，最大值，模式 超阈值的置零
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)       # 截断：超阈值的设置为阈值，其他不变
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)      # 暗部更暗：超阈值的不变，没有超阈值的置零
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)  # 上一步的反转，暗部变亮，亮部变暗：超阈值的置零，没有超阈值的不变

titles = ['original Image', 'BINARY' , 'BINARY INV', 'TRUNC', 'TOZERO', 'T0ZERO_INV' ]
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt. subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt. title(titles[i])
    plt. xticks([]), plt.yticks([])
plt. show()
