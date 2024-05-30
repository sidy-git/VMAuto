import time
import pyperclip

from common.config_reader import ConfigReader
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt
from common.common_api import CommonApi


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


# 导出视频
print(">>>>开始进行视频剪辑，如剪辑完成，按<enter>进行视频导出及后续步骤")
if not GlobalVar.get("inputSrc") == "wechat":
    input()
GuiOpt.click_icon(add_url("jianying_icon.png"))
GuiOpt.click_icon(add_url("jianying_daochu.png"))
GuiOpt.wait_appear(add_url("jianying_daochuchuangkou.png"))
# GuiOpt.find_icon(url_pre + "wechat_bnt_fasong.png"
GuiOpt.move_to(1131, 253)
GuiOpt.click_pos(1131, 253)
GuiOpt.select_all()
export_dir_name = "temp_export_video"
pyperclip.copy(export_dir_name)
GuiOpt.paste()
time.sleep(2)
GuiOpt.click_pos(1148, 817)
time.sleep(2)
if GuiOpt.find_icon(add_url("jianying_daochuchongfu.png")):
    GuiOpt.enter()
if GuiOpt.wait_appear(add_url("jianying_daochuchenggong.png"), 300):
    print("视频导出成功")
    GuiOpt.click_icon(add_url("jianying_pycharm_icon.png"))
else:
    print("视频导出失败")
    exit(-1)
