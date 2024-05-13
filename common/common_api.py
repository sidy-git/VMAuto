import os
import platform


class CommonApi:
    # 获取操作系统类型
    @staticmethod
    def get_os_type():
        if os.name == 'nt':
            return 'win'
        elif os.name == 'posix':
            if 'darwin' in platform.system().lower():
                return 'mac'
            else:
                return 'Linux'
        else:
            return 'Unknown'
