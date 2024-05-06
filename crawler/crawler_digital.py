from crawler_template import CrawlerBase
from digital_ithome import DigitalIthome
from digital_zol import DigitalZol
from common.global_var import GlobalVar
from output_manager import XmlOutput

scripts = [DigitalIthome("IT之家", "https://www.ithome.com/"),
           DigitalZol("中关村", "https://news.zol.com.cn/")]


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


def get_detail():
    # 选择选材
    print("请输入选材序号: ")
    input_index = input()
    print("选择素材序号: ", input_index)
    index = int(input_index)
    context = None
    if 0 < index <= len(CrawlerBase.itemList):
        for script in scripts:
            if script.src == CrawlerBase.itemList[index].src:
                context = script.get_detail(CrawlerBase.itemList[index-1].link)
                break
        if context is None:
            print("find context failed")
            GlobalVar.add("context", "")
        else:
            GlobalVar.add("context", context)
    else:
        print("序号错误，请重新输入")
        get_detail()


# 执行脚本
collect_list()
get_detail()
