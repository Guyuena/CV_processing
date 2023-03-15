import cv2 as cv
import numpy as np, sys
from clang.cindex import xrange

""" 图像融合的目的就是使两幅图像的重叠区域过渡自然且平滑  """


def tuxiangronghe(img1, img2):
    A = img1
    B = img2
    # 生成A的高斯金字塔
    G = A.copy()  # 源图像的复制
    gpA = [G]  # 高斯金字塔结果列表
    for i in range(6):
        G = cv.pyrDown(G)
        gpA.append(G)

    # #生成B的高斯金字塔
    G = B.copy()
    gpB = [G]
    for i in range(6):
        G = cv.pyrDown(G)
        gpB.append(G)

    # 生成A的拉普拉斯金字塔
    lpA = [gpA[5]]
    for i in range(5, 0, -1):
        GE = cv.pyrUp(gpA[i])  # 上采样
        L = cv.subtract(gpA[i - 1], GE)  # #两个图像相减
        lpA.append(L)
    # 生成B的拉普拉斯金字塔
    lpB = [gpB[5]]
    for i in range(5, 0, -1):
        GE = cv.pyrUp(gpB[i])
        L = cv.subtract(gpB[i - 1], GE)
        lpB.append(L)
    # Now add left and right halves of images in each level
    # numpy.hstack(tup)
    # Take a sequence of arrays and stack them horizontally
    # to make a single array.
    # 现在在每个级别中添加左右两半图像
    LS = []
    for la, lb in zip(lpA, lpB):
        rows, cols, dpt = la.shape
        ls = np.hstack((la[:, :cols // 2], lb[:, cols // 2:]))
        # ls = np.hstack((la[:, :cols // 4], lb[:, cols // 4: cols//2], la[:, cols//2:3 * cols//4], lb[:, 3*cols//4: ]))
        LS.append(ls)
    # now reconstruct
    # 现在重建
    ls_ = LS[0]
    for i in range(1, 6):
        ls_ = cv.pyrUp(ls_)
        ls_ = cv.add(ls_, LS[i])
    # image with direct connecting each half
    # 图像与直接连接的每一半
    # real = np.hstack((A[:,:cols//2],B[:,cols//2:]))
    # real = np.hstack((A[:,:cols//4],B[:,cols//4: cols//2], A[:, cols//2: 3*cols//4], B[:, 3*cols//4: ]))
    # cv.imwrite('F:/ninny_nero.jpg',ls_)
    # cv.imwrite('F:/nini_chaochao.jpg',real)
    real1 = np.hstack((A, B))
    real = np.hstack((A[:, 0:int(cols / 2)], B[:, int(cols / 2):]))
    cv.imshow('input_image1', ls_)
    cv.imshow('input_image2', real1)
    cv.imshow('input_image3', real)
    # pyramid_demo(src) # 高斯
    cv.waitKey(0)
    cv.destroyAllWindows()


"""
报错在：  L = cv.subtract(gpA[i-1],GE)  cv2.error:
L = cv.subtract(gpA[i-1], GE)图像相减这里报错，因为gpA[i-1]和GE的维度不一样所以报错，把两张输入图片的的尺寸改成一样，并且图片像素是2的幂
ls = np.hstack((la[:, 0:cols/2], lb[:, cols/2:]))图像拼接这里出错，原因可能是因为除2之后可能是浮点数
"""

if __name__ == "__main__":
    # 注意输入的图像的尺寸应为2的幂次方，而且两张图片要尺寸一样
    A = cv.imread('Fig/apple.png')
    B = cv.imread('Fig/orange.png')
    tuxiangronghe(A, B)
# 1、加载苹果和橙子的两个图像
# 2、查找苹果和橙子的高斯金字塔（在此示例中，级别数为6）
# 3、在高斯金字塔中，找到其拉普拉斯金字塔
# 4、然后在每个拉普拉斯金字塔级别中加入苹果的左半部分和橙子的右半部分
# 5、最后从此联合图像金字塔中重建原始图像