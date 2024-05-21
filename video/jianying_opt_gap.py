# -*- coding: utf-8 -*-
# 调用剪映进行文生视频操作
import os
import sys
import time

from common.common_api import CommonApi
from common.config_reader import ConfigReader
from monitor.wechat_im import WechatIm

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


# 文案确认
context = GlobalVar.get("final_context")
if context is not None:
    print("生成视频文案: " + context)
    if ConfigReader.get("config", "inputsrc") == "wechat":
        tempContext = GuiOpt.read_clipboard()
        if tempContext is not None and tempContext != "":
            WechatIm.send_msg(tempContext)
        context = WechatIm.wait_msg()
        GlobalVar.add("final_context", context)
    GuiOpt.copy(context)

# 启动剪映
GuiOpt.click_icon(add_url( "jianying_icon.png"))
# GuiOpt.click_icon(add_url( "jianying_icon2.png"))
if not GuiOpt.find_icon(add_url("jianying_ziyoubianjiwenan.png")):
    if GuiOpt.wait_appear(add_url("jianying_kaishichuangzuo.png"), 20):
        GuiOpt.click_icon(add_url("jianying_tuwenchengpian.png"))
        GuiOpt.wait_appear(add_url("jianying_ziyoubianji.png"), 10)
        GuiOpt.click_icon(add_url("jianying_ziyoubianji.png"))

    time.sleep(2)
    GuiOpt.paste()
    print(">>>>请确认文案是否需要修改，不需要修改请按<enter>，需要请在剪映中修改后继续")
    print(">>>>如需中断当前操作，请输入<N>")
    input_value = ""
    if not ConfigReader.get("config", "inputsrc") == "wechat":
        input_value = input()
        GuiOpt.click_icon(add_url("jianying_icon.png"))
        # 兼容windows处理
        if CommonApi.get_os_type() == "win":
            GuiOpt.click_icon(add_url("jianying_tuwenchengpian2.png"))
    if input_value == "n" or input_value == "N":
        print("中断当前操作")
        exit(1)
    time.sleep(1)
    GuiOpt.click_icon(add_url("jianying_shengchengshipin.png"))
    GuiOpt.click_icon(add_url("jianying_zhinengpipei.png"))
    print("视频生成中........")
    GuiOpt.wait_disappear(add_url("jianying_shengchengzhong.png"), 120)
    print("视频生成成功")
    time.sleep(3)
else:
    print("获取视频文案失败")
