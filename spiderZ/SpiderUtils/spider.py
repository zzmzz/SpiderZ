# !/usr/bin/python
# coding=utf-8
from SpiderUtils.getWords import GetWords
from getUrls import UrlScan
from urlparse import *
from spiderStrategy import SpiderStrategy
from enums import Language


class Spider:
    __isout = False
    __url = ""
    __depth = 1
    __pattern = None
    __language = Language.All

    def __init__(self, strategy=SpiderStrategy()):
        self.__isout = strategy.is_out
        self.__url = strategy.url
        self.__depth = strategy.depth
        self.__language = strategy.language
        pattern = strategy.pattern
        if (pattern == None):
            if (strategy.is_out == False):
                r = urlparse(strategy.url)
                self.__pattern = 'http(\w|\W)*' + r.netloc
            else:
                self.__pattern = None
        else:
            self.__pattern = pattern

    def get_all_words(self, queue, lock):
        html = GetWords.getWords(self.__url, Language.All)
        if (self.__depth > 1):
            urllist = UrlScan.scanpage(html, self.__url, self.__isout, self.__pattern)
            for link in urllist:
                lock.acquire()
                queue.put(SpiderStrategy(link, self.__depth - 1, self.__isout, self.__pattern, self.__language))
                lock.release()