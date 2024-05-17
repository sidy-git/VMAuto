import datetime
import time

from common.common_api import CommonApi
from gui_opt import GuiOpt
from monitor.wechat_im import WechatIm


def add_url(file):
    url_pre = "monitor/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


# 打印当前时间
# time.sleep(3)
WechatIm.send_msg("Cidy", "hello world")
# print(WechatIm.get_last_msg("Cidy"))
print(WechatIm.wait_msg("Cidy", 30))
# WechatIm.send_msg("Cidy", "hello world")
# time.sleep(3)
# GuiOpt.find_icon(add_url("temp4.png"))
