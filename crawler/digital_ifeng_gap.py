# -*- coding: utf-8 -*-
import os
import urllib.request

from common.global_var import GlobalVar
from crawler_template import CrawlerBase


class DigitaliFengGap(CrawlerBase):
    def __init__(self, src, url):
        super().__init__()
        self.set_attr(src, url)

    def run(self):
        self.get_list()
        if self.soup is not None:
            news = self.soup.find("div", {"class": "style_news_ibc02"})
            # print(news)
            items = news.select("a")
            # 限制数量
            max_line = 10
            for li in items:
                # print(li)
                if str(li).find("class=\"index_title_oqpqT\"") > 0:
                    super().addItem(self.src, li.attrs["title"], li.attrs["href"])
                    max_line -= 1
                if max_line <= 0:
                    break
        else:
            print('Failed to retrieve the webpage from: ', super().url)

    def get_detail_dl_img(self, detail_url, index):
        imgdir = GlobalVar.get("imgSaveDir")
        if imgdir is None:
            print("get imgdir failed")
        super().get_detail(detail_url)
        if self.soup is not None:
            # print(self.soup)
            # 获取文本
            detail = self.soup.find("div", {"class", "index_text_D0U1y"})
            # print(detail)
            context = ""
            lines = detail.select("p")
            for line in lines:
                if line.text.find("广告声明") >= 0 or len(line.text) < 1:
                    continue
                else:
                    context += line.text.strip("\n")
                    # print(context)
            # 下载图片
            imgs = detail.select("p")
            imgIndex = 1
            for img in imgs:
                if img.find("img"):
                    pic_src = img.find("img").attrs["src"]
                    if pic_src.find("?"):
                        pic_src = pic_src.split("?")[0]
                    if pic_src.find("https") < 0:
                        pic_src = "https:" + pic_src
                    # 使用splitext分割文件名和扩展名
                    file_extension = os.path.splitext(pic_src)[1]
                    # print(pic_src)
                    save_path = imgdir + "/" + str(index) + "-" + str(imgIndex) + file_extension
                    print("开始下载图片" + str(index) + "-" + str(imgIndex) + " 图片地址: " + pic_src)
                    try:
                        urllib.request.urlretrieve(pic_src, save_path)
                    except:
                        print("图片下载失败")
                    imgIndex += 1
            # print(context)
            return context
        else:
            print('Failed to retrieve the webpage from: ', detail_url)
            return None


# instance = DigitaliFengGap("凤凰网", "https://tech.ifeng.com/")
# instance.run()
# instance.printList()
# instance.get_detail_dl_img("https://tech.ifeng.com/c/8ZuGwlS3nTx", 1)
