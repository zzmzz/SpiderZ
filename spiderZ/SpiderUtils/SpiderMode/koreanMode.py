from abstractMode import AbstractMode
from Utils.logFactory import LogFactory
from SpiderUtils.getWords import GetWords
from WordSplit.splitAdapter import SplitAdapter

logger = LogFactory.getlogger("KoreanMode")


class KoreanMode(AbstractMode):
    def __init__(self):
        super(KoreanMode, self).__init__()

    def catch_words(self, html):
        words = GetWords.get_korean(html)
        return words

    def analyze(self, word):
        return [word]
