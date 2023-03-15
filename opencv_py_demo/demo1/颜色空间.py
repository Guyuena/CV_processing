import cv2 as cv
# 查看所有颜色空间关键字
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( flags )