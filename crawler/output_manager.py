import xml.etree.ElementTree as ET
from common.item_struct import StItem


class XmlOutput:
    static_index = 1
    filename = ""
    root: ET.Element

    def __init__(self):
        print("XmlOutput.init()")

    @staticmethod
    def init_file(pfilename):
        XmlOutput.filename = pfilename
        # 创建根元素
        XmlOutput.root = ET.Element("data")

    @staticmethod
    def write_to_xml(items):
        # 添加子元素
        item: StItem
        itemsTemp = ET.SubElement(XmlOutput.root, "items")
        for item in items:
            subitem = ET.SubElement(itemsTemp, "item")
            subitem.set("id", str(item.id))
            itemsrc = ET.SubElement(subitem, "src")
            itemsrc.text = item.src
            itemtitle = ET.SubElement(subitem, "title")
            itemtitle.text = item.title
            itemlink = ET.SubElement(subitem, "link")
            itemlink.text = item.link
            XmlOutput.static_index += 1

    @staticmethod
    def save_to_file():
        # 写入XML文件
        tree = ET.ElementTree(XmlOutput.root)
        tree.write("output/" + XmlOutput.filename, encoding="utf-8", xml_declaration=True)


# 测试代码
# XmlOutput.init_file("test.xml")
# item1 = StItem()
# item1.set_attr("IT之家", "title1", "link1")
# item2 = StItem()
# item2.set_attr("IT之家", "title2", "link2")
# items = [item1, item2]
# XmlOutput.write_to_xml(items)
# XmlOutput.save_to_file()
