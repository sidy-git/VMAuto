# -*- coding: utf-8 -*-
from crawler_template import CrawlerBase


class DigitalZol(CrawlerBase):
    def __init__(self, src, url):
        super().__init__()
        self.set_attr(src, url)

    def run(self):
        self.get_list()
        if self.soup is not None:
            news = self.soup.find("div", id="list-v-1")
            items = news.select("ul")
            for ul in items:
                for li in ul:
                    if str(li).find("class=\"news-moudle_item\"") > 0:
                        super().addItem(self.src, li.find("a").attrs["title"], "https:" + li.find("a").attrs["href"])
        else:
            print('Failed to retrieve the webpage from: ', super().url)


# instance = DigitalZol("中关村", "https://news.zol.com.cn/")
# instance.run()
# instance.printList()
