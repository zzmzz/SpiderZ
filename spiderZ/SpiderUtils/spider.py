# !/usr/bin/python
# coding=utf-8
from SpiderUtils.getWords import GetWords
from getUrls import UrlScan
from urlparse import *
import threadpool
from spiderStrategy import SpiderStrategy
from enums import Language

pool = threadpool.ThreadPool(10)


def Son_Spider(strategy):
    s = Spider(strategy)  # 递归调用
    s.get_all_words()


class Spider():
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

    def get_all_words(self):
        html = GetWords.getWords(self.__url, Language.All)
        if (self.__depth > 1):
            list = UrlScan.scanpage(html, self.__url, self.__isout, self.__pattern)
            arglist = []
            for link in list:
                arg = ([SpiderStrategy(link, self.__depth - 1, self.__isout, self.__pattern, self.__language)], {})
                arglist.append(arg)
            requests = threadpool.makeRequests(Son_Spider, arglist)
            [pool.putRequest(req) for req in requests]
            pool.wait()
