import time

from common.common_api import CommonApi
from gui_opt import GuiOpt


def add_url(file):
    url_pre = "video/pic/" + CommonApi.get_os_type() + "/"
    return url_pre + file

print("run")
time.sleep(1800)

# GuiOpt.find_icon(add_url("jianying_fengmian.png"))