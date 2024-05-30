# -*- coding: utf-8 -*-
import time
import pyautogui
import pyperclip

from common.common_api import CommonApi


# GUI 操作类
class GuiOpt:

    @staticmethod
    def click_icon(icon_path):
        # print("icon_path: " + icon_path)
        x, y = pyautogui.locateCenterOnScreen(icon_path, confidence=0.7)
        pyautogui.moveTo(x,y)
        time.sleep(1)
        pyautogui.click(x, y)
        time.sleep(1)

    @staticmethod
    def move_to(x, y):
        pyautogui.moveTo(x, y)
        time.sleep(1)

    @staticmethod
    def click_pos(x, y):
        pyautogui.click(x, y)
        time.sleep(1)

    @staticmethod
    def r_click_pos(x, y):
        pyautogui.rightClick(x, y)
        time.sleep(1)

    @staticmethod
    def double_click_pos(x, y):
        pyautogui.doubleClick(x, y)
        time.sleep(1)

    @staticmethod
    def double_click_icon(icon_path):
        x, y = pyautogui.locateCenterOnScreen(icon_path, confidence=0.7)
        pyautogui.moveTo(x, y)
        time.sleep(1)
        pyautogui.doubleClick(x, y)
        time.sleep(1)

    @staticmethod
    def find_icon(icon_path):
        x = None
        y = None
        try:
            x, y = pyautogui.locateCenterOnScreen(icon_path, confidence=0.7)
        except pyautogui.ImageNotFoundException:
            print("can not find icon: " + icon_path)
            return False
        # print("find icon: " + icon_path + " x=" + str(x) + ", y=" + str(y))
        pyautogui.moveTo(x, y)
        return True

    @staticmethod
    def get_icon_pos(icon_path):
        x = None
        y = None
        try:
            x, y = pyautogui.locateCenterOnScreen(icon_path, confidence=0.7)
        except pyautogui.ImageNotFoundException:
            print("can not find icon: " + icon_path)
            return None, None
        # print("get icon: " + icon_path + " x=" + str(x) + ", y=" + str(y))
        pyautogui.moveTo(x, y)
        return x, y

    @staticmethod
    def input(string):
        print("开始输入: " + string)
        pyautogui.typewrite(string)

    @staticmethod
    def copy(context=None):
        if context is None:
            if CommonApi.get_os_type() == "win":
                pyautogui.hotkey('ctrl', 'c')
            else:
                pyautogui.hotkey('command', 'c')
        else:
            pyperclip.copy(context)

    @staticmethod
    def read_clipboard():
        return pyperclip.paste()

    @staticmethod
    def clear_clipboard():
        pyperclip.copy("")

    @staticmethod
    def paste():
        if CommonApi.get_os_type() == "win":
            pyautogui.hotkey('ctrl', 'v')
        else:
            pyautogui.hotkey('command', 'v')

    @staticmethod
    def hot_key(*args: str):
        pyautogui.hotkey(*args)

    @staticmethod
    def select_all():
        if CommonApi.get_os_type() == "win":
            pyautogui.hotkey('ctrl', 'a')
        else:
            pyautogui.hotkey('command', 'a')

    @staticmethod
    def desktop():
        if CommonApi.get_os_type() == "win":
            pyautogui.hotkey('win', 'd')
        else:
            pyautogui.hotkey('command', 'd')

    @staticmethod
    def windows_max():
        if CommonApi.get_os_type() == "win":
            pyautogui.hotkey('win', 'up')
        else:
            pyautogui.hotkey('command', 'up')

    @staticmethod
    def enter():
        if CommonApi.get_os_type() == "win":
            pyautogui.press('enter')
        else:
            pyautogui.press('enter')

    @staticmethod
    def esc():
        if CommonApi.get_os_type() == "win":
            pyautogui.press('esc')
        else:
            pyautogui.press('esc')
        time.sleep(1)

    @staticmethod
    def wait_appear(icon_path, max_sec=10):
        # 统计频度
        range_sec = 5
        sec = range_sec
        location = None
        while 1:
            if sec > max_sec:
                print("等待超时")
                return False
            try:
                location = pyautogui.locateOnScreen(icon_path, confidence=0.7)
            except pyautogui.ImageNotFoundException:
                print("wait time: " + str(sec))
                location = None
                time.sleep(range_sec)
                sec += range_sec
            if location is not None:
                print("图片出现: " + icon_path + ", 位置: " + str(location.left) + ", " + str(location.top))
                break
        return True

    @staticmethod
    def wait_disappear(icon_path, max_sec):
        # 统计频度
        range_sec = 5
        sec = range_sec
        location = None
        while 1:
            if sec > max_sec:
                print("等待超时")
                break
            try:
                location = pyautogui.locateOnScreen(icon_path, confidence=0.7)
            except pyautogui.ImageNotFoundException:
                location = None

            if location is None:
                print("图片消失")
                break
            else:
                time.sleep(range_sec)
                print("wait time: " + str(sec) + " seconds")
                sec += range_sec

    @staticmethod
    def save_screenshot(save_dir, x1=0, y1=0, x2=1902, y2=1080):
        img = pyautogui.screenshot(region=[x1, y1, x2, y2])
        # img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img.save(save_dir)


# GuiOpt.click_icon("jianying_icon.png")
# time.sleep(3)
# GuiOpt.find_icon("jianying_shengchengshipin.png")
# time.sleep(4)
# GuiOpt.input("/Users/liushaocai110100/Documents/PycharmProjects/VMAuto/.venv/bin/python /Users/liushaocai110100/Documents/PycharmProjects/VMAuto/pyauto/gui_opt.py ")
# time.sleep(2)
# GuiOpt.paste()


# time.sleep(5)
# GuiOpt.wait_disappear("test_wait.png", 20)
# GuiOpt.screenshot("C:\\Users\\Administrator\\Videos\\temp_export_video\\screenshot.png")
