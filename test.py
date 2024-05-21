import datetime
import time

from common.common_api import CommonApi
from common.global_var import GlobalVar
from gui_opt import GuiOpt
from monitor.wechat_im import WechatIm


def add_url(file):
    url_pre = "monitor/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


# 打印当前时间
# time.sleep(3)
# title = time.strftime("%Y年%m月%d日科技快讯", time.localtime())
# print(title)
# WechatIm.send_msg("Cidy", "hello world")
# print(WechatIm.get_last_msg("Cidy"))
# print(WechatIm.wait_msg("Cidy", 30))
# WechatIm.send_msg("Cidy", "hello world")
# time.sleep(3)
# GuiOpt.find_icon(add_url("temp4.png"))
# save_dir = GlobalVar.get("imgsavedir") + "\\temp_screenshot.png"
# GuiOpt.save_screenshot(save_dir)
# picture_dir = "C:\\Users\\Administrator\\Pictures\\temp_screenshot.png"
# CommonApi.copy_file(save_dir, picture_dir)
# WechatIm.send_msg("xiaodouya_temp_screenshot.png")

