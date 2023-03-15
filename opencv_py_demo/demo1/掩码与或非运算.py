import cv2 as cv
import numpy as np


def image_and(image,mask):#输入图像和掩膜
	area = cv.bitwise_and(image,image,mask=mask)  #mask=mask表示要提取的区域
	cv.imshow("area",area)
	return area

def image_and2(mask1,mask2):#输入两张不同掩膜，求他们的交集
	cv.imshow("mask1",mask1)
	cv.imshow("mask2",mask2)
	and_area = cv.bitwise_and(mask1,mask2)  #掩膜mask1和掩膜mask2相与求并集
	cv.imshow("and_area",and_area)
	return and_area


def image_and3():
	img = cv.imread("Fig/test.jpg")
	lower = np.uint8([120, 120, 120])
	upper = np.uint8([255, 255, 255])
	# 低于lower_red 和高于uppper_red的部分都变成0， 之间的数字变成255，相当于过滤掉背景
	white_mask = cv.inRange(img, lower, upper)
	cv.imshow("white_mask", white_mask)
	masked = cv.bitwise_and(img, img, mask=white_mask)
	cv.imshow("result_mask", masked)
	cv.waitKey(0)
	cv.destroyAllWindows()

#或运算
def image_or():
	img = cv.imread("Fig/test.jpg")
	lower = np.uint8([120, 120, 120])
	upper = np.uint8([255, 255, 255])
	# 低于lower_red 和高于uppper_red的部分都变成0， 之间的数字变成255，相当于过滤掉背景
	white_mask = cv.inRange(img, lower, upper)
	cv.imshow("white_mask_or", white_mask)
	masked = cv.bitwise_or(img, img, mask=white_mask)
	cv.imshow("result_mask_or", masked)
	cv.waitKey(0)
	cv.destroyAllWindows()

# 非运算
def image_not():
	img = cv.imread("Fig/test.jpg")
	lower = np.uint8([120, 120, 120])
	upper = np.uint8([255, 255, 255])
	# 低于lower_red 和高于uppper_red的部分都变成0， 之间的数字变成255，相当于过滤掉背景
	white_mask = cv.inRange(img, lower, upper)
	cv.imshow("white_mask_not", white_mask)
	masked = cv.bitwise_not(img, img, mask=white_mask)
	cv.imshow("result_mask_not", masked)
	cv.waitKey(0)
	cv.destroyAllWindows()

if __name__ == "__main__":
	image_and3()
	image_or()
	image_not()

