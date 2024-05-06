import time
import numpy as np
from PIL import ImageGrab
import cv2
from moviepy.editor import VideoClip
from pygetwindow import PyGetWindow


def record_screen(duration):
    # 获取当前主窗口
    window = PyGetWindow.getActiveWindow()
    window_rect = window.rect

    # 初始化视频录制
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (window_rect.width, window_rect.height))

    # 录制屏幕
    start_time = time.time()
    while time.time() - start_time < duration:
        # 捕获屏幕区域
        screenshot = np.array(ImageGrab.grab(window_rect))
        out.write(screenshot)

        # 可以添加延时，防止CPU占用过高
        time.sleep(0.02)

    # 释放资源
    out.release()


# 开始录制，时长60秒
record_screen(60)