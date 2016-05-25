from abstractMode import AbstractMode
from SpiderUtils.getWords import GetWords

class Regex:
    __pattern = ''

    def __init__(self, pattern):
        self.__pattern = pattern

    def get_pattern(self):
        return self.__pattern


class RegexMode(AbstractMode):
    __pattern = ''

    def __init__(self, regex):
        self.__pattern = regex.get_pattern()

    def catch_words(self, html):
        words = GetWords.get_by_regex(html, self.__pattern)
        return words

    def analyze(self, word):
        return [word]
