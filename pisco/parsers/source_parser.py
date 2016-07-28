import javalang
import logging
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class SourceParser():
    def __init__(self, splitter=u"<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>\r"):
        self.splitter = splitter

    def parse(self, x, only_parsable=False):
        codes = []
        segments = x.split(self.splitter)
        if only_parsable:
            for segment in segments:
                try:
                    javalang.parse.parse(segment)
                    codes.append(segment)
                except Exception as e:
                    logging.warn('Parsing java code failed: '.format(e))
            return codes
        else:
            return segments
