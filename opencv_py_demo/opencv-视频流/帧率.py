import random

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)  # 例化相机设备
while (1):
    # Take each frame 提取每一视频帧
    _, frame = cap.read()

    # 获取视频的帧率（FPS,pictures per second）
    text = "Nice to see you!"
    fps = cap.get(cv.CAP_PROP_FPS)
    # 图片 添加的文字 位置 字体 字体大小 字体颜色 字体粗细
    X = random.randint(50,100)
    Y= random.randint(50,100)
    cv.putText(frame, str(fps)+"FPS", (X, Y), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 200), 2)
    # print(X)
    # print(Y)
    # 用putText把FPS的数值显示到屏幕上。
    # print("FPS: ", str(fps))
    # print(type(fps))
    # print(type(str(fps)))
    cv.imshow('frame', frame)
    # waitKey():函数的功能是不断刷新图像, 频率时间为delay, 单位为ms  返回值为当前键盘按键值
    # waitKey()–是在一个给定的时间内(单位ms)等待用户按键触发
    # 就是在5毫秒延时检测按下的键盘按键是哪个，和0xFF按位运算来得到具体的按键
    k = cv.waitKey(5) & 0xFF
    if k == 27:  # 用户按下 ESC(ASCII码为27)
        break

cv.destroyAllWindows()

# // 将帧率信息写在输出帧上
# putText(frame, // 图像矩阵
# fpsString, // string型文字内容
# cv::Point(5, 20), // 文字坐标，以左下角为原点
# cv::FONT_HERSHEY_SIMPLEX, // 字体类型
# 0.5, // 字体大小
