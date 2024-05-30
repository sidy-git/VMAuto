import time

from common.common_api import CommonApi
from common.config_reader import ConfigReader
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt
from monitor.wechat_im import WechatIm


def add_url(file):
    url_pre = "monitor/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


def run():
    GuiOpt.desktop()
    if GuiOpt.find_icon(add_url("qq_icon.png")):
        GuiOpt.click_icon(add_url("qq_icon.png"))
    else:
        exit(-1)
    time.sleep(3)
    if GuiOpt.find_icon(add_url("qq_head_cidy_2.png")):
        print("已在目标会话中")
    elif GuiOpt.find_icon(add_url("qq_head_cidy.png")):
        GuiOpt.click_icon(add_url("qq_head_cidy.png"))
    GuiOpt.click_icon(add_url("qq_im_yuancheng.png"))
    GuiOpt.click_icon(add_url("qq_im_yuanchengxiezhu.png"))
    time.sleep(3)
    if GuiOpt.find_icon(add_url("qq_yuanchengdengdai.png")):
        WechatIm.send_msg_without_code("已启动QQ远程协助，请在QQ中接收邀请")
    else:
        exit(-1)


run()
