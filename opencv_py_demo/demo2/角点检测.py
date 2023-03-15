import numpy as np
import cv2 as cv


# 围棋棋盘角点检测
from matplotlib import pyplot as plt


def f1():
    img = cv.imread("Fig/test9.png")
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # 转换成灰度图
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray,2,3,0.04) # harris角点检测
    #result is dilated for marking the corners, not important
    dst = cv.dilate(dst,None)
    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
    cv.imshow('dst',img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()


# 以最高精度找到角点。OpenCV 带有一个函数 cv.cornerSubPix() ，它进一步细化了角点检测，以达到亚像素级精度

def f2():
    img = cv.imread("Fig/test9.png")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转换成灰度图
    # find Harris corners
    # harris角点检测
    gray = np.float32(gray)
    dst = cv.cornerHarris(gray, 2, 3, 0.04)
    dst = cv.dilate(dst, None)
    # 阈值转换原图
    ret, dst = cv.threshold(dst, 0.01 * dst.max(), 255, 0)
    dst = np.uint8(dst)
    # find centroids
    ret, labels, stats, centroids = cv.connectedComponentsWithStats(dst)
    # define the criteria to stop and refine the corners
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv.cornerSubPix(gray, np.float32(centroids), (5, 5), (-1, -1), criteria)
    # Now draw them
    # 整合
    res = np.hstack((centroids, corners))
    res = np.int0(res)
    img[res[:, 1], res[:, 0]] = [0, 0, 255]
    img[res[:, 3], res[:, 2]] = [0, 255, 0]
    # cv.imwrite('subpixel5.png', img)
    cv.imshow('dst',img)
    if cv.waitKey(0) & 0xff == 27:
        cv.destroyAllWindows()


def f3():
    # img = cv.imread('Fig/test9.png',0)
    img = cv.imread('Fig/test9.png')
    cv.imshow("in",img)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # 图像应该是灰度图像
    # gray = img.copy()
    corners = cv.goodFeaturesToTrack(gray, 0, 0.01, 10)
    corners = np.int0(corners)
    for i in corners:
        x, y = i.ravel()
        cv.circle(img, (x, y), 3, 255, -1)
    plt.imshow(img), plt.show()
    cv.waitKey(0)
    cv.destroyAllWindows()


# 视频图形中角点检测
def f4():
    cap = cv.VideoCapture(0)  # 例化相机设备
    # HSV 比 BGR 在颜色空间上更容易表示颜色。在我们的应用中，我们会尝试提取一个蓝色的彩色对象
    # 色调（H）、饱和度（S）和明度（V）
    while (1):
        # Take each frame 提取每一视频帧
        _, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # 转换成灰度图
        gray = np.float32(gray)
        dst = cv.cornerHarris(gray, 2, 3, 0.04)  # harris角点检测
        # result is dilated for marking the corners, not important
        dst = cv.dilate(dst, None)
        # Threshold for an optimal value, it may vary depending on the image.
        frame[dst > 0.01 * dst.max()] = [0, 0, 255]
        cv.imshow('frame', frame)
        # waitKey():函数的功能是不断刷新图像, 频率时间为delay, 单位为ms  返回值为当前键盘按键值
        # waitKey()–是在一个给定的时间内(单位ms)等待用户按键触发
        # 就是在5毫秒延时检测按下的键盘按键是哪个，和0xFF按位运算来得到具体的按键
        k = cv.waitKey(5) & 0xFF
        if k == 27:  # 用户按下 ESC(ASCII码为27)
            break

if __name__ == "__main__":
    f1()
    # f2()
    # f3()
    # f4()


# goodFeaturesToTrack(image, maxCorners, qualityLevel,
#                       minDistance, corners=None, mask=None,
#                       blockSize=None, useHarrisDetector=None, k=None):

# image: 输入图像，是八位的或者32位浮点型，单通道图像，所以有时候用灰度图
# maxCorners: 返回最大的角点数，是最有可能的角点数，如果这个参数不大于0，那么表示没有角点数的限制。
# qualityLevel: 图像角点的最小可接受参数，质量测量值乘以这个参数就是最小特征值，小于这个数的会被抛弃。
# minDistance: 返回的角点之间最小的欧式距离。 检测到的两个角点之间的最小欧氏距离
# mask: 检测区域。如果图像不是空的(它需要具有CV_8UC1类型和与图像相同的大小)，它指定检测角的区域。
# blockSize: 用于计算每个像素邻域上的导数协变矩阵的平均块的大小。
# useHarrisDetector：选择是否采用Harris角点检测，默认是false.
# k: Harris检测的自由参数。


#
# 也称为特征点检测。
# 角点通常被定义为两条边的交点，更严格地说法是，角点的局部邻域应该具有两个不同区域的不同方向的边界。而实际应用中，
# 大多数所谓的角点检测方法检测的是拥有特定特征的图像点，而不仅仅是“角点”。
# 这些特征点在图像中有具体的坐标，并具有某些数学特征，如局部最大或最小灰度、某些梯度特征等。

"""
图像特征类型可以被分为如下三种：

    边缘
    角点（感兴趣关键点）
    斑点（Blobs）（感兴趣区域）

角点检测算法

当前的图像处理邻域，角点检测算法可归纳为以下三类

    基于灰度图像的角点检测
    基于二值图像的角点检测
    基于轮廓曲线的角点检测
"""

# Scale-invariant feature transform，SIFT