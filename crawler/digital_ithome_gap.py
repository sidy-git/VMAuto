# -*- coding: utf-8 -*-
import os
import urllib.request
from common.global_var import GlobalVar
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

    def get_detail_dl_img(self, detail_url, index):
        imgdir = GlobalVar.get("imgsavedir")
        if imgdir is None:
            print("get imgdir failed")
        super().get_detail(detail_url)
        if self.soup is not None:
            # 获取文本
            detail = self.soup.find("div", id="paragraph")
            context = ""
            lines = detail.select("p")
            for line in lines:
                if line.text.find("广告声明") >= 0 or len(line.text) < 1:
                    continue
                else:
                    context += line.text + "\r\n"
            # 下载图片
            imgs = detail.select("p")
            imgIndex = 1
            for img in imgs:
                if img.find("img"):
                    # print(img)
                    pic_src = img.find("img").attrs["data-original"]
                    if pic_src.find("?"):
                        pic_src = pic_src.split("?")[0]
                    # 使用splitext分割文件名和扩展名
                    file_extension = os.path.splitext(pic_src)[1]
                    # print(pic_src)
                    save_path = imgdir + "/" + str(index) + "-" + str(imgIndex) + file_extension
                    print("开始下载图片" + str(index) + "-" + str(imgIndex))
                    urllib.request.urlretrieve(pic_src, save_path)
                    imgIndex += 1
            return context
        else:
            print('Failed to retrieve the webpage from: ', detail_url)
            return None


# instance = DigitalIthomeGap("IT之家", "https://www.ithome.com/")
# instance.run()
# instance.printList()
# context = instance.get_detail_dl_img("https://www.ithome.com/0/766/372.htm", 1)
# print(context)
