from common.common_api import CommonApi
from common.config_reader import ConfigReader
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt
from monitor.wechat_im import WechatIm


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file


def run():
    WechatIm.esc_wechat()
    ConfigReader.init("C:\\Users\\Administrator\\PycharmProjects\\VMAuto\\config\\win\\digital_gap.ini")
    pic_dir = ConfigReader.get("path", "pic_dir")
    if pic_dir is None:
        print("获取截图保存路径失败")
        exit(-1)
    pic_dir = pic_dir + "\\temp_screenshot.png"
    print("截屏保存路径：" + pic_dir)
    GuiOpt.save_screenshot(pic_dir)
    WechatIm.send_img(add_url("xiaodouya_temp_screenshot.png"))


run()
