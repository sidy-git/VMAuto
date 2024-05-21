# -*- coding: utf-8 -*-
# 自动运行模式
import configparser
import datetime
import os
import sys

from common.config_reader import ConfigReader
from common.global_var import GlobalVar
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def auto_run(cfg_file, args):
    # 启动运行
    print("config file: ",  cfg_file)
    i = 0
    while i < len(args):
        print("arg[" + str(i) + "]: " + str(args[i]))
        i += 1
    GlobalVar.add("config", cfg_file)
    ConfigReader.init(cfg_file)

    theme = ConfigReader.get('info', 'theme')
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
    scriptconfigs = ConfigReader.get_options("scripts")
    print("-------------------------------------")
    for option in scriptconfigs:
        item = ConfigReader.get("scripts", option).split(",")
        print(option + ": " + item[0])
    print(">>>>请输入需要执行的步骤id：（支持格式：'1,3' 或 '1-3', 直接<enter>则默认全部执行）")
    inputs = []
    input_str: str
    if ConfigReader.get("config", "inputsrc") == "wechat":
        input_str = ""
    else:
        input_str = input()
    if input_str.strip("") == "":
        inputs = scriptconfigs
    elif input_str.find("-") > 0:
        temps = input_str.split("-")
        start = int(temps[0].strip(" "))
        end = int(temps[1].strip(" "))
        if start > end:
            print("输入错误")
            exit(-1)
        while start <= end:
            inputs.append(str(start))
            start += 1
    else:
        temps = input_str.replace(" ", "").split(",")
        for i in temps:
            inputs.append(i)

    for option in scriptconfigs:
        item = ConfigReader.get("scripts", option).split(",")
        script_name = item[0]
        script_path = item[1]
        if option in inputs:
            print("开始运行 " + option + ": " + script_name)
            ret = os.system("python " + script_path)
            if ret == 0:
                print("完成" + script_name)
            else:
                print("执行" + script_name + "失败，返回：" + str(ret))
                break
        else:
            print("跳过 " + option + ": " + script_name)

