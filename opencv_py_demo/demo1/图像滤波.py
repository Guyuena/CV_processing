import numpy as np
import cv2 as cv

from matplotlib import pyplot as plt

# 卷积核滤波
# https://blog.csdn.net/hysterisis/article/details/113097507
def filter2D():

    img = cv.imread('Fig/img.png')
    kernel = np.ones((5,5),np.float32)/25
    dst = cv.filter2D(img,-1,kernel)
    plt.subplot(121),plt.imshow(img),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 均值滤波
def blur():
    img = cv.imread('Fig/img.png')
    blur = cv.blur(img, (5, 5))
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('Blurred')
    plt.xticks([]), plt.yticks([])
    plt.show()


def gauss():
    img = cv.imread('Fig/img.png')
    blur = cv.GaussianBlur(img,(5,5),0)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('gauss')
    plt.xticks([]), plt.yticks([])
    plt.show()
# 种植滤波
def midVale():
    img = cv.imread('Fig/img.png')
    blur = cv.medianBlur(img,5)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('midVale')
    plt.xticks([]), plt.yticks([])
    plt.show()


# 双边滤波
def filter2():
    img = cv.imread('Fig/img.png')
    blur = cv.bilateralFilter(img,9,75,75)
    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122), plt.imshow(blur), plt.title('bilateralFilter')
    plt.xticks([]), plt.yticks([])
    plt.show()


if __name__ == "__main__":
    filter2D()
    blur()
    gauss()
    midVale()
    filter2()
