import os
import time

from common.common_api import CommonApi
from common.public_function import PublicFunction
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
time.sleep(2)
if GuiOpt.find_icon(add_url("xiaodouya_icon.png")):
    GuiOpt.double_click_icon(add_url("xiaodouya_icon.png"))
elif GuiOpt.find_icon(add_url("xiaodouya_icon2.png")):
    GuiOpt.double_click_icon(add_url("xiaodouya_icon2.png"))
else:
    exit(-1)
time.sleep(2)

# 小豆芽是否登录失效
if GuiOpt.find_icon(add_url("xiaodouya_zhanghaodenglushixiao.png")):
    GuiOpt.click_icon(add_url("xiaodouya_zhanghaodenglushixiao.png"))
    time.sleep(3)
    PublicFunction.screenshot_send()
    WechatIm.send_msg("小豆芽账号登录失效，请扫码后回复验证码")
    PublicFunction.wait_verify_code()
else:
    GuiOpt.esc()
    GuiOpt.esc()
    if GuiOpt.find_icon(add_url("xiaodouya_fabujilu.png")):
        GuiOpt.click_icon(add_url("xiaodouya_fabujilu.png"))


# 恢复剪映界面状态
if GuiOpt.find_icon(add_url("jianying_icon.png")):
    GuiOpt.click_icon(add_url("jianying_icon.png"))
    time.sleep(3)
    GuiOpt.windows_max()
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
        time.sleep(3)
if not GuiOpt.find_icon(add_url("jinagying_shouyecaidan.png")):
    GuiOpt.desktop()
    time.sleep(2)
    GuiOpt.double_click_icon(add_url("jianying_desktop_icon.png"))
    GuiOpt.wait_appear(add_url("jianying_xiankashengji.png"), 30)
    if GuiOpt.find_icon(add_url("jianying_xiankashengji.png")):
        GuiOpt.click_icon(add_url("jianying_xiankashengji.png"))
    GuiOpt.wait_appear(add_url("jinagying_shouyecaidan.png"))
GuiOpt.windows_max()
GuiOpt.click_icon(add_url("jianying_pycharm_icon.png"))
