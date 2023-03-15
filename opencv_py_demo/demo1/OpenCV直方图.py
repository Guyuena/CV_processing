import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def f1():

    img = cv.imread('Fig/test.jpg',0) # 先以灰度图的方式读取图片,当然可以非灰度图
    plt.hist(img.ravel(),256,[0,256]); plt.show()

    # 或
    # hist, bins = np.histogram(img.ravel(), 256, [0, 256])
    # plt.hist(hist,bins)
    # plt.show()


# 通过直方图分析 R-G-B色彩分布,通过直方图中三种颜色的灰度分布分析出在某个灰度范围内哪个颜色占主要
def f2():
    img = cv.imread('Fig/f1.png')  # 先以灰度图的方式读取图片,当然可以非灰度图
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()


# 直方图之蒙板
"""
如果要查找图像某些区域的直方图怎么办？只需在要查找直方图的区域上创建白色的蒙版图像，否则创建黑色。然后通过这个作为掩码
"""
def f3(): # 分析图像特定区域的直方图
    img = cv.imread('Fig/f1.png', 0)
    # create a mask
    mask = np.zeros(img.shape[:2], np.uint8)
    mask[100:300, 100:400] = 255
    masked_img = cv.bitwise_and(img, img, mask=mask)
    # Calculate histogram with mask and without mask
    # Check third argument for mask
    hist_full = cv.calcHist([img], [0], None, [256], [0, 256])
    hist_mask = cv.calcHist([img], [0], mask, [256], [0, 256])
    plt.subplot(221), plt.imshow(img, 'gray')
    plt.subplot(222), plt.imshow(mask, 'gray')
    plt.subplot(223), plt.imshow(masked_img, 'gray')
    plt.subplot(224), plt.plot(hist_full), plt.plot(hist_mask)
    plt.xlim([0, 256])
    plt.show()

"""
直方图均衡化的概念，并将其用于改善图像的对比度。 理论 考虑一个图像，其像素值仅限于特定的值范围。例如，较亮的图像会将所有像素限制在较高的值。
但是，好的图像将具有来自图像所有区域的像素。因此，您需要将此直方图拉伸到两端(如下图所示，来自维基百科)，这就是直方图均衡化的作用(简单来说)
"""

def f4():
    img = cv.imread('Fig/f1.png', 0) # 它的输入只是灰度图像，所以读取图像要求是灰度读入

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    plt.plot(cdf_normalized, color='b')
    plt.hist(img.flatten(), 256, [0, 256], color='r')
    plt.xlim([0, 256])
    plt.legend(('cdf', 'histogram'), loc='upper left')
    plt.show()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img2 = cdf[img]


def f5():
    img = cv.imread('Fig/f2.png',0)
    equ = cv.equalizeHist(img)
    res = np.hstack((img, equ))  # stacking images side-by-side
    cv.imwrite('res.png', res)
    cv.imshow("res",res)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == "__main__":
    # 图像直方图是对图像的像素进行统计，不受到图像的旋转和平移等效果。
    # 图像直方图的横轴为图像的灰度值作为横轴，以灰度值的个数和比例作为纵轴去绘制统计图。
    # 直方图做均衡，就是让一个可能是因为色彩分布过于集中而导致图像的亮度过小了，经过直方图均衡后显得更加明亮
    # f1()
    # f2()

    # f3()
    f4()