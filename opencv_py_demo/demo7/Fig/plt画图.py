
from matplotlib import pyplot as plt

"""   绘制子图有两种方法，一种是plt.subplot，另一种是plt.subplots    """


def subplot_n():
    # 使用plt.subplot来创建小图. plt.subplot(221)表示将整个图像窗口分为2行2列, 当前位置为1.
    plt.subplot(221)
    # plt.subplot(222)表示将整个图像窗口分为2行2列, 当前位置为2.
    plt.subplot(222) # 第一行的右图
    # plt.subplot(223)表示将整个图像窗口分为2行2列, 当前位置为3.
    plt.subplot(223)
    # plt.subplot(224)表示将整个图像窗口分为2行2列, 当前位置为4.
    plt.subplot(224)
    plt.show()


def figure_n():
    fig = plt.figure(figsize=(3, 3), dpi=300)  # 初始化一张画布
    plt.show()



if __name__ =="__main__":
    figure_n()
