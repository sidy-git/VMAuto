
from common.global_var import GlobalVar
from pyauto.gui_opt import GuiOpt
from monitor.wechat_im import WechatIm


class Log:
    @staticmethod
    def info(context):
        # 缓存剪切板内容
        temp_clipboard = GuiOpt.read_clipboard()
        if GlobalVar.get("inputSrc") == "wechat":
            WechatIm.send_msg_without_code(context)
        print(context)
        # 还原剪切板内容
        GuiOpt.copy(temp_clipboard)
