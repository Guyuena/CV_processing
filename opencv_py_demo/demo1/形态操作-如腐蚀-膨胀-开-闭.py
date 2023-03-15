import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt



# 腐蚀的基本概念就像土壤侵蚀一样，只侵蚀前景对象的边界（总是尽量保持前景为白色）。
# 那它有什么作用呢？内核在图像中滑动（如二维卷积）。只有当内核下的所有像素都为 1 时，
# 原始图像中的像素（1 或 0）才会被视为 1，否则会被侵蚀（变为零）。
def ff(): # 腐蚀  erode：冲蚀、侵蚀
    img = cv.imread("Fig/img2.png")
    kernel = np.ones((3, 3), dtype=np.uint8)
    erosion = cv.erode(img, kernel, iterations=1)
    ss = np.hstack((img, erosion)) # 水平拼接两张图片
    plt.imshow(ss)
    plt.show()

def ff2(): #膨胀  dilate：使膨胀
    img = cv.imread("Fig/img2.png")
    kernel = np.ones((3, 3), dtype=np.uint8)
    dilate = cv.dilate(img, kernel, 1)  # 1:迭代次数，也就是执行几次膨胀操作
    res = np.hstack((img, dilate))  # 水平拼接两张图片
    plt.imshow(res)
    plt.show()


# 开运算和闭运算
#       开运算：先腐蚀，再膨胀
#       闭运算：先膨胀，再腐蚀

def ff3(): #开运算
    img = cv.imread("Fig/img2.png")
    kernel = np.ones((3, 3), dtype=np.uint8)
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel, 10)  # 10:迭代次数，也就是执行几次开运算操作
    res = np.hstack((img, opening))  # 水平拼接两张图片
    plt.imshow(res)
    plt.show()


# 分析： 我们发现大部分毛刺已经消除，而且字体信息也没有发生变化，
# 这也就是我们想要的效果。虽然仍然有一部信息没有被清除，我们只需要调整卷积核的大小就可以实现。




def ff4(): #闭运算
    img = cv.imread("Fig/img2.png")
    kernel = np.ones((3, 3), dtype=np.uint8)
    closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)  ## 有缺陷，填补缺陷  # 10:迭代次数，也就是执行几次开运算操作
    res = np.hstack((img, closing))  # 水平拼接两张图片
    plt.imshow(res)
    plt.show()
# 分析： 字体不改变的前提下，我们把字体缺陷信息补全。


# 梯度计算
#   梯度计算主要显示的是边缘信息。计算的方法：
#   膨胀的图像 - 腐蚀的图像
#   我们明显的看出，用大一圈的图像减去小一圈的图像正好就是边缘的信息。
def ff5():
    img = cv.imread("Fig/img2.png")
    kernel = np.ones((3, 3), dtype=np.uint8)
    gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    res = np.hstack((img, gradient))  # 水平拼接两张图片
    plt.imshow(res)
    plt.show()
# 分析： 我们可以看出来，我们形成了一个空心的字体样式


# 高帽计算：原始图像 - 开运算结果
def ff6():
    img = cv.imread("Fig/img2.png")
    kernel = np.ones((3, 3), dtype=np.uint8)
    top_hat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
    res = np.hstack((img, top_hat))  # 水平拼接两张图片
    plt.imshow(res)
    plt.show()

# 分析： 可以看出来，所有的毛刺信息我们全部提取了出来。

 # 黑帽计算：闭运算结果 - 原始图像


def ff7():
    img = cv.imread("Fig/img2.png")
    kernel = np.ones((3, 3), dtype=np.uint8)
    black_hat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)
    res = np.hstack((img, black_hat))  # 水平拼接两张图片
    plt.imshow(res)
    plt.show()
# 高帽操作显示毛刺，那么黑帽就是显示缺陷。


if __name__ == "__main__":
    """ 总结性的来说： + 膨胀用来处理缺陷问题； + 腐蚀用来处理毛刺问题。 """
    # ff()
    # ff2()
    # ff3()
    # ff4()
    # ff5()
    # ff6()
    ff7()