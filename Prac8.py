import cv2
import numpy as np

lena_noise = cv2.imread("Images/lenanoise.png")

# 均值滤波
lena_blur = cv2.blur(lena_noise, (3, 3))        # 图像 卷积核大小，全为1  均值滤波，平均卷积操作

# 方框滤波   True，均值化就是均值滤波，false：＞255，保持不变；-1，输入输出表示颜色通道一致
lena_box = cv2.boxFilter(lena_noise, -1, (3, 3), normalize=False)

# 高斯滤波   卷积核中心权重最高，周围数字按高斯分布递减
lena_Gaus_r11 = cv2.GaussianBlur(lena_noise, (11, 11), 0, 0)  # 图像  卷积核大小   x方向的方差  y方向的方差
lena_Gaus_r5 = cv2.GaussianBlur(lena_noise, (5, 5), 0, 0)      # 需要注意卷积核大小必须为奇数

# 中值滤波    卷积核选中的数字中，取中位数输出
lena_median = cv2.medianBlur(lena_noise, 5)     # 卷积核 5×5

# 分别显示
cv2.imshow("lena_noise", lena_noise)
cv2.imshow("blur", lena_blur)
cv2.imshow("box", lena_box)
cv2.imshow("Gaus_r11", lena_Gaus_r11)
cv2.imshow("Gaus_r5", lena_Gaus_r5)
cv2.imshow("median", lena_median)
cv2.waitKey()
cv2.destroyAllWindows

# 集中显示 h水平，v垂直
res = np.hstack((lena_blur, lena_box, lena_Gaus_r11, lena_Gaus_r5, lena_median))
cv2.imshow("combination", res)
cv2.waitKey()
cv2.destroyAllWindows
