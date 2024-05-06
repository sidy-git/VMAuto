# 资讯条目结构类
class StItem:
    id: int
    src = ""
    title = ""
    link = ""

    def set_attr(self, pid, psrc, ptitle, plink):
        self.id = pid
        self.title = ptitle
        self.src = psrc
        self.link = plink

    def __getstate__(self):
        # 排除不可序列化的字段
        return {'data': self.id}

    def __setstate__(self, state):
        # 恢复对象状态
        self.__dict__.update(state)
