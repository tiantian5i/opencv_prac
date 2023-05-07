import cv2
import numpy as np

img = cv2.imread("Images/R3.jpg")
cv2.imshow('img', img)
cv2.waitKey()
# cv2.destroyAllWindows()

# 腐蚀
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)      # 迭代次数
# cv2.imshow('erosion', erosion)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 膨胀
dilation = cv2.dilate(img, kernel, iterations=1)      # 迭代次数

# 开运算：先腐蚀，再膨胀
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# 闭运算：先膨胀，再腐蚀
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# 梯度运算=膨胀-腐蚀
gardient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('gardient', gardient)
cv2.waitKey()

# 礼帽 原始输入-开运算结果
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow('tophat', tophat)
cv2.waitKey()

# 黑帽 闭运算-原始输入
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('blackhat', blackhat)
cv2.waitKey()


# 显示
res = np.hstack((erosion, dilation, opening, closing))
cv2.imshow("combination", res)
cv2.waitKey()
cv2.destroyAllWindows
