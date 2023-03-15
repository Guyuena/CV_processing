
import cv2 as cv
import numpy as np


# 直线检测
def f1():

    img = cv.imread(cv.samples.findFile('Fig/test6.png',1))# Read image
    # Convert the image to gray-scale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the edges in the image using canny detector
    edges = cv.Canny(gray, 50, 200)
    # Detect points that form a line
    lines = cv.HoughLinesP(edges, 1, np.pi/180, 10, minLineLength=10, maxLineGap=250)
    # Draw lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    # Show result
    cv.imshow("Result Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# 检测图像中的圆圈
def f2():
    # Read image as gray-scale
    img = cv.imread('Fig/liu2.png', cv.IMREAD_COLOR)
    # Convert to gray-scale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Blur the image to reduce noise
    img_blur = cv.medianBlur(gray, 5)
    # Apply hough transform on the image
    circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, img.shape[0] / 64, param1=200, param2=10, minRadius=5,
                               maxRadius=30)
    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw outer circle
            cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw inner circle
            cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv.imshow("Result Image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def f3():
    cap = cv.VideoCapture(0)  # 例化相机设备
    # HSV 比 BGR 在颜色空间上更容易表示颜色。在我们的应用中，我们会尝试提取一个蓝色的彩色对象
    # 色调（H）、饱和度（S）和明度（V）
    while (1):
        # Take each frame 提取每一视频帧
        _, frame = cap.read()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # 进行中值滤波
        # dst_img = cv.medianBlur(gray, 7)
        img_blur = cv.medianBlur(gray, 9)
        # Apply hough transform on the image

        # 霍夫圆检测
        circles = cv.HoughCircles(img_blur, cv.HOUGH_GRADIENT, 1, frame.shape[0] / 64, param1=200, param2=10, minRadius=5,
                                  maxRadius=30)
        # Draw detected circles
        # 将检测结果绘制在图像上
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                # Draw outer circle
                cv.circle(frame, (i[0], i[1]), i[2], (0, 255, 0), 2)
                # Draw inner circle
                cv.circle(frame, (i[0], i[1]), 2, (0, 0, 255), 3)

        # 显示图像
        cv.imshow('frame', frame)
        # waitKey():函数的功能是不断刷新图像, 频率时间为delay, 单位为ms  返回值为当前键盘按键值
        # waitKey()–是在一个给定的时间内(单位ms)等待用户按键触发
        # 就是在5毫秒延时检测按下的键盘按键是哪个，和0xFF按位运算来得到具体的按键
        k = cv.waitKey(5) & 0xFF
        if k == 27:  # 用户按下 ESC(ASCII码为27)
            break

if __name__ == "__main__":
    # f1()
    # f2()
    f3()

"""霍夫圆检测对噪声比较敏感，所以首先对图像进行中值滤波"""
# circle = cv2.HoughCircles() 圆检测
#   image：输入图像（灰度图）
#   method：使用霍夫变换圆检测的算法，参数为cv2.HOUGH_GRADIENT
#   dp：霍夫空间的分辨率，dp=1时表示霍夫空间与输入图像空间的大小一致，dp=2时霍夫空间是输入图像空间的一半，以此类推
#   minDist：为圆心之间的最小距离，如果检测到的两个圆心之间距离小于该值，则认为它们是同一个圆心
#   param1：边缘检测时使用Canny算子的高阈值，低阈值是高阈值的一半
#   param2∶检测圆心和确定半径时所共有的阈值
#   minRadius和maxRadius：为所检测到的圆半径的最小值和最大值


