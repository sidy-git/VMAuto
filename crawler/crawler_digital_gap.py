import os
import time

import pyperclip
from crawler_template import CrawlerBase
from digital_geekpark_gap import DigitalGeekparkGap
from digital_ifeng_gap import DigitaliFengGap
from digital_huanqiu_gap import DigitalHuanqiuGap
from digital_mydrivers_gap import DigitalMydriversGap
from digital_zol_gap import DigitalZolGap
from digital_ithome_gap import DigitalIthomeGap
from crawler_template import CrawlerBase
from common.global_var import GlobalVar
from output_manager import XmlOutput


scripts = [
    DigitalIthomeGap("IT之家", "https://www.ithome.com/"),
    DigitalZolGap("中关村", "https://news.zol.com.cn/"),
    DigitalMydriversGap("快科技", "https://news.mydrivers.com/"),
    DigitalHuanqiuGap("环球网", "https://tech.huanqiu.com/"),
    DigitaliFengGap("凤凰网", "https://tech.ifeng.com/"),
    DigitalGeekparkGap("极客公园", "https://www.geekpark.net")
]


def collect_list():
    index = 1
    XmlOutput.init_file("test.xml")
    for script in scripts:
        print("开始执行脚本 " + str(index) + "/" + str(len(scripts)))
        script.run()
        index += 1

    XmlOutput.write_to_xml(CrawlerBase.itemList)
    CrawlerBase().printList()
    XmlOutput.save_to_file()

def make_img_save_dir():
    imgfile = GlobalVar.get("imgDir")
    if imgfile is None:
        print("get img file from global var failed")
        exit(-1)
    filename = time.strftime("VMAuto%Y%m%d", time.localtime())
    imgdir = imgfile + "/" + str(filename)
    # 判断是否存在重名文件夹，是则增加后缀
    if os.path.exists(imgdir):
        tmp_i = 1
        tmp_dir = imgdir + "(" + str(tmp_i) + ")"
        while os.path.exists(tmp_dir):
            tmp_i += 1
            tmp_dir = imgdir + "(" + str(tmp_i) + ")"
        imgdir = tmp_dir
    os.mkdir(imgdir)
    print(f"Folder '{imgdir}' created successfully.")
    GlobalVar.add("imgSaveDir", imgdir)
    print("图片保存路径：" + imgdir)

def get_detail_download_img():
    # 选择选材
    print("请输入选材序号（序号中间用空格分隔）: ")
    input_index = input()
    print("选择素材序号: ", input_index)
    indexs = str(input_index).split()
    temp_context = None
    context = ""
    make_img_save_dir()

    iindex = 0
    GlobalVar.clear_all("context")
    for i in indexs:
        index = int(i)
        if 0 < index <= len(CrawlerBase.itemList):
            for script in scripts:
                if script.src == CrawlerBase.itemList[index-1].src:
                    iindex += 1
                    temp_context = script.get_detail_dl_img(CrawlerBase.itemList[index-1].link, iindex)
                    # 删除网站标题
                    temp_context = temp_context.replace(CrawlerBase.itemList[index-1].src, "")
                    GlobalVar.add_more("context", CrawlerBase.itemList[index-1].title + "。" + temp_context)
                    break
            if temp_context is None:
                print("find context failed")
                GlobalVar.clear_all("context")
        else:
            print("序号[" + i + "]错误，请重新输入")
            get_detail_download_img()


# 执行脚本
collect_list()
get_detail_download_img()
