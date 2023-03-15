

# 如果像素值大于阈值怎么样，小于阈值怎么样

import cv2 as cv
import numpy as np
from clang.cindex import xrange
from matplotlib import pyplot as plt

# 如果像素值大于阈值，则会被赋为一个值（可能为白色），否则会赋为另一个值（可能为黑色）。使用的函数是 cv.threshold。
# 第一个参数是源图像，它应该是灰度图像。第二个参数是阈值，用于对像素值进行分类。第三个参数是 maxval，它表示像素值大于（有时小于）阈值时要给定的值
"""
    src：源图像，可以为8位的灰度图，也可以为32位的彩色图像；
    thresh：阈值；
    maxval：二值图像中灰度最大值；  当大于阈值thresh就把灰度值设为这个设定值
    type：阈值操作类型
    dst：输出图像；
    
    threshold(src, thresh, maxval, type, dst=None):
"""

# 简单阈值法
def fc1():
    img = cv.imread('Fig/test.jpg', 0) # 以灰度图的形式读取图像
    # ret: 阈值大小 thresh：处理后的图像
    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    print("ret= ",ret)
    print("thresh1.shape= ",thresh1.shape)
    ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
    print("ret= ", ret)
    ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)
    print("ret= ", ret)
    ret,thresh4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)
    print("ret= ", ret)
    ret,thresh5 = cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
    print("ret= ", ret)
    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
    for i in xrange(6):
        # 绘制多个图像，我们使用plt.subplot()函数
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()


# 自适应阈值
# (src, maxValue, adaptiveMethod, thresholdType, blockSize, C, dst=None)
""" maxValue：满足条件的像素点需要设置的灰度值。（将要设置的灰度值）
    adaptiveMethod：自适应阈值算法
    thresholdType：opencv提供的二值化方法
    blockSize：要分成的区域大小，上面的N值，一般取奇数
    C：常数，每个区域计算出的阈值的基础上在减去这个常数作为这个区域的最终阈值，可以为负数
"""
def fc2():
    img = cv.imread('Fig/test.jpg', 0)
    img = cv.medianBlur(img, 5)
    ret, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 2)
    th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    titles = ['Original Image', 'Global Thresholding (v = 127)',
              'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    for i in xrange(4):
        plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

def fc3():
    return






if __name__ =="__main__":
    # fc1()
    fc2()
    # fc3()