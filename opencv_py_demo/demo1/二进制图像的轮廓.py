import numpy as np
import cv2 as cv
def ff():
    im = cv.imread('Fig/test4.png')
    imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    # 用阈值处理把灰度图转为二值化黑白图   ret:是阈值 255 :大于阈值就把灰度值设为这个255，小于就为0
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    # print("ret",ret)
    """  2.寻找轮廓  """
    # 返回值： contours:轮廓（图像轮廓本身）  hierarchy：等级（每条轮廓对应的属性）
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    print(len(contours), hierarchy)
    print("type(contours= )",type(contours))
    # 参数1：源图像
    # 参数2：轮廓的检索方式，这篇文章主要讲解这个参数
    # 参数3：一般用 cv.CHAIN_APPROX_SIMPLE，就表示用尽可能少的像素点表示轮廓
    # contours：图像轮廓坐标，是一个链表
    # hierarchy：[Next, Previous, First Child, Parent]

    # 3.绘制轮廓
    cv.drawContours(im, contours, -1, (0, 0, 255), 2)
    # 第一个参数是指明在哪幅图像上绘制轮廓；
    # 第二个参数（contours）是轮廓本身，在Python中是一个list。
    # 第三个参数指定绘制轮廓list中的哪条轮廓，如果是 - 1，则绘制其中的所有轮廓。
    # 后面的参数很简单。其中color：线的颜色（0，0，255）表示红色；（255，0，0）表示蓝色；
    # thickness表明轮廓线的宽度，如果是 - 1（cv2.FILLED），则为填充模式。



    cv.imshow("show",im)
    cv.imshow("thresh",thresh)
    cv.waitKey(0)
    cv.destroyAllWindows()



if __name__ == "__main__":
    # 在OpenCV中，找到轮廓就像从黑色背景中找到白色物体。因此请记住，要找到的对象应该是白色，背景应该是黑色。
    ff()