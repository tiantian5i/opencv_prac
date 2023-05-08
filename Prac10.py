import cv2
import numpy as np


def cv_show(img, name):
    cv2.imshow(name, img)
    cv2.waitKey()
    cv2.destroyAllWindows()


img = cv2.imread("Images/R3.jpg", cv2.IMREAD_GRAYSCALE)

# sobel 源 图像深度，此处位数更多，可带负值； 水平 竖直 sobel算子大小
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # 负数被截断为0
sobelX = cv2.convertScaleAbs(sobelX)

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # 负数被截断为0
sobelY = cv2.convertScaleAbs(sobelY)

sobelXY = cv2.addWeighted(sobelX, 0.5, sobelY, 0.5, 0)

cv_show(sobelX, "sobelX")
cv_show(sobelY, "sobelY")
cv_show(sobelXY, "sobelXY")
