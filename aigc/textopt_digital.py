# -*- coding: utf-8 -*-
import json
import os
import sys

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


opts = [OptConfig("口语化", "https://ppwx-helpseller-gm2.jd.com/text/nlp", "Chatrhino", "请将以下内容用较为口语化的风格进行重写：")]


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
    index = 1
    context = GlobalVar.get("context")
    print("context:" + context)
    opt: OptConfig
    for opt in opts:
        print("开始文本优化[" + str(index) + "]:" + opt.key)
        temp_context = opt.prompts + context
        json_data = json.dumps({"model": opt.model, "userSend": temp_context})
        context = post_json(opt.url, json_data)
        if context is None:
            print("优化[" + str(index) + "]执行失败")
        index += 1
    if context is None:
        print("文本优化失败")
    else:
        GlobalVar.add("opt_context", context)
        print("优化后文本：" + context)
        pyperclip.copy(context)
        print("-----------------------------------------------------------------")
        print("以上内容已复制到剪贴板，可直接粘贴")


run()
