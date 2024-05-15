import time
import pyperclip
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt
from common.common_api import CommonApi


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


# 导出视频
input()
GuiOpt.click_icon(add_url("jianying_icon.png"))
GuiOpt.click_icon(add_url("jianying_daochu.png"))
GuiOpt.wait_appear(add_url("jianying_daochuchuangkou.png"), 10)
# GuiOpt.find_icon(url_pre + "temp.png"
GuiOpt.move_to(1131, 253)
GuiOpt.click_pos(1131, 253)
GuiOpt.select_all()
export_dir_name = "temp_export_video"
pyperclip.copy(export_dir_name)
GuiOpt.paste()
GuiOpt.click_icon(add_url("jianying_daochu2.png"))
time.sleep(2)
if GuiOpt.find_icon(add_url("jianying_daochuchongfu.png")):
    GuiOpt.enter()
if GuiOpt.wait_appear(add_url("jianying_daochuchenggong.png"), 300):
    print("视频导出成功")
else:
    print("视频导出失败")
    exit(-1)
