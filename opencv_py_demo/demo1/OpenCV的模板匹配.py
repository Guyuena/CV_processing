

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def f1():
    img = cv.imread('Fig/liu2.png', 0)
    img2 = img.copy()
    template = cv.imread('Fig/liu22.png',0)
    w, h = template.shape[::-1]
    # All the 6 methods for comparison in a list
    methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img,top_left, bottom_right, 255, 2)
        plt.subplot(121),plt.imshow(res,cmap = 'gray')
        plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(img,cmap = 'gray')
        plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)
        plt.show()



# 模板与多个对象匹配  比如找出棋盘中的黑子与白子
def f2():
    img_rgb = cv.imread('Fig/test9.png')
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('Fig/test9_2.png', 0)
    template2 = cv.imread('Fig/test9_3.png', 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
    res2 = cv.matchTemplate(img_gray, template2, cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

    loc2 = np.where(res2 >= threshold)
    for pt2 in zip(*loc2[::-1]):
        cv.rectangle(img_rgb, pt2, (pt2[0] + w, pt2[1] + h), (0, 255, 0), 1)

    cv.imwrite('Fig/res.png', img_rgb)
    cv.imshow("res",img_rgb)
    cv.waitKey(0)
    cv.destroyAllWindows()



def f3():
    cap = cv.VideoCapture(0)  # 例化相机设备
    # HSV 比 BGR 在颜色空间上更容易表示颜色。在我们的应用中，我们会尝试提取一个蓝色的彩色对象
    # 色调（H）、饱和度（S）和明度（V）
    template = cv.imread('Fig/liu22.png', 0)
    while (1):
        # Take each frame 提取每一视频帧
        _, frame = cap.read()
        w, h = template.shape[::-1]
        img_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        res = cv.matchTemplate(img_gray, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.8
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 1)

        cv.imshow('frame', frame)
        # waitKey():函数的功能是不断刷新图像, 频率时间为delay, 单位为ms  返回值为当前键盘按键值
        # waitKey()–是在一个给定的时间内(单位ms)等待用户按键触发
        # 就是在5毫秒延时检测按下的键盘按键是哪个，和0xFF按位运算来得到具体的按键
        k = cv.waitKey(5) & 0xFF
        if k == 27:  # 用户按下 ESC(ASCII码为27)
            break

def f4():
    cap = cv.VideoCapture(0)  # 例化相机设备
    # HSV 比 BGR 在颜色空间上更容易表示颜色。在我们的应用中，我们会尝试提取一个蓝色的彩色对象
    # 色调（H）、饱和度（S）和明度（V）
    template = cv.imread('Fig/liu22.png', 0)
    w, h = template.shape[::-1]
    while (1):
        _, frame = cap.read()
        methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
                   'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
        img1 = frame.copy()
        img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        method = eval("cv.TM_CCOEFF")
        # Apply template Matching
        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv.rectangle(img, top_left, bottom_right, 255, 2)
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
