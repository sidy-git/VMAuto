# -*- coding: utf-8 -*-
import json
import os
import sys
import time

import pyperclip
import requests
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.global_var import GlobalVar


class OptConfig:
    key = ""
    url = ""
    model = ""
    prompts = ""

    def __init__(self, pkey, purl, pmodel, pprompts):
        self.key = pkey
        self.url = purl
        self.model = pmodel
        self.prompts = pprompts

    def print(self):
        print("key:" + self.key)


chnIndex = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "十二"]

opts = [
    # OptConfig("口语化", "https://ppwx-helpseller-gm2.jd.com/text/nlp", "Chatrhino", "请将以下内容用较为口语化的风格进行重写："),
    OptConfig("新闻稿", "https://ppwx-helpseller-gm2.jd.com/text/nlp", "Chatrhino", "请将以下内容用新闻稿的风格进行重写："),
    OptConfig("新闻稿缩写", "https://ppwx-helpseller-gm2.jd.com/text/nlp", "Chatrhino", "请以新闻稿的风格提取以下内容的核心信息，并控制在300个字以内：")
]


def post_json(url, body):
    response = requests.post(url, data=body, headers={'Content-Type': 'application/json'})
    print("url: " + url + " body: " + json.dumps(body))
    if response.status_code == 200:
        # 使用 'html.parser' 解析器解析 HTML 内容
        response.encoding = response.apparent_encoding
        print("post_json() return: " + response.text)
        return response.text
    else:
        print("post_json() return: " + str(response.status_code))
        return None


def run():
    i = 1
    total_txt = ""
    option = "context" + str(i)
    GlobalVar.clear_all("opt_context")
    mode = int(GlobalVar.get("mode"))
    while GlobalVar.get(option) is not None:
        context = GlobalVar.get(option)
        print("context:" + context)
        # 根据mode选用不同prompts
        opt = opts[mode-1]
        print("开始文本优化:" + opt.key)
        temp_context = opt.prompts + context
        json_data = json.dumps({"model": opt.model, "userSend": temp_context})
        context = post_json(opt.url, json_data)
        if context is None:
            print("文本优化失败")
        else:
            GlobalVar.add("opt_context" + str(i), context)
            total_txt += chnIndex[i] + "、 " + context
            print("优化后文本：" + context)
        i += 1
        option = "context" + str(i)

    # 增加头部和尾部文案
    headtxt = time.strftime("%Y年%m月%d日", time.localtime()) + "科技资讯\r\n"
    # tailtxt = "了解更多科技资讯，欢迎关注，一键三连"
    # total_txt = headtxt + total_txt + tailtxt
    total_txt = headtxt + total_txt
    print("优化后文本：" + total_txt)
    pyperclip.copy(total_txt)
    GlobalVar.add("final_context", total_txt)
    print("-----------------------------------------------------------------")
    print("以上内容已复制到剪贴板，可直接粘贴")


run()
# opt = opts[0]
# context = "2024款苹果iPadPro发布：采用OLED屏幕，搭载全新M4芯片，8999元起。5月7日消息，苹果今晚发布了全新iPadPro，采用了全新的OLED屏幕，搭载M4芯片，8999元起。11英寸的厚度为5.3mm，13英寸的厚度为5.1mm，甚至比iPodnano还要薄，这使其成为100%再生铝金属打造。全新iPadPro采用OLED显示屏，由于“单个OLED面板无法为XDR产生足够的亮度”，因此苹果开发了“双层串联OLED”，使用两个OLED显示屏来获得1000尼特的全局亮度和1600尼特的峰值亮度。XDR精度现已达到“全新水平”，苹果称之为“超精视具有四个性能核心和六个高能效核心，采用新一代机器学习（ML）加速器，与前代iPadPro搭载的M2芯片相比，中央处理器性能提升最快可达1.5倍。新CPU具有10核GPU，并首次为iPad带来了动态缓存、硬件加速网格着色和光线追踪功能，与M2相比，整体渲染性来高分辨率流媒体服务视频播放体验。搭载M4芯片的全新iPadPro采用苹果迄今最强大的神经网络引擎，每秒可执行高达38万亿次运算，比A11仿生芯片采用的首款Apple神经网络引擎相比最快可达60倍。此外，iPadOS还推出CoreML等先进框架，供开发者进一步强大的生产力和创意app，发挥AI技术的威力。此外，新的工业设计使新iPadPro 的散热性能提高了20%，与上一代iPadPro相比，整体性能提升了4倍。苹果称，新iPadPro 比初代iPadPro快10倍。苹果还推出了新的FinalCutPro和LogicPro，在新M4上，FCP渲染ro搭载12mp后置摄像头，现支持ProRes视频录制和SmartHDR4。还拥有四个录音室麦克风、激光雷达扫描仪。全新iPadPro现在还配备全新自适应原彩闪光灯，进一步提升文稿扫描效果。采用AI，新iPadPro可通过相机App自动识别文档，如果画面中有阴影，会即最高可达40Gb/s的高速有线连接。苹果还推出了新妙控键盘，基本设计理念相同，但更薄，新增了一个功能行，采用铝制掌托，触控板具有触觉反馈，苹果称“整个体验就像使用MacBook一样。”苹果还推出了ApplePencilPro，现在用户可以挤压ApplePencilPro起，13英寸版为11499元起，妙控键盘11英寸款售价2399元，13英寸款售价2799元。新手写笔售价999元。5月9日上午9点接受订购，5月15日发售。苹果“放飞吧”特别活动专题"
# temp_context = opt.prompts + context
# json_data = json.dumps({"model": opt.model, "userSend": temp_context})
# context = post_json(opt.url, json_data)
# print("优化后：")
# print(context)
