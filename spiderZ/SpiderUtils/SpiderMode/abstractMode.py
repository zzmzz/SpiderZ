#!/usr/bin/python
# coding=utf-8
from abc import ABCMeta, abstractmethod
import sys
from SpiderUtils.getWords import GetWords
from Utils.logFactory import LogFactory
from PyIO.pyMongoUtil import PyMongoUtil

reload(sys)
sys.setdefaultencoding('utf-8')

logger = LogFactory.getlogger("Mode")


class AbstractMode:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def get_words(self, url):
        html = GetWords.get_content(url)
        try:
            words = self.catch_words(html)
            wlist = []
            for wd in words:
                wlist.extend(self.analyze(wd))
            PyMongoUtil.write(url, wlist)
        except Exception, e:
            logger.error(url + " " + str(e))
        return html

    @abstractmethod
    def catch_words(self, html):
        pass

    @abstractmethod
    def analyze(self, word):
        pass
