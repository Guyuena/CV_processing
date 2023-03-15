import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)  # 例化相机设备
# HSV 比 BGR 在颜色空间上更容易表示颜色。在我们的应用中，我们会尝试提取一个蓝色的彩色对象
# 色调（H）、饱和度（S）和明度（V）
while (1):
    # Take each frame 提取每一视频帧
    _, frame = cap.read()
    # Convert BGR to HSV 将 BGR 转化为 HSV 颜色空间。
    # Converts an image from one colo space to another.
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    # 我们用蓝色像素的范围对该HSV图片做阈值。
    # [R,G,B]
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # Threshold the HSV image to get only blue colors
    # HSV图片阈值。
    # cv.inRange():主要是将在两个阈值内的像素值设置为白色（255），而不在阈值区间内的像素值设置为黑色（0），
    mask = cv.inRange(hsv, lower_blue, upper_blue) # cv.inRange()函数的作用是可以提取你想要的颜色，并把该颜色的区域设置为白色，其余的设置为黑色。
    # hsv:需要处理的源图像，可以为单通道或多通道
    # 就是将转换为HSV的图像中的像素值进行约束，可以同时针对多通道进行操作
    # Bitwise-AND mask and original image
    # 掩码和原始图片数据做与运算
    res = cv.bitwise_and(frame,frame, mask= mask)
    # res = cv.bitwise_or(frame,frame, mask= mask)
    # res = cv.bitwise_not(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    # 获取视频的帧率（FPS,pictures per second）
    fps = cap.get(cv.CAP_PROP_FPS)
    print("FPS: ", fps)

    # waitKey():函数的功能是不断刷新图像, 频率时间为delay, 单位为ms  返回值为当前键盘按键值
    # waitKey()–是在一个给定的时间内(单位ms)等待用户按键触发
    # 就是在5毫秒延时检测按下的键盘按键是哪个，和0xFF按位运算来得到具体的按键
    k = cv.waitKey(5) & 0xFF
    if k == 27:  # 用户按下 ESC(ASCII码为27)
        break

cv.destroyAllWindows()

# 拓展知识：如何知道我要追踪的颜色的HSV值是多少
# 例如, 为了找到绿色的 HSV 值, 可以在 Python 终端中输入以下代码
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
print(hsv_green)
#根据这个值去修改颜色的上下限范围


"""
    cv.inRange()函数的作用是可以提取你想要的颜色，并把该颜色的区域设置为白色，其余的设置为黑色。
    
    其实原理是这样的：在RGB三通道图像中，该函数会让你输入一个低值数组和高值数组，然后这个函数会扫描图片的每个像素，
    每个像素的值，即这个数组的每个值，如果相对应的，都在两个你输入的数组的，相对应的位置的数值内，
    那么这个数值会被设置为白色。否则只要有一个不在这个范围内，那么就会设置为黑色。
    
    比如：低值数组：np.array([1,2,3])
         高值数组：np.array([4,5,6])
    那么，如果一个像素所在区域想被设置成白色的话，那么像素值的第一个元素就得在1和4之间，第二个在2和5之间，第三个就在3和6之间。
    
    
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    输入的三通道数据，每个像素的RGB色值，R在110-130，G在50-255，R在50-255之间，那么就把它设置为白色
    否则就设置为黑色
    
    
"""