# -*- coding: utf-8 -*-
from crawler_template import CrawlerBase


class DigitalMydriversGap(CrawlerBase):
    def __init__(self, src, url):
        super().__init__()
        self.set_attr(src, url)

    def run(self):
        self.get_list()
        if self.soup is not None:
            news = self.soup.find("ul", id="pchdpitem")
            items = news.select("li")
            # 限制数量
            max_line = 10
            for li in items:
                temp = li.find("div", {"class": "text"})
                super().addItem(self.src, temp.find("a").text, li.find("a").attrs["href"])
                max_line -= 1
                if max_line <= 0:
                    break
        else:
            print('Failed to retrieve the webpage from: ', super().url)


# instance = DigitalZol("中关村", "https://news.zol.com.cn/")
# instance.run()
# instance.printList()
