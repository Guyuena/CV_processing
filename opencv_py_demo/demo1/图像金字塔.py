import cv2 as cv


# 高斯金字塔


# 首先将原图像作为最底层图像G0（高斯金字塔的第0层），利用高斯核对其进行卷积，
# 然后对卷积后的图像进行下采样（去除偶数行和列）得到上一层图像G1，
# 将此图像作为输入，重复卷积和下采样操作得到更上一层图像，反复迭代多次，
# 形成一个金字塔形的图像数据结构，即高斯金字塔。

def pyramid_demo(image):
    level = 3  # 设置金字塔的层数为3
    temp = image.copy()  # 拷贝图像
    pyramid_images = []  # 建立一个空列表
    for i in range(level):
        dst = cv.pyrDown(temp)  # 先对图像进行高斯平滑，然后再进行降采样（将图像尺寸行和列方向缩减一半）
        pyramid_images.append(dst)  # 在列表末尾添加新的对象
        cv.imshow("pyramid" + str(i), dst)
        temp = dst.copy() # 下一次采样的来源是上一次采样的结果
    return pyramid_images


# 拉普拉斯金字塔
# 在高斯金字塔的运算过程中，图像经过卷积和下采样操作会丢失部分 "高频细节" 信息。为描述这些高频信息，
# 人们定义了拉普拉斯金字塔(Laplacian Pyramid， LP)。
# 用高斯金字塔的每一层图像减去其上一层图像上采样并高斯卷积之后的预测图像，得到一系列的差值图像即为 LP 分解图像。
def lapalian_demo(image):
    pyramid_images = pyramid_demo(image)  # 做拉普拉斯金字塔必须用到高斯金字塔的结果
    level = len(pyramid_images)
    for i in range(level - 1, -1, -1):
        if (i - 1) < 0:
            expand = cv.pyrUp(pyramid_images[i], dstsize=image.shape[:2])
            lpls = cv.subtract(image, expand)
            cv.imshow("lapalian_down_" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i - 1].shape[:2])
            lpls = cv.subtract(pyramid_images[i - 1], expand)
            cv.imshow("lapalian_down_" + str(i), lpls)




# 图像金字塔做图像混合图像混合












"""图像金字塔是图像中多尺度表达的一种，最初用于机器视觉和图像压缩，最主要用于图像的分割、融合"""
if __name__ == "__main__":
    src = cv.imread('Fig/test.jpg')
    cv.namedWindow('input_image', cv.WINDOW_AUTOSIZE)  # 设置为WINDOW_NORMAL可以任意缩放
    cv.imshow('input_image', src)
    lapalian_demo(src)  # 拉普莱斯
    # pyramid_demo(src) # 高斯
    cv.waitKey(0)
    cv.destroyAllWindows()

    # 图像缩放的世界里，还有另外一种方式 - ---图像金字塔

# 高斯金字塔下采样时先做高斯模糊、再下采样，图像除了分辨率缩小之外、只包含了低频信息；
# 拉普拉斯金字塔通过源图像减去先缩小后(高斯金字塔下采样的低频图像)再放大的图像提取到源图像的高频残差，
# 可以帮助高斯金字塔下采样后的图像再上采样时的重建(复原)。