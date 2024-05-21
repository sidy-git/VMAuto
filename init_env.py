import os
import time

from common.common_api import CommonApi
from monitor.wechat_im import WechatIm
from pyauto.gui_opt import GuiOpt


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


# 把当前路径添加到系统路径
curPath = os.path.dirname(os.path.abspath(__file__))
print("curPath: " + curPath)
ret = os.system("set path=%path%;" + curPath)

# 恢复小豆芽界面状态
GuiOpt.desktop()
GuiOpt.double_click_icon(add_url("xiaodouya_icon.png"))
time.sleep(2)
if GuiOpt.find_icon(add_url("xiaodouya_fabujilu.png")):
    GuiOpt.click_icon(add_url("xiaodouya_fabujilu.png"))

# 恢复剪映界面状态
GuiOpt.click_icon(add_url("jianying_icon.png"))
if CommonApi.get_os_type() == "win":
    # 关闭图文成片窗口
    if GuiOpt.find_icon(add_url("jianying_tuwenchengpian2.png")):
        GuiOpt.click_icon(add_url("jianying_tuwenchengpian2.png"))
        # GuiOpt.find_icon(add_url("temp_close.png"))
        GuiOpt.click_pos(1429, 212)
    # 关闭导出成功窗口
    if GuiOpt.find_icon(add_url("jianying_daochuchenggong.png")):
        GuiOpt.click_icon(add_url("jianying_close.png"))
    # 关闭导出窗口
    if GuiOpt.find_icon(add_url("jianying_daochuchuangkou.png")):
        GuiOpt.esc()
    # 关闭视频编辑窗口
    if GuiOpt.find_icon(add_url("jianying_bianjicaidan.png")):
        # GuiOpt.find_icon(add_url("temp_close2.png"))
        GuiOpt.click_pos(1904, 17)
GuiOpt.click_icon(add_url("jianying_pycharm_icon.png"))
