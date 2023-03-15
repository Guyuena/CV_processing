import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
count=2
while(True):
# while(count):
    # 一帧一帧捕捉
    ret, frame = cap.read()
    print("摄像头捕获是否成功： ",ret)
    # 我们对帧的操作在这里
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 显示返回的每帧
    # cv.imshow('frame',gray)
    cv.imshow('frame',frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

    # count = count -1
# 当所有事完成，释放 VideoCapture 对象
cap.release()
cv.destroyAllWindows()