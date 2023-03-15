

# OpenCv 提供三种类型的梯度滤波器或高通滤波器，Sobel、Scharr 和 Laplacian

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Sobel(src, ddepth, dx, dy, dst=None, ksize=None, scale=None, delta=None, borderType=None)
#   dst 代表目标图像。
#   src 代表原始图像。
#   ddepth 代表输出图像的深度。
#   dx 代表 x 方向上的求导阶数。
#   dy 代表 y 方向上的求导阶数。
#   ksize 代表 Sobel 核的大小。该值为-1 时，则会使用 Scharr 算子进行运算。
#   scale 代表计算导数值时所采用的缩放因子，默认情况下该值是 1，是没有缩放的。
#   delta 代表加在目标图像 dst 上的值，该值是可选的，默认为 0。
#   borderType 代表边界样式。



def ff1():
    img = cv.imread('Fig/img2.png', 0)
    laplacian = cv.Laplacian(img,cv.CV_64F)
    sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5) # cv2.Sobel()获取图像水平方向的完整边缘信息。
    sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5) # cv2.Sobel()获取图像垂直方向的边缘信息。
    plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    plt.show()

"""

    上一个示例中，输出数据类型是 cv.CV_8U或 np.uint8。但这有一个小问题。
    黑白过渡为正斜率（有正值），而白黑过渡为负斜率（有负值）。所以当你把数据转换成 np.uint8 时，
    所有的负斜率都变成零。简单来说，你失去了边缘。
    如果要检测两条边，更好的选择是将输出数据类型保留为更高的格式，如 cv.CV_16S、cv.CV_64F 等，取其绝对值，然后转换回 cv.CV_8U
"""

# 计算函数 cv2.Sobel()在水平、垂直两个方向叠加的边缘信息。
def ff2():
    o = cv.imread('Fig/img3.png', cv.IMREAD_GRAYSCALE)
    sobelx = cv.Sobel(o, cv.CV_64F, 1, 0) # 获取图像水平方向的边缘信息。
    sobely = cv.Sobel(o, cv.CV_64F, 0, 1) # 获取图像垂直方向的边缘信息。
    sobelx = cv.convertScaleAbs(sobelx)  # 转回uint8
    sobely = cv.convertScaleAbs(sobely)  # convertScaleAbs()函数计算绝对值，并将图像转换为8位图进行显示
    sobelxy = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0) # cv2.Sobel()在水平、垂直两个方向叠加的边缘信息。
    # cv.imshow("original", o)
    cv.imshow("x方向求梯度", sobelx)
    cv.imshow("y方向求梯度", sobely)
    cv.imshow("xy方向梯度", sobelxy)
    cv.waitKey()
    cv.destroyAllWindows()


# scharr滤波器主要是配合sobel算子运算的，分别计算x方向或y方向的图像差分，其参数与sobel基本一致。

def ff3():
    o = cv.imread('Fig/test3.jpg', cv.IMREAD_GRAYSCALE)
    scharrx = cv.Scharr(o, cv.CV_64F, 1, 0)
    scharrx = cv.convertScaleAbs(scharrx)  # 转回uint8
    scharry = cv.Scharr(o, cv.CV_64F, 0, 1)
    scharry = cv.convertScaleAbs(scharry)
    scharrxy = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
    cv.imshow("original", o)
    cv.imshow("x", scharrx)
    cv.imshow("y", scharry)
    cv.imshow("xy", scharrxy)
    cv.waitKey()
    cv.destroyAllWindows()



if __name__ == "__main__":
    # ff1()
    # ff2()
    ff3()

"""
    图像梯度计算的是图像变化的速度。对于图像的边缘部分，其灰度值变化较大，梯度值也较大；
    相反，对于图像中比较平滑的部分，其灰度值变化较小，相应的梯度值也较小。
    一般情况下，图像梯度计算的是图像的边缘信息。严格来讲，图像梯度计算需要求导数，
    但是图像梯度一般通过计算像素值的差来得到梯度的近似值（近似导数值）。
    
    
    Sobel 算子是一种离散的微分算子，该算子结合了高斯平滑和微分求导运算。该算子利用局部差分寻找边缘，计算所得的是一个梯度的近似值
    
    
 """

