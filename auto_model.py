# -*- coding: utf-8 -*-
# 自动运行模式
import configparser
import datetime
import os
import sys
from common.global_var import GlobalVar
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def auto_run(cfg_file):
    # 启动运行
    print("config file: ",  cfg_file)
    config = configparser.ConfigParser()
    config.read(cfg_file, encoding="utf-8")

    theme = config.get('info', 'theme')
    print("主题: ", theme)
    # 判断用上午还是下午模式
    # 获取当前时间
    current_time = datetime.datetime.now()
    if current_time.hour < 12:
        print("启用模式1")
        GlobalVar.add("mode", 1)
    else:
        print("启用模式2")
        GlobalVar.add("mode", 2)

    # 开始脚本执行
    scriptconfigs = config.options("scripts")
    for option in scriptconfigs:
        item = config.get("scripts", option).split(",")
        script_name = item[0]
        script_path = item[1]
        print("开始运行" + script_name)
        ret = os.system("python " + script_path)
        if ret == 0:
            print("完成" + script_name)
        else:
            print("执行" + script_name + "失败，返回：" + str(ret))
            break

