import time
import pyperclip

from common.config_reader import ConfigReader
from common.global_var import GlobalVar
from monitor.wechat_im import WechatIm
from pyauto.gui_opt import GuiOpt
from common.common_api import CommonApi


def add_url(file):
    url_pre = "monitor/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


if GlobalVar.get("inputSrc") == "wechat":
    # 微信发送视频
    WechatIm.send_video(add_url("wechat_send_video2.png"))
    WechatIm.send_msg("请确认是否直接使用该视频，如需更换回复<否>并发送新视频，否则回复验证码或<是>")
    response = WechatIm.wait_msg()
    if response == "否":
        # 等待接收新视频
        WechatIm.wait_save_video("wechat_send_video2.png")
else:
    print("非微信交互模式，跳过该步骤")
