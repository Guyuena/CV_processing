import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def f1():

    # img = cv.imread('Fig/liu2.png')
    img = cv.imread('Fig/test.jpg')
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64) #以0填充的背景
    fgdModel = np.zeros((1,65),np.float64) #以0填充的前景
    rect = (0,0,700,700)
    # rect = (0,0,1000,1000)
    cv.grabCut(img=img,mask=mask,rect=rect,bgdModel=bgdModel,fgdModel=fgdModel,iterCount=10,mode=cv.GC_INIT_WITH_RECT)
    # 做完这些我们的掩码已经变成包含0~3的值

    # 将掩码中0或2 转为0（背景）， 其它（1或3）转为1（前景）
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    # np.where(condition, x, y)
    # 满足条件(condition)，输出x，不满足输出y。
    img = img*mask2[:,:,np.newaxis] #分割后的前景
    plt.imshow(img),plt.colorbar(),plt.show()


def f2():
    capture = cv.VideoCapture(0)
    mog = cv.createBackgroundSubtractorMOG2()
    se = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    while True:
        ret, image = capture.read()
        if ret is True:
            fgmask = mog.apply(image)
            ret, binary = cv.threshold(fgmask, 220, 255, cv.THRESH_BINARY)
            binary = cv.morphologyEx(binary, cv.MORPH_OPEN, se)
            bgimage = mog.getBackgroundImage()
            cv.imshow("bgimage", bgimage) # 背景建模
            cv.imshow("frame", image)  # 前景检测
            cv.imshow("fgmask", binary) # 移动对象mask
            c = cv.waitKey(50)
            if c == 27:
                break
        else:
            break

    cv.destroyAllWindows()

if __name__ == "__main__":
    # f1()
    f2()
    # f3()



# GrabCut算法的实现步骤：
#
# 1   在图片中定义(一个或者多个)包含物体的矩形。
# 2   矩形外的区域被自动认为是背景。
# 3   对于用户定义的矩形区域，可用背景中的数据来区分它里面的前景和背景区域。
# 4   用高斯混合模型(GMM)来对背景和前景建模，并将未定义的像素标记为可能的前景或者背景。
# 5   图像中的每一个像素都被看做通过虚拟边与周围像素相连接，而每条边都有一个属于前景或者背景的概率，这是基于它与周边像素颜色上的相似性。
# 6   每一个像素(即算法中的节点)会与一个前景或背景节点连接。
# 7   在节点完成连接后(可能与背景或前景连接)，若节点之间的边属于不同终端(即一个节点属于前景，另一个节点属于背景)，则会切断他们之间的边，这就能将图像各部分分割出来。





"""grabcut分割算法，该算法可以方便的分割出前景图像"""
# grabCut(img, mask, rect, bgdModel, fgdModel, iterCount, mode=None)
# img：输入原图像；图像的类型必须为：CV_8UC3
# mask：输出掩码； 第二个参数是mask图像，它的大小和image一样，但是它的格式为CV_8UC1，只能是单通道的，grabcut算法的结果就保存在该图像中
# rect：用户选择的前景矩形区域；
# bgModel：输出背景图像；
# fgModel：输出前景图像；
# iterCount：迭代次数；
# mode: 模式   要么cv2.GC_INIT_WITH_RECT或cv2.GC_INIT_WITH_MASK，这分别取决于你是用一个边框还是一个掩码初始化GrabCut。

# mask掩码图像的值只能为下面下面4个值(PR，probably表示可能的)：
# GC_BGD    = 0,  //背景
# GC_FGD    = 1,  //前景
# GC_PR_BGD = 2,  //可能背景
# GC_PR_FGD = 3   //可能前景