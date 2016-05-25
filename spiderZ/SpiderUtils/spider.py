# !/usr/bin/python
# coding=utf-8
from urlparse import *

from SpiderUtils.getWords import GetWords
from Utils.logFactory import LogFactory
from enums import Language
from getUrls import UrlScan
from spiderStrategy import SpiderStrategy
from SpiderUtils.modeFactory import ModeFactory

logger = LogFactory.getlogger("Spider")


class Spider:
    __isout = False
    __url = ""
    __depth = 1
    __url_pattern = None
    __mode = None

    def __init__(self, strategy=SpiderStrategy()):
        self.__isout = strategy.is_out
        self.__url = strategy.url
        self.__depth = strategy.depth
        self.__mode = strategy.mode
        pattern = strategy.pattern
        if pattern is None:
            if strategy.is_out is False:
                r = urlparse(strategy.url)
                self.__url_pattern = r.netloc
            else:
                self.__url_pattern = None
        else:
            self.__url_pattern = pattern

    def get_all_words(self, queue, lock):
        try:
            mode = ModeFactory.get_mode(self.__mode)
            html = mode.get_words(self.__url)
            if self.__depth > 1:
                urllist = UrlScan.scanpage(html, self.__url, self.__url_pattern)
                for link in urllist:
                    try:
                        lock.acquire()
                        logger.info("new strategy created:" + link)
                        queue.put(SpiderStrategy(link, self.__depth - 1, self.__isout, self.__url_pattern, self.__mode))
                    except Exception, e:
                        logger.error(str(e))
                    finally:
                        lock.release()
        except Exception, e:
            logger.error(str(e))
        return
