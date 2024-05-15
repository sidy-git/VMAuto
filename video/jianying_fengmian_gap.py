# -*- coding: utf-8 -*-
# 调用剪映进行文生视频操作
import os
import sys
import time

import pyperclip

from common.common_api import CommonApi

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt

# 启动剪映
url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
GuiOpt.click_icon(url_pre + "jianying_icon.png")
# GuiOpt.click_icon(url_pre + "jianying_icon2.png")
GuiOpt.click_icon(url_pre + "jianying_fengmian.png")
GuiOpt.click_icon(url_pre + "jianying_bendi.png")
GuiOpt.click_icon(url_pre + "jianying_tupianshangchuan.png")
GuiOpt.click_icon(url_pre + "jianying_zhuomian.png")
# 根据模式选用不同封面
mode = GlobalVar.get("mode")
if mode == "1":
    GuiOpt.click_icon(url_pre + "jianying_head_pic1.png")
    GuiOpt.double_click_icon(url_pre + "jianying_head_pic1_db.png")
elif mode == "2":
    GuiOpt.click_icon(url_pre + "jianying_head_pic2.png")
    GuiOpt.double_click_icon(url_pre + "jianying_head_pic2_db.png")
else:
    print("unknow mode: " + mode)
    exit(-1)
if CommonApi.get_os_type() == "mac":
    GuiOpt.click_icon(url_pre + "jianying_dakai.png")
GuiOpt.click_icon(url_pre + "jianying_qubianji.png")
GuiOpt.click_icon(url_pre + "jianying_wenben.png")
GuiOpt.click_icon(url_pre + "jianying_morenwenben.png")
GuiOpt.click_icon(url_pre + "jianying_morenwenben_input.png")
# 获取标题并复制到剪贴板
if mode == "1":
    title = GlobalVar.get("head_pic_title1")
elif mode == "2":
    title = GlobalVar.get("head_pic_title2") + "\r\n信息差"
else:
    print("unknow mode: " + mode)
    exit(-1)
if title is None:
    print("get title failed")
    exit(-1)
# title = time.strftime("%m月%d日", time.localtime()) + "\r\n" + title
pyperclip.copy(title)
GuiOpt.double_click_icon(url_pre + "jianying_morenwenben_input.png")
GuiOpt.paste()
GuiOpt.click_icon(url_pre + "jianying_wanchengshezhi.png")

# 导入图片
if CommonApi.get_os_type() == "win":
    srcpath = GlobalVar.get("imgsavedir")
    destpath = "C:\\Users\\Administrator\\Desktop\\temp_del"
    if os.path.exists(destpath):
        print("存在同名目录，正在删除: " + destpath)
        CommonApi.remove_directory(destpath)
    else:
        os.mkdir(destpath)
    CommonApi.copy_files(srcpath, destpath)
    GuiOpt.click_icon(url_pre + "jianying_daoru.png")
    GuiOpt.click_icon(url_pre + "jianying_zhuomian.png")
    GuiOpt.double_click_icon(url_pre + "jianying_temp_del.png")
    GuiOpt.select_all()
    GuiOpt.click_icon(url_pre + "jianying_dakai2.png")

