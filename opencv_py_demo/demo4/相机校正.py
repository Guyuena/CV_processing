# import numpy as np
# import cv2 as cv
# import glob
#
# # 终止标准
# criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
#
# # 准备对象点, 如 (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# objp = np.zeros((6*7,3), np.float32)
# objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
#
# # 用于存储所有图像对象点与图像点的矩阵
# objpoints = [] # 在真实世界中的 3d 点
# imgpoints = [] # 在图像平面中的 2d 点
#
#
#
# # 视频流中检测
# def f2():
#     cap = cv.VideoCapture(0)  # 例化相机设备
#     while (1):
#         # Take each frame 提取每一视频帧
#         _, img = cap.read()
#         gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#         # 找到棋盘上所有的角点
#         ret, corners = cv.findChessboardCorners(gray, (7, 6), None)
#         # 如果找到了，便添加对象点和图像点(在细化后)
#         if ret == True:
#             objpoints.append(objp)
#             corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
#             imgpoints.append(corners)
#             # 绘制角点
#             cv.drawChessboardCorners(img, (7, 6), corners2, ret)
#         cv.imshow('frame', img)
#         k = cv.waitKey(10) & 0xFF
#         if k == 27:  # 用户按下 ESC(ASCII码为27)
#             break
#
#
#
# if __name__ == "__main__":
#     # f1()
#     f2()
#
#

import cv2  # Import the OpenCV library to enable computer vision
import numpy as np  # Import the NumPy scientific computing library

# Author: Addison Sears-Collins
# https://automaticaddison.com
# Description: Detect corners on a chessboard

filename = 'Fig/chess.png'

# Chessboard dimensions
number_of_squares_X = 9  # 列数 Number of chessboard squares along the x-axis
number_of_squares_Y = 7  # 行数 Number of chessboard squares along the y-axis
# 居于内部的行列列数
nX = number_of_squares_X - 1  # Number of interior corners along x-axis
nY = number_of_squares_Y - 1  # Number of interior corners along y-axis


def main():
    # Load an image
    image = cv2.imread(filename)
    cv2.imshow("source", image)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Find the corners on the chessboard
    # findChessboardCorners的内置函数，利用这个函数可以找出棋盘格中各个角的坐标
    success, corners = cv2.findChessboardCorners(gray, (nY, nX), None)
    print("success= ",success)

    # If the corners are found by the algorithm, draw them
    if success == True:




        # Draw the corners
        cv2.drawChessboardCorners(image, (nY, nX), corners, success)

        # Create the output file name by removing the '.jpg' part
        size = len(filename)
        # new_filename = filename[:size - 4]
        # new_filename = new_filename + '_drawn_corners.jpg'
        new_filename = './_drawn_corners.jpg'

        # Save the new image in the working directory
        cv2.imwrite(new_filename, image)

        # Display the image
        cv2.imshow("Image", image)

        # Display the window until any key is pressed
    cv2.waitKey(0)

        # Close all windows
    cv2.destroyAllWindows()




if __name__ == "__main__":
    main()

# 校准相机是使用已知的真实世界模式（例如棋盘）来估计相机镜头和图像的外参数（旋转和平移矢量）和
# 内参数（例如焦距、光学中心等）的过程传感器，以减少由相机缺陷引起的失真误差。
# 这些参数包括：
#   焦距
#   图像（即光学）中心（通常不完全在（宽度/2，高度/2）处）
#   沿行和列的像素的缩放因子
#   偏斜因子
#   镜头畸变
