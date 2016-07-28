import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SourceParser():
    def __init__(self, splitter=u"<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>\r"):
        self.splitter = splitter

    def parse(self, x):
        return x.split(self.splitter)
