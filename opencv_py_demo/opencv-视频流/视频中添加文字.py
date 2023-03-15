import cv2
from PIL import Image, ImageDraw, ImageFont
import numpy as np

cap = cv2.VideoCapture('video.avi')  # 读取视频

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 360))  # 输出视频参数设置

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # 在 frame 上显示一些信息
        img_PIL = Image.fromarray(frame[..., ::-1])  # 转成 array
        font = ImageFont.truetype('STZHONGS.TTF', 40)  # 字体设置，Windows系统可以在 "C:\Windows\Fonts" 下查找
        text1 = "机器视觉CV"
        text2 = "目标检测DEMO"
        for i, te in enumerate(text1):
            position = (50, 20 + i * 50)
            draw = ImageDraw.Draw(img_PIL)
            draw.text(position, te, font=font, fill=(255, 0, 0))

        for i, te in enumerate(text2):
            position = (520, 10 + i * 40)
            draw = ImageDraw.Draw(img_PIL)
            draw.text(position, te, font=font, fill=(255, 0, 0))
        frame = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
        # write the frame
        cv2.imshow('frame', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()