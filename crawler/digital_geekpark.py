# -*- coding: utf-8 -*-
from pyauto.gui_opt import GuiOpt
from crawler_template import CrawlerBase


class DigitalGeekpark(CrawlerBase):
    def __init__(self, src, url):
        super().__init__()
        self.set_attr(src, url)

    def run(self):
        self.get_list()
        if self.soup is not None:
            news = self.soup.find("div", {"class": "article-list"})
            # print(news)
            items = news.select("article")
            # 限制数量
            max_line = 10
            for li in items:
                # print(li)
                if str(li).find("class=\"article-item\"") > 0:
                    temp = li.find("a", {"data-event-category": "article-list.title"})
                    # print(temp)
                    super().addItem(self.src, temp.text, self.url + temp.attrs["href"])
                    max_line -= 1
                if max_line <= 0:
                    break
        else:
            print('Failed to retrieve the webpage from: ', super().url)

    # def get_detail_dl_img(self, detail_url, index):
    #     imgdir = GlobalVar.get("imgSaveDir")
    #     if imgdir is None:
    #         print("get imgdir failed")
    #     super().get_detail(detail_url)
    #     if self.soup is not None:
    #         # print(self.soup)
    #         # 获取文本
    #         detail = self.soup.find("div", {"class", "article-content"})
    #         # print(detail)
    #         context = ""
    #         lines = detail.select("p")
    #         for line in lines:
    #             if line.text.find("广告声明") >= 0 or len(line.text) < 1:
    #                 continue
    #             else:
    #                 context += line.text.strip("\n")
    #                 # print(context)
    #         # 下载图片
    #         imgs = detail.select("p")
    #         imgIndex = 1
    #         for img in imgs:
    #             if img.find("img"):
    #                 pic_src = img.find("img").attrs["data-lazyload"]
    #                 if pic_src.find("?"):
    #                     pic_src = pic_src.split("?")[0]
    #                 if pic_src.find("https") < 0:
    #                     pic_src = "https:" + pic_src
    #                 # 使用splitext分割文件名和扩展名
    #                 file_extension = os.path.splitext(pic_src)[1]
    #                 # print(pic_src)
    #                 save_path = imgdir + "/" + str(index) + "-" + str(imgIndex) + file_extension
    #                 print("开始下载图片" + str(index) + "-" + str(imgIndex))
    #                 urllib.request.urlretrieve(pic_src, save_path)
    #                 imgIndex += 1
    #         # print(context)
    #         return context
    #     else:
    #         print('Failed to retrieve the webpage from: ', detail_url)
    #         return None
1
# instance = DigitalGeekparkGap("极客公园", "https://www.geekpark.net")
# instance.run()
# instance.printList()
