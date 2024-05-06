# 资讯条目结构类
class StItem:
    static_index = 0
    id = 0
    src = ""
    title = ""
    link = ""

    def set_attr(self, psrc, ptitle, plink):
        self.id = StItem.static_index
        self.title = ptitle
        self.src = psrc
        self.link = plink
        StItem.static_index += 1

    def __getstate__(self):
        # 排除不可序列化的字段
        return {'data': self.id}

    def __setstate__(self, state):
        # 恢复对象状态
        self.__dict__.update(state)
