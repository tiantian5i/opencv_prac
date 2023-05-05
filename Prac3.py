import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Images/R.jpg')

# 100，100的像素值，向量
px = img[100, 100]
print(px)       # BGR

# 100，100的像素值，单个
blue = img[100, 100, 0]
green = img[100, 100, 1]
red = img[100, 100, 2]
print(blue)
print(green)
print(red)
# print(img)

img[100, 100] = [255, 255, 255]     # 修饰[100,100]的单个像素
print(img[100, 100])

# accessing RED value
# img.item(100, 100, 2)

# modifying RED value
# img.itemset((100, 100, 2), 255)
# img.item(100, 100, 2)

# img.shape      # (row, colum, channel)
# img.size       # row * colum * channel
# img.dtype      # 位数 一般是uint8,256个数： 0~255

for j in range(100):
    for i in range(800):
     img.itemset((100 + j, 100 + i, 2), 0)    # R
     img.itemset((100 + j, 100 + i, 0), 0)    # B
     img.itemset((100 + j, 100 + i, 1), 255)    # G

top_left_corner = img[0:200, 0:200]     # 截取左上角图片200*200

img_gray = cv.imread('Images/R.jpg', cv.IMREAD_GRAYSCALE)

# img[:, :, 2] = 0      # 红色通道置零

cv.imshow('modify', img)        # 自适应打印图片真实大小
cv.imshow("top_left_corner", top_left_corner)
cv.waitKey(0)
cv.destroyAllWindows()

b, g, r = cv.split(img)         # 分离颜色通道
img = cv.merge((r, g, b))       # 改变颜色通道为RGB
pon='bicubic')   # plt默认RGB
plt.xticks([]), plt.yticks([])lt.imshow(img, cmap='gray', interpolati
plt.show()

plt.subplot(1), plt.imshow(img,)