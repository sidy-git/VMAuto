import time
import pyperclip

from common.config_reader import ConfigReader
from common.global_var import GlobalVar
from common.public_function import PublicFunction
from monitor.wechat_im import WechatIm
from pyauto.gui_opt import GuiOpt
from common.common_api import CommonApi


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


def open_xiaodouya():
    GuiOpt.desktop()
    GuiOpt.wait_appear(add_url("xiaodouya_icon.png"))
    GuiOpt.click_icon(add_url("xiaodouya_icon.png"))
    GuiOpt.double_click_icon(add_url("xiaodouya_icon.png"))

# 开始分发
open_xiaodouya()
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
title = GlobalVar.get("title")
GuiOpt.click_icon(add_url("xiaodouya_biaotishuru.png"))
# 获取标题并复制到剪贴板
pyperclip.copy(title)
GuiOpt.select_all()
GuiOpt.paste()
GuiOpt.click_icon(add_url("xiaodouya_tongyongfabushezhi.png"))
# 获取描述信息
desp = GlobalVar.get("description")
pyperclip.copy(desp)
GuiOpt.select_all()
GuiOpt.paste()

# 发布
GuiOpt.click_icon(add_url("xiaodouya_yulanjifabu.png"))
time.sleep(2)
# 检查是否存在登录失效
max_time = 5
while max_time > 0 and GuiOpt.find_icon(add_url("xiaodouya_denglushixiao.png")):
    print("发现账号登录异常: " + str(max_time))
    GuiOpt.click_icon(add_url("xiaodouya_denglushixiao.png"))
    time.sleep(5)
    if GlobalVar.get("inputSrc") == "wechat":
        PublicFunction.screenshot_send()
        WechatIm.send_msg("扫码完成请发送<完成>")
        response = WechatIm.wait_msg()
        if response == "完成":
            print("扫码完成")
            open_xiaodouya()
        else:
            print("输入错误")
            exit(-1)
    else:
        print("扫码完成请输入<enter>")
    max_time -= 1

# 确认发布
GuiOpt.move_to(1309, 970)
GuiOpt.click_pos(1309, 970)
time.sleep(5)
GuiOpt.find_icon(add_url("xiaodouya_fabuzhipingtai.png"))
# GuiOpt.click_icon(add_url("xiaodouya_fabuzhipingtai.png"))
time.sleep(3)
GuiOpt.desktop()

# 发布失败处理
