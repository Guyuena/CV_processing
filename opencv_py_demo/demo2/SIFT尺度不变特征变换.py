# import cv2
# def sift_kp(image):
#     gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#     sift = cv2.xfeatures2d_SIFT.create()
#     kp,des = sift.detectAndCompute(image, None)
#     kp_image = cv2.drawKeypoints(image, kp, None)
#     return kp_image,kp,des
# image = cv2.imread('Fig/test.jpg')
# kp_image, _, des = sift_kp(image)
# print(image.shape, des.shape)
# cv2.namedWindow('dog',cv2.WINDOW_NORMAL)
# cv2.imshow('dog', kp_image)
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()
#

import numpy as np
import cv2 as cv
# img = cv.imread('Fig/test.jpg')
# gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# sift = cv.xfeatures2d.SIFT_create()
# # sift = cv.SIFT_create()
# kp = sift.detect(gray,None)
# img=cv.drawKeypoints(gray,kp,img)
# cv.imwrite('sift_keypoints.jpg',img)

# AttributeError: module 'cv2.cv2' has no attribute 'xfeatures2d'
# 将d = cv2.xfeatures2d.SIFT_create()
# 修改为d = cv2.SIFT_create()
print("当前OpenCV版本",cv.__version__)


# 主要步骤：
#   1.构建DOG尺度空间
#   2.关键点搜索和定位
#   3.方向赋值
#   4.关键点描述子的生成