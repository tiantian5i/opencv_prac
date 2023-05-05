import numpy as np
import cv2

img = cv2.imread('Images/R.jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('Rgray.png', img)   # 写入一个新文件
    cv2.destroyAllWindows()
