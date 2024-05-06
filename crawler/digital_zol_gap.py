# -*- coding: utf-8 -*-
from crawler_template import CrawlerBase


class DigitalZolGap(CrawlerBase):
    def __init__(self, src, url):
        super().__init__()
        self.set_attr(src, url)

    def run(self):
        self.get_list()
        if self.soup is not None:
            news = self.soup.find("div", id="list-v-1")
            items = news.select("ul")
            # 限制数量
            max_line = 10
            for ul in items:
                for li in ul:
                    if str(li).find("class=\"news-moudle_item\"") > 0:
                        super().addItem(self.src, li.find("a").attrs["title"], "https:" + li.find("a").attrs["href"])
                        max_line -= 1
                    if max_line <= 0:
                        break
                if max_line <= 0:
                    break
        else:
            print('Failed to retrieve the webpage from: ', super().url)


# instance = DigitalZol("中关村", "https://news.zol.com.cn/")
# instance.run()
# instance.printList()
