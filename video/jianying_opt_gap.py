# -*- coding: utf-8 -*-
# 调用剪映进行文生视频操作
import os
import sys
import time

from common.common_api import CommonApi
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt

# 启动剪映
url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
GuiOpt.click_icon(url_pre + "jianying_icon.png")
# GuiOpt.click_icon(url_pre + "jianying_icon2.png")
if not GuiOpt.wait_appear(url_pre + "jianying_ziyoubianjiwenan.png", 5):
    if GuiOpt.wait_appear(url_pre + "jianying_kaishichuangzuo.png", 20):
        GuiOpt.click_icon(url_pre + "jianying_tuwenchengpian.png")
        time.sleep(2)
        GuiOpt.click_icon(url_pre + "jianying_ziyoubianji.png")

context = GlobalVar.get("final_context")
if context is not None:
    print("生成视频文案: " + context)
    time.sleep(2)
    GuiOpt.paste()
    print(">>>>请确认文案是否需要修改，不需要修改请按<enter>，需要请在剪映中修改后继续")
    print(">>>>如需中断当前操作，请输入<N>")
    input_value = input()
    if input_value == "n" or input_value == "N":
        print("中断当前操作")
        exit(1)
    GuiOpt.click_icon(url_pre + "jianying_icon.png")
    # 兼容windows处理
    if CommonApi.get_os_type() == "win":
        GuiOpt.click_icon(url_pre + "jianying_tuwenchengpian2.png")

    GuiOpt.click_icon(url_pre + "jianying_shengchengshipin.png")
    GuiOpt.click_icon(url_pre + "jianying_zhinengpipei.png")
    print("视频生成中........")
    GuiOpt.wait_disappear(url_pre + "jianying_shengchengzhong.png", 120)
    print("视频生成成功")
else:
    print("获取视频文案失败")
