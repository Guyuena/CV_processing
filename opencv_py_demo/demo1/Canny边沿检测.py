import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# edge = cv2.Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient ]]])
#   参数 image - 输入图片，必须为单通道的灰度图
#   参数 threshold1 和 threshold2 - 分别对应于阈值 minVal 和 maxVal
#   参数 apertureSize - 用于计算图片提取的 Sobel kernel 尺寸. 默认为 3.
#   参数 L2gradient - 指定计算梯度的等式. 当参数为 True 时，采用 梯度计算公式(3)(4)，其精度更高；否则采用的梯度计算公式为：G = G_x + G_y



def ff():
    img = cv.imread('Fig/shi2.png', 0)
    # 第一个参数是我们的输入图像。第二个和第三个参数分别是我们的minVal和maxVal
    edges = cv.Canny(img,100,200)
    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()

"""
    基于Canny算子的边缘检测主要有5个步骤，依次是高斯滤波、像素梯度计算、非极大值抑制、滞后阈值处理和孤立弱边缘抑制。
    1. 应用高斯滤波来平滑(模糊)图像，目的是去除噪声
    2. 计算梯度强度和方向
    3. 应用非最大抑制技术NMS来消除边误检
    4. 应用双阈值的方法来决定可能的（潜在的）边界
    5. 利用滞后技术来跟踪边界
"""

if __name__ =="__main__":
    ff()