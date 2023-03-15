# 将不同的几何变换应用于图像，如平移、旋转、仿射变换等

import numpy as np
import cv2 as cv

# 缩放
from matplotlib import pyplot as plt

"""
    图像几何变换又称为图像空间变换， 它将一幅图像中的坐标位置映射到另一幅图像中的新坐标位置。
    几何变换不改变图像的像素值， 只是在图像平面上进行像素的重新安排。
    常用于图像翻转(Flip)、旋转(Rotations)、
    平移(Translations)、
    缩放(Scale operations)等，
    然而其实现的函数就是cv::warpAffine()
"""

def resize():
    img = cv.imread('Fig/test.jpg')

    # interpolation:内插法  进行插值方法指定
    res1 = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
    cv.imshow('res1', res1)
    # OR
    height, width = img.shape[:2]
    res2 = cv.resize(img, (1 * width, 1 * height), interpolation=cv.INTER_CUBIC)
    cv.imshow('res2', res2)
    cv.waitKey(0)
    cv.destroyAllWindows()


"""  仿射变换(warpaffine) """

# 平移变换
def pingyi():
    img = cv.imread('Fig/test.jpg', 0) # 0:读的模式
    rows, cols = img.shape
    # 创建转换矩阵M M矩阵这里丝毫两行三列
    # 平移变换是物体位置的移动。如果知道 （x，y） 方向的偏移量，假设为 (t_x,t_y)
    # [1,0,t_x]:x方向移动量
    # [0,1,t_y]:y方向移动量
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    # 操作函数cv.warpAffine() M:线性变换矩阵
    dst = cv.warpAffine(img, M, (cols, rows))
    # cv.warpAffine 函数的第三个参数是输出图像的大小，其形式应为（宽度、高度）。记住宽度=列数，高度=行数。
    cv.imshow('img', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()


#旋转 Rotation

def xuanzhuan():
    img = cv.imread('Fig/test.jpg', 0)
    rows, cols = img.shape
    # cols-1 and rows-1 are the coordinate limits.
    # 获得线性变换矩阵M
    M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)
    # 和线性变换矩阵进行矩阵运算，得到目的矩阵
    dst = cv.warpAffine(img, M, (cols, rows))
    cv.imshow('img', dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

# 仿射变换   Transform
# 进行线性映射
# 在仿射变换中，原始图像中的所有平行线在输出图像中仍然是平行的
def transform():
    img = cv.imread('Fig/test.jpg')
    rows, cols, ch = img.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    M = cv.getAffineTransform(pts1, pts2)
    dst = cv.warpAffine(img, M, (cols, rows))
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()

# 透视变换
def toushi():
    img = cv.imread('Fig/test.jpg')
    rows, cols, ch = img.shape
    pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
    pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
    M = cv.getPerspectiveTransform(pts1, pts2)
    dst = cv.warpPerspective(img, M, (300, 300))
    plt.subplot(121), plt.imshow(img), plt.title('Input')
    plt.subplot(122), plt.imshow(dst), plt.title('Output')
    plt.show()

def toushi2():
    # img = cv.imread('test.jpg')
    while (1):
        _, img = cap.read()
        rows, cols, ch = img.shape
        pts1 = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
        pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
        M = cv.getPerspectiveTransform(pts1, pts2)
        dst = cv.warpPerspective(img, M, (300, 300))
        plt.subplot(121), plt.imshow(img), plt.title('Input')
        plt.subplot(122), plt.imshow(dst), plt.title('Output')
        plt.show()

if __name__ == "__main__":
    print("main()")
    cap = cv.VideoCapture(0)  # 例化相机设备
    # resize()
    # pingyi()
    # xuanzhuan()
    transform()
    # toushi()
    # toushi2()


