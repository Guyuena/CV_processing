import numpy as np
import cv2 as cv

def f1():
    face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')
    img = cv.imread('Fig/liu2.png')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv.imshow('img', img)
    cv.waitKey(0)
    cv.destroyAllWindows()



# 视频流中检测
def f2():
    cap = cv.VideoCapture(0)  # 例化相机设备
    face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('haarcascades/haarcascade_eye.xml')
    while (1):
        # Take each frame 提取每一视频帧
        _, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv.imshow('frame', frame)
        k = cv.waitKey(5) & 0xFF
        if k == 27:  # 用户按下 ESC(ASCII码为27)
            break



if __name__ == "__main__":
    # f1()
    f2()
