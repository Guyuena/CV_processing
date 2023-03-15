import cv2 as cv



def test():
    img1 = cv.imread("Fig/test.jpg") # 无参读取，默认读取 1 cv.imread("test.jpg",1)
    print(img1.shape)
    img2 = cv.imread("Fig/test.jpg", 0) # cv2.IMREAD_GRAYSCALE 读入灰度图片，可以直接写0
    print(img2.shape)
    img3 = cv.imread("Fig/test.jpg", -1) # cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道，可以直接写-1
    print(img3.shape)
    cv.imshow("默认 1 ", img1)
    cv.imshow("灰度 0 ", img2)
    cv.imshow("完整读取-alpha", img3)
    cv.waitKey(0)
    cv.destroyAllWindows()

# cv2.imread()的默认通道格式HWC

if __name__ == "__main__":

    print("cv-imread-测试")
    test()