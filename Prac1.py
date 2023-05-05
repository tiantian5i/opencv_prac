import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:\workspace\Yolo_cli\R.jpg", 0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

# print(img)
# cv2.imshow('r', img)
# cv2.waitKey(0)