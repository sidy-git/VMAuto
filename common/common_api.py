import os
import platform
import random
import shutil

from common.global_var import GlobalVar


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

    @staticmethod
    def copy_files(source_folder, destination_folder):
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        for filename in os.listdir(source_folder):
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            if os.path.isfile(source_file):
                shutil.copy2(source_file, destination_folder)
                print(f"Copied {source_file} to {destination_folder}")

    @staticmethod
    def remove_directory(directory):
        try:
            shutil.rmtree(directory)
            print("目录删除成功")
        except OSError as e:
            print("目录删除失败：", e)

    @staticmethod
    def generate_captcha(length=4):
        captcha = ''
        for _ in range(4):
            captcha += str(random.randint(0, 9))
        return captcha

