import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

""" 使用Numpy查找傅立叶变换  """
def fft1():
    img = cv.imread('Fig/liu2.png',0)
    # 使用Numpy查找傅立叶变换
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift)) # 到幅度谱。
    plt.subplot(221),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])


    # 低频成分多的频谱图
    img2 = cv.imread('Fig/test8.jpg',0)
    # 使用Numpy查找傅立叶变换
    f2 = np.fft.fft2(img2)
    fshift2 = np.fft.fftshift(f2)
    magnitude_spectrum2 = 20*np.log(np.abs(fshift2)) # 到幅度谱。
    plt.subplot(223),plt.imshow(img2, cmap = 'gray')
    plt.title('Input Image2'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(magnitude_spectrum2, cmap = 'gray')
    plt.title('Magnitude Spectrum2'), plt.xticks([]), plt.yticks([])


    plt.show()

#逆变换
def ifft():
    # 使用np.fft.ifftshift()应用反向移位，以使DC分量再次出现在左上角。然后使用np.ifft2()函数找到逆FFT
    print("ceshi")



# OpenCV中的傅立叶变换
def fft2():
    img = cv.imread('Fig/liu2.png', 0) #灰度图读取
    # 输入的图像应首先转换为np.float32
    dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    # 频谱转换
    magnitude_spectrum = 20 * np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title('Input Image1'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum1'), plt.xticks([]), plt.yticks([])


    # 逆变换
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)
    # create a mask first, center square is 1, remaining all zeros
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1
    # apply mask and inverse DFT
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv.idft(f_ishift)
    img_back = cv.magnitude(img_back[:, :, 0], img_back[:, :, 1])
    plt.subplot(223), plt.imshow(img, cmap='gray')
    plt.title('Input Image2'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img_back, cmap='gray')
    plt.title('Magnitude Spectrum2'), plt.xticks([]), plt.yticks([])
    plt.show()





    plt.show()



if __name__ == "__main__":
    # fft1()
    fft2()

# 图像处理2.二维图像的频谱图理解  https://blog.csdn.net/weixin_39504171/article/details/94553357

 # 频谱图的中心为0频率点,可以视为直流分量,这一点的表示完全没有灰度变化的部分的能量高低。以该点为圆心做同心圆,半径越大,表示频率越大;亮度越大,表示能量越大。