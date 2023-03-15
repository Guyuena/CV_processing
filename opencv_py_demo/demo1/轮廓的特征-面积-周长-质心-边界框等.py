import numpy as np
import cv2 as cv


""" 矩 """
# 图像矩可帮助您计算某些特征，例如物体的重心，物体的面积等
def f1():
    img = cv.imread('Fig/test.jpg',0) # 灰度图的读取方式
    ret,thresh = cv.threshold(img,127,255,0) # 二值化
    contours,hierarchy = cv.findContours(thresh, 1, 2) # 轮廓查找
    cnt = contours[0]
    # print("contours[0] = ",contours[0] )
    M = cv.moments(cnt)
    # moments(array, binaryImage=None)
    # array：计算矩的区域2D像素坐标集合或者单通道的CV_8U图像  是待计算矩的输入图像或者2D坐标集合
    # binaryImage：是否将所有非0像素值视为1的标志
    print( M )

    """质心"""
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    print("质心= ",cx ," ",cy)

    """轮廓面积"""
    area = cv.contourArea(cnt)
    print("轮廓面积= ",area)
    """轮廓周长"""
    perimeter = cv.arcLength(cnt, True) # 第二个参数指定形状是闭合轮廓(如果通过True)还是曲线。
    print("轮廓周长=",perimeter)



if __name__ == "__main__":
    f1()