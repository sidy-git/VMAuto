import time

from common.common_api import CommonApi
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt


def add_url(file):
    url_pre = "monitor/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


class WechatContactItem:
    name = ""
    icon = ""

    def __init__(self, p_name, p_icon):
        self.name = p_name
        self.icon = p_icon

class WechatIm:
    contact = [WechatContactItem("Cidy", add_url("head_cidy.png"))]
    name = "Cidy"

    @staticmethod
    def find_head_icon(name):
        for item in WechatIm.contact:
            if item.name == name:
                return item.icon
        print("can not find wechat contact name: " + name)
        return None

    @staticmethod
    def send_msg(context):
        verify_code = CommonApi.generate_captcha()
        verify_str = "code:" + verify_code + "\r\n"
        GlobalVar.add("verity_code", verify_code)
        context = verify_str + context
        WechatIm.send_msg_with_code(context)

    @staticmethod
    def send_msg_with_code(context):
        if not GuiOpt.find_icon(add_url("wechat_menu.png")):
            GuiOpt.click_icon(add_url("wechat_icon.png"))
        GuiOpt.windows_max()
        GuiOpt.click_icon(WechatIm.find_head_icon(WechatIm.name))
        GuiOpt.copy(context)
        GuiOpt.select_all()
        GuiOpt.paste()
        time.sleep(1)
        GuiOpt.click_icon(add_url("wechat_bnt_fasong.png"))
        GuiOpt.click_icon(add_url("wechat_icon.png"))

    @staticmethod
    # 发送的视频截图只能放置到视频目录的temp_export_video目录下
    def send_video(video_screenshot):
        if not GuiOpt.find_icon(add_url("wechat_menu.png")):
            GuiOpt.click_icon(add_url("wechat_icon.png"))
        GuiOpt.windows_max()
        GuiOpt.click_icon(WechatIm.find_head_icon(WechatIm.name))
        GuiOpt.click_icon(add_url("wechat_send_file.png"))
        if not GuiOpt.find_icon(add_url("wechat_shipin.png")):
            GuiOpt.double_click_icon(add_url("wechat_head_db.png"))
        GuiOpt.click_icon(add_url("wechat_shipin.png"))
        GuiOpt.double_click_icon(add_url("wechat_send_video.png"))
        GuiOpt.double_click_icon(video_screenshot)
        if GuiOpt.wait_appear(add_url("wechat_send_video_tanchuan.png")):
            GuiOpt.click_icon(add_url("wechat_video_send.png"))

    @staticmethod
    # 发送的图片截图只能放置到图片目录下
    def send_img(img_screenshot):
        if not GuiOpt.find_icon(add_url("wechat_menu.png")):
            GuiOpt.click_icon(add_url("wechat_icon.png"))
        GuiOpt.windows_max()
        GuiOpt.click_icon(WechatIm.find_head_icon(WechatIm.name))
        GuiOpt.click_icon(add_url("wechat_send_file.png"))
        if not GuiOpt.find_icon(add_url("wechat_tupian.png")):
            GuiOpt.double_click_icon(add_url("wechat_head_db.png"))
        GuiOpt.click_icon(add_url("wechat_tupian.png"))
        GuiOpt.double_click_icon(img_screenshot)
        if GuiOpt.wait_appear(add_url("wechat_tupian_tanchuang.png")):
            GuiOpt.click_icon(add_url("wechat_tupian_tanchuang.png"))

    @staticmethod
    def get_last_msg():
        GuiOpt.clear_clipboard()
        if not GuiOpt.find_icon(add_url("wechat_menu.png")):
            if GuiOpt.find_icon(add_url("wechat_icon.png")):
                GuiOpt.click_icon(add_url("wechat_icon.png"))
            elif GuiOpt.find_icon(add_url("wechat_icon2.png")):
                GuiOpt.click_icon(add_url("wechat_icon2.png"))
            else:
                print("获取微信icon失败")
                exit(-1)
            GuiOpt.windows_max()
        else:
            print("当前在微信界面")
        GuiOpt.click_icon(WechatIm.find_head_icon(WechatIm.name))
        x, y = GuiOpt.get_icon_pos(add_url("wechat_send_tool.png"))
        y = y - 45
        GuiOpt.double_click_pos(x, y)
        GuiOpt.copy()
        GuiOpt.click_icon(add_url("wechat_icon.png"))
        return GuiOpt.read_clipboard()

    @staticmethod
    def wait_msg(max_wait_sec=1800):
        verity_code = GlobalVar.get("verity_code")
        range = 5
        times = 0
        while times <= max_wait_sec:
            last_msg = str(WechatIm.get_last_msg())
            # print("last_msg: " + last_msg)
            if last_msg.find(verity_code) == 0:
                last_msg = last_msg.lstrip(verity_code).lstrip()
                print("获取微信输入：" + last_msg)
                return last_msg
            elif last_msg.find("0000") == 0:
                print("进入指令模式")
                last_msg = last_msg.lstrip(verity_code).lstrip()
                print("获取微信输入：" + last_msg)
                return last_msg
            elif len(last_msg) > 0:
                print("验证码核对错误，继续等待... wait seconds: " + str(times))
            else:
                print("未收到新的微信输入内容")
            time.sleep(range)
            times += range
        print("等待微信消息超时")
        exit(-1)

    @staticmethod
    def wait_save_video(save_screen, max_wait_sec=1800):
        range = 5
        times = 0
        while times <= max_wait_sec:
            if not GuiOpt.find_icon(add_url("wechat_menu.png")):
                if GuiOpt.find_icon(add_url("wechat_icon.png")):
                    GuiOpt.click_icon(add_url("wechat_icon.png"))
                elif GuiOpt.find_icon(add_url("wechat_icon2.png")):
                    GuiOpt.click_icon(add_url("wechat_icon2.png"))
                else:
                    print("获取微信icon失败")
                    exit(-1)
                GuiOpt.windows_max()
            else:
                print("当前在微信界面")
            GuiOpt.click_icon(WechatIm.find_head_icon(WechatIm.name))
            x, y = GuiOpt.get_icon_pos(add_url("wechat_send_tool.png"))
            y = y - 45
            GuiOpt.move_to(x, y)
            GuiOpt.r_click_pos(x, y)
            if GuiOpt.find_icon(add_url("wechat_saveas.png")):
                GuiOpt.click_icon(add_url("wechat_saveas.png"))
                if not GuiOpt.find_icon(add_url("wechat_shipin.png")):
                    GuiOpt.double_click_icon(add_url("wechat_saveas_head_db.png"))
                GuiOpt.click_icon(add_url("wechat_shipin.png"))
                GuiOpt.double_click_icon(add_url("wechat_send_video.png"))
                GuiOpt.double_click_icon(add_url(save_screen))
                if GuiOpt.find_icon(add_url("wechat_saveas_fugai.png")):
                    GuiOpt.click_icon(add_url("wechat_saveas_fugai.png"))
                    print("视频保存成功")
                    break
            else:
                GuiOpt.esc()
                print("未收到视频，继续等待: " + str(times))
            time.sleep(range)
            times += range
        print("等待微信消息超时")
        exit(-1)

