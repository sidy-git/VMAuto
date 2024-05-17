# -*- coding: utf-8 -*-
import os
import sys

import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common.item_struct import StItem


# 爬虫框架基类
class CrawlerBase:
    static_index = 1
    src = ""
    url = ""
    soup: BeautifulSoup
    itemList = []

    def set_attr(self, psrc, purl):
        self.src = psrc
        self.url = purl

    def get_list(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            # 使用 'html.parser' 解析器解析 HTML 内容
            response.encoding = response.apparent_encoding
            self.soup = BeautifulSoup(response.text, 'html.parser')
            # html列表解析由子类实现
        else:
            print('Failed to retrieve the webpage')
            self.soup = None

    def addItem(self, psrc, ptitle, plink):
        item = StItem()
        item.set_attr(CrawlerBase.static_index, psrc, ptitle, plink)
        self.itemList.append(item)
        CrawlerBase.static_index += 1

    def printList(self):
        # 创建一个PrettyTable对象
        table = PrettyTable()
        # 设置列名
        table.field_names = ["序号", "来源", "标题", "链接"]
        item: StItem
        for item in self.itemList:
            # 添加行
            table.add_row([str(item.id), item.src, item.title, item.link])
        # 打印表格
        print(table)

    def get_text(self):
        ret = ""
        for item in self.itemList:
            lint = str(item.id) + " " + item.title + " " + item.link + "\r\n"
            ret = ret + lint
        return ret

    def get_detail(self, detail_url):
        print("获取信息详情, url:", detail_url)
        response = requests.get(detail_url)
        if response.status_code == 200:
            # 使用 'html.parser' 解析器解析 HTML 内容
            response.encoding = response.apparent_encoding
            self.soup = BeautifulSoup(response.text, 'html.parser')
            # 详情文案解析由子类实现
        else:
            print('Failed to retrieve the webpage')
            self.soup = None

    def get_detail_dl_img(self, detail_url, index):
        print("获取信息详情, url:", detail_url)
        response = requests.get(detail_url)
        if response.status_code == 200:
            # 使用 'html.parser' 解析器解析 HTML 内容
            response.encoding = response.apparent_encoding
            self.soup = BeautifulSoup(response.text, 'html.parser')
            # 详情文案解析由子类实现
        else:
            print('Failed to retrieve the webpage')
            self.soup = None
