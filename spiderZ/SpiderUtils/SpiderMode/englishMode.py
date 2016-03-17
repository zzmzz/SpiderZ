from abstractMode import AbstractMode
from Utils.logFactory import LogFactory
from SpiderUtils.getWords import GetWords
import re

logger = LogFactory.getlogger("EnglishMode")


class EnglishMode(AbstractMode):
    def __init__(self):
        super(EnglishMode, self).__init__()

    def catch_words(self, html):
        words = GetWords.get_english(html)
        return words

    def analyze(self, word):
        m = re.search("\d+", word)
        n = re.search("\W+", word)
        if not m and not n and len(word) > 4:
            return [word]
        else:
            return []
