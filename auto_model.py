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
    config.read(cfg_file)

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

    # 运行选材推荐脚本
    print("开始收集选材......")
    if config.has_option('scripts', "crawler"):
        script = config.get('scripts', "crawler")
        os.system("python3 " + script)
    else:
        print("收集选材脚本未找到")

    print("完成选材收集")

    # 开始文案生成和优化
    print("开始文案优化......")
    if config.has_option('scripts', "aigc"):
        script = config.get('scripts', "aigc")
        os.system("python3 " + script)
    else:
        print("文案优化脚本未找到")
    print("完成文案优化")

    # 准备图片素材
    print("开始准备图片素材")
    if config.has_option('scripts', "picCollect"):
        script = config.get('scripts', "picCollect")
        os.system("python3 " + script)
    else:
        print("图片素材准备脚本未找到")

    # 开始生成视频
    print("开始文图成片......")
    if config.has_option('scripts', "jianying"):
        script = config.get('scripts', "jianying")
        os.system("python3 " + script)
    else:
        print("生成视频脚本未找到")
    print("完成视频生成")

    # 开始封面制作
    print("开始封面制作......")
    if config.has_option('scripts', "fengmian"):
        script = config.get('scripts', "fengmian")
        os.system("python3 " + script)
    else:
        print("生成封面脚本未找到")
    print("完成封面生成")




