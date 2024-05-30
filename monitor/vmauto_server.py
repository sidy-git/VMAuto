import os
import time

from common.config_reader import ConfigReader
from common.log import Log
from monitor.wechat_im import WechatIm


class Command:
    keyword: str
    cmd: str

    def __init__(self, pkeyword, pcmd):
        self.keyword = pkeyword
        self.cmd = pcmd


commands = [
    Command("科技", "python main.py digital_gap.ini auto"),
    Command("截屏", "python monitor/screenshot.py"),
    Command("远程", "python monitor/mstsc.py")
]


def run():
    print("run VMAuto Server")
    # 定时监控微信im
    while 1:
        try:
            msg = WechatIm.wait_msg()
            if msg is None:
                print("获取不到新的指令，继续等待")
            else:
                find_flag = False
                for command in commands:
                    if msg.find(command.keyword) >= 0:
                        find_flag = True
                        send_context = "开始执行指令：" + command.keyword
                        WechatIm.send_msg_without_code(send_context)
                        print(send_context)
                        try:
                            ret = os.system(command.cmd)
                            if ret == 0:
                                Log.info("完成指令：" + command.keyword)
                            else:
                                Log.info("执行" + command.keyword + "失败，返回：" + str(ret))
                        except:
                            Log.info("执行指令异常: " + command.keyword)
                if not find_flag:
                    send_context = ""
                    index = 1
                    for cmd in commands:
                        send_context += str(index) + " " + cmd.keyword + "\r\n"
                        index += 1
                    Log.info("未找到该指令，目前支持指令如下：\r\n" + send_context)
        except:
            print("获取微信输入异常")
        time.sleep(5)


run()
