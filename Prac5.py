import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img_birds = cv.imread('Images/R1.jpg')
img_cars = cv.imread('Images/R2.jpg')
print(img_birds.shape)
print(img_cars.shape)
img_cars = cv.resize(img_cars, (700, 467)) # 变换图像尺寸

img_birds_2 = img_birds + 15
# print(img_birds_2)

cv.imshow('img_birds_2', img_birds_2)
cv.waitKey(0)

# 相当于%256，超界限重新开始
cv.imshow('array add', img_birds + img_cars)
cv.waitKey(0)

# 超界限封顶255，不变
cv.imshow('cv.add', cv.add(img_birds, img_cars))
cv.waitKey(0)

# 带权重的cv.add，ax+by+c
res = cv.addWeighted(img_cars, 0.9, img_cars, 0.6, 0)
cv.imshow('cv.addWeighted', res)
cv.waitKey(0)