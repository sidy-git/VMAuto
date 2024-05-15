import time
import pyperclip
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt
from common.common_api import CommonApi


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


# 输入关键词
print("请输入分发关键词: （格式：#关键词1 #关键词2...），如复用之前关键词，请直接<enter>")
keywords = input()
print("输入：" + keywords)
if keywords is not None and keywords != "":
    GlobalVar.add("keywords", keywords)
else:
    keywords = GlobalVar.get("keywords")
    keywords = keywords.replace("#", " #")
# 开始分发
GuiOpt.desktop()
GuiOpt.click_icon(add_url("xiaodouya_icon.png"))
GuiOpt.double_click_icon(add_url("xiaodouya_icon.png"))
# 最大化
GuiOpt.windows_max()
GuiOpt.click_icon(add_url("xiaodouya_yijianfabu.png"))
GuiOpt.click_icon(add_url("xiaodouya_fabushipin.png"))
# 添加账号
GuiOpt.click_icon(add_url("xiaodouya_tianjiazhanghao.png"))
GuiOpt.click_icon(add_url("xiaodouya_anfenzuxuanze.png"))
GuiOpt.click_icon(add_url("xiaodouya_zhanghaoqueding.png"))
# 上传视频和封面
GuiOpt.click_icon(add_url("xiaodouya_tihuanshipin.png"))
GuiOpt.click_icon(add_url("xiaodouya_dakaishipin.png"))
GuiOpt.double_click_icon(add_url("xiaodouya_xuanzemulu.png"))
GuiOpt.double_click_icon(add_url("xiaodouya_xuanzeshipin.png"))
if not GuiOpt.wait_appear(add_url("xiaodouya_fengmianshangchuanchenggong.png"), 20):
    print("视频上传失败")
    exit(-1)

print("视频上传成功")
time.sleep(2)
# print("上传封面位置")
# GuiOpt.find_icon(add_url("temp_shangchuangfengmian.png"))
GuiOpt.click_pos(731, 661)
GuiOpt.double_click_icon(add_url("xiaodouya_xuanzefengmian.png"))
# print("标题位置")
# GuiOpt.find_icon(add_url("temp_yijianshezhibiaoti.png"))
GuiOpt.click_pos(578, 775)
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
# GuiOpt.find_icon(add_url("temp_yijianshezhijianjie.png"))
GuiOpt.click_pos(675, 854)
desp = title
if keywords is not None:
    desp = title + " " + keywords
pyperclip.copy(desp)
GuiOpt.select_all()
GuiOpt.paste()

# 发布
GuiOpt.click_icon(add_url("xiaodouya_tianjiadaoyouce.png"))
GuiOpt.click_icon(add_url("xiaodouya_yijianfabu2.png"))
time.sleep(2)
# 裁剪图片
if GuiOpt.find_icon(add_url("xiaodouya_jianchacanshu.png")):
    GuiOpt.esc()
    # print("裁剪图片位置:")
    # GuiOpt.find_icon(add_url("temp_caijianfengmian.png"))
    # 小红书封面裁剪
    GuiOpt.click_icon(add_url("xiaodouya_xiaohongshu_icon.png"))
    GuiOpt.move_to(1323, 330)
    GuiOpt.click_pos(1323, 330)
    GuiOpt.click_icon(add_url("xiaodouya_queding.png"))
    time.sleep(1)
    # 视频号封面裁剪
    GuiOpt.click_icon(add_url("xiaodouya_shipinhao_icon.png"))
    GuiOpt.move_to(1323, 330)
    GuiOpt.click_pos(1323, 330)
    GuiOpt.click_icon(add_url("xiaodouya_queding.png"))
# GuiOpt.click_icon(add_url("xiaodouya_yijianfabu2.png"))

