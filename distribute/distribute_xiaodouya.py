import time
import pyperclip
from common.global_var import GlobalVar
from monitor.wechat_im import WechatIm
from pyauto.gui_opt import GuiOpt
from common.common_api import CommonApi


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


# 输入关键词
print(">>>>请输入分发关键词: （格式：#关键词1 #关键词2...），如复用之前关键词，请直接<enter>")
if GlobalVar.get("inputsrc") == "wechat":
    WechatIm.send_msg("请输入分发关键词: （格式：#关键词1 #关键词2...）")
    keywords = WechatIm.wait_msg()
else:
    keywords = input()
print("输入：" + keywords)
if keywords is not None and keywords != "":
    GlobalVar.add("keywords", keywords)
else:
    keywords = GlobalVar.get("keywords")
    keywords = keywords.replace("#", " #")
# 开始分发
GuiOpt.desktop()
GuiOpt.wait_appear(add_url("xiaodouya_icon.png"))
GuiOpt.click_icon(add_url("xiaodouya_icon.png"))
GuiOpt.double_click_icon(add_url("xiaodouya_icon.png"))
# 最大化
GuiOpt.windows_max()
time.sleep(2)
GuiOpt.click_icon(add_url("xiaodouya_yijianfabu.png"))
time.sleep(2)
if GuiOpt.find_icon(add_url("xiaodouya_yijianqingkong.png")):
    GuiOpt.click_icon(add_url("xiaodouya_yijianqingkong.png"))
    GuiOpt.click_icon(add_url("xiaodouya_querenqingkong.png"))
GuiOpt.click_icon(add_url("xiaodouya_fabushipin.png"))
# 上传视频和封面
# GuiOpt.click_icon(add_url("xiaodouya_tihuanshipin.png"))
GuiOpt.click_icon(add_url("xiaodouya_dakaishipin.png"))
GuiOpt.double_click_icon(add_url("xiaodouya_xuanzemulu.png"))
GuiOpt.double_click_icon(add_url("xiaodouya_xuanzeshipin.png"))
if not GuiOpt.wait_appear(add_url("xiaodouya_tongyongfabushezhi.png"), 20):
    print("视频上传失败")
    exit(-1)
print("视频上传成功")
time.sleep(2)
# 添加账号
GuiOpt.click_icon(add_url("xiaodouya_piliangtianjiazhanghao.png"))
GuiOpt.click_icon(add_url("xiaodouya_anfenzuxuanze.png"))
GuiOpt.click_icon(add_url("xiaodouya_zhanghaoqueding.png"))

# 修改标题和描述
GuiOpt.click_icon(add_url("xiaodouya_biaotishuru.png"))
# 获取标题并复制到剪贴板
title = None
mode = GlobalVar.get("mode")
if mode == "1":
    title = time.strftime("%y年%m月%d日科技快讯", time.localtime())
elif mode == "2":
    title = time.strftime("%y年%m月%d日科技信息差", time.localtime())
else:
    print("unknown mode: " + mode)
    exit(-1)
pyperclip.copy(title)
GuiOpt.select_all()
GuiOpt.paste()
# print("描述位置")
GuiOpt.click_icon(add_url("xiaodouya_tongyongfabushezhi.png"))
desp = title
if keywords is not None:
    desp = title + " " + keywords
pyperclip.copy(desp)
GuiOpt.select_all()
GuiOpt.paste()

# 发布
GuiOpt.click_icon(add_url("xiaodouya_yulanjifabu.png"))
time.sleep(2)
GuiOpt.move_to(1309, 970)
# GuiOpt.click_pos(1309, 970)

