# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

url = "https://www.ithome.com/"
# url = "https://www.baidu.com/"
response = requests.get(url)

if response.status_code == 200:
    # 使用 'html.parser' 解析器解析 HTML 内容
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, 'html.parser')

    # 创建一个PrettyTable对象
    table = PrettyTable()
    # 设置列名
    table.field_names = ["标题", "链接"]

    # 提取标题
    title = soup.title.text
    news = soup.find("div", id="nnews")
    items = news.select("ul")
    for ul in items:
        for li in ul:
            if (str(li).find("class=\"ad\"") < 0):
                # 添加行
                table.add_row([li.text, li.find("a").attrs["href"]])
    # 打印表格
    print(table)

else:
    print('Failed to retrieve the webpage')

