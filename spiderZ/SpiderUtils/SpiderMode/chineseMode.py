from abstractMode import AbstractMode
from Utils.logFactory import LogFactory
from SpiderUtils.getWords import GetWords
from WordSplit.splitAdapter import SplitAdapter

logger = LogFactory.getlogger("ChineseMode")


class ChineseMode(AbstractMode):
    def __init__(self):
        super(ChineseMode, self).__init__()

    def catch_words(self, html):
        words = GetWords.get_chinese(html)
        return words

    def analyze(self, word):
        ws = SplitAdapter.split(word)
        return ws
