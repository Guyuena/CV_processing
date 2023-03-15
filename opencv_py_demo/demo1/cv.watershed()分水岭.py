import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def f1():

    img = cv.imread("Fig/test9.png")
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

    cv.imshow("origin",img)
    cv.imshow("res",thresh)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    f1()
    # f2()
    # f3()


"""分水岭算法的整个过程："""

# 1-把梯度图像中的所有像素按照灰度值进行分类，并设定一个测地距离阈值。
# 2-找到灰度值最小的像素点（默认标记为灰度值最低点），让threshold从最小值开始增长，这些点为起始点。
# 3-水平面在增长的过程中，会碰到周围的邻域像素，测量这些像素到起始点（灰度值最低点）的测地距离，如果小于设定阈值，则将这些像素淹没，否则在这些像素上设置大坝，这样就对这些邻域像素进行了分类。
# 4-随着水平面越来越高，会设置更多更高的大坝，直到灰度值的最大值，所有区域都在分水岭线上相遇，这些大坝就对整个图像像素的进行了分区。