import cv2 as cv
cap = cv.VideoCapture(0)
while (1):
    ret, img = cap.read()

    fps = cap.get(cv.CAP_PROP_FPS)
    print(fps)

    # 图片 添加的文字 位置 字体 字体大小 字体颜色 字体粗细
    cv.putText(img, fps, (5,50 ), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
    cv.imshow("image", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()


