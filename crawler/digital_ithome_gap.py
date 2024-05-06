# -*- coding: utf-8 -*-
from crawler_template import CrawlerBase


class DigitalIthomeGap(CrawlerBase):
    def __init__(self, src, url):
        super().__init__()
        self.set_attr(src, url)

    def run(self):
        self.get_list()
        if self.soup is not None:
            news = self.soup.find("div", id="rank")
            items = news.find("ul", id="d-1")
            # 限制数量
            max_line = 10
            for li in items:
                super().addItem(self.src, li.find("a").attrs["title"], li.find("a").attrs["href"])
                max_line -= 1
                if max_line <= 0:
                    break
        else:
            print('Failed to retrieve the webpage from: ', super().url)

    def get_detail(self, detail_url):
        super().get_detail(detail_url)
        if self.soup is not None:
            detail = self.soup.find("div", id="paragraph")
            context = ""
            lines = detail.select("p")
            for line in lines:
                if line.text.find("广告声明") >= 0 or len(line.text) < 1:
                    continue
                else:
                    context += line.text + "\r\n"
            return context
        else:
            print('Failed to retrieve the webpage from: ', detail_url)
            return None


# instance = DigitalIthome("IT之家", "https://www.ithome.com/")
# instance.run()
# instance.printList()
# context = instance.get_detail("https://www.ithome.com/0/762/511.htm")
# print(context)
