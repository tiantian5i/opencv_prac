import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Images/R.jpg')

# 100,100的像素值,向量
px = img[100, 100]
print(px)       # BGR

# 100,100的像素值,单个
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
plt.imshow(img, cmap='gray', interpolation='bicubic')   # plt默认RGB
plt.xticks([]), plt.yticks([])
plt.show()




top_size, bottom_size, left_size, right_size = (50, 50, 50, 50)
replicate = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, borderType=cv.BORDER_REPLICATE)    # 复制最边缘像素
reflect = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, top_size, bottom_size,left_size, right_size, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img, top_size, bottom_size, left_size, right_size, cv.BORDER_CONSTANT, value=0)        # 常数值填充，此处0为黑边

plt.subplot(231), plt.imshow(img, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt. title('CONSTANT')
plt.show()

