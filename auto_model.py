# -*- coding: utf-8 -*-
# 自动运行模式
import configparser
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def auto_run(cfg_file):
    # 启动运行
    print("config file: ",  cfg_file)
    config = configparser.ConfigParser()
    config.read(cfg_file)

    theme = config.get('info', 'theme')
    print("主题: ", theme)
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

    # 开始生成视频
    print("开始文图成片......")
    if config.has_option('scripts', "jianying"):
        script = config.get('scripts', "jianying")
        os.system("python3 " + script)
    else:
        print("生成视频脚本未找到")
    print("完成视频生成")