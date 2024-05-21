import os

from monitor.wechat_im import WechatIm

class Command:
    keyword: str
    cmd: str

    def __init__(self, pkeyword, pcmd):
        self.keyword = pkeyword
        self.cmd = pcmd

commands = [
    Command("制作科技数码", "python main.py digital_gap.ini")
]
def run():
    print("run VMAuto Server")
    # 定时监控微信im
    while 1:
        msg = WechatIm.wait_msg()
        if msg is None:
            print("获取不到新的指令，继续等待")
        else:
            find_flag = False
            for command in commands:
                if msg.find(command.keyword) >= 0:
                    find_flag = True
                    send_context = "开始执行指令：" + command.keyword
                    WechatIm.send_msg(send_context)
                    print(send_context)
                    try:
                        ret = os.system(command.cmd)
                        if ret == 0:
                            print("完成指令：" + command.keyword)
                        else:
                            print("执行" + command.keyword + "失败，返回：" + str(ret))
                    except:
                        print("执行指令异常: " + command.keyword)
            if not find_flag:
                send_context = ""
                index = 1
                for cmd in commands:
                    send_context += str(index) + " " + cmd.keyword + "\r\n"
                WechatIm.send_msg("未找到该指令，目前支持指令如下：\r\n" + send_context)


run()
