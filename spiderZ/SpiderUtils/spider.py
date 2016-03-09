# !/usr/bin/python
# coding=utf-8
from urlparse import *

from SpiderUtils.getWords import GetWords
from Utils.logFactory import LogFactory
from enums import Language
from getUrls import UrlScan
from spiderStrategy import SpiderStrategy


class Spider:
    __isout = False
    __url = ""
    __depth = 1
    __pattern = None
    __language = Language.All
    logger = LogFactory.getlogger("Spider")

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
        html = GetWords.getWords(self.__url, self.__language)
        if (self.__depth > 1):
            urllist = UrlScan.scanpage(html, self.__url, self.__isout, self.__pattern)
            for link in urllist:
                try:
                    lock.acquire()
                    self.logger.info("new strategy created:" + link)
                    queue.put(SpiderStrategy(link, self.__depth - 1, self.__isout, self.__pattern, self.__language))
                except Exception, e:
                    self.logger.error(e)
                finally:
                    lock.release()
        return
