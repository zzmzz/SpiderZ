# !/usr/bin/python
# coding=utf-8
from Consts.cacheKeyConstants import const
from ProcessPool.pool import PyPool
from PyIO.pyMongoUtil import PyMongoUtil
from PyMemcached.memcacheUtil import MemcacheUtil
from QueueListener.listener import MyListener
from SpiderUtils.bloomFilter import SpiderBloomFilter
from SpiderUtils.enums import Language
from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from Statics.wordCount import WordCount
from Utils.logFactory import LogFactory
from SpiderUtils.SpiderMode.regexMode import Regex
from SpiderUtils.getUrls import UrlScan
from SpiderUtils.getWords import GetWords
import urllib, htmllib, formatter
logger = LogFactory.getlogger("test")
import re
from bs4 import BeautifulSoup
from PyIO.pyMongoUtil import PyMongoUtil

class Test:
    @staticmethod
    def testGetUrl():
        PyMongoUtil.clean()
        MemcacheUtil.clean()
        SpiderBloomFilter()

        html = GetWords.get_content("http://www.leakedin.com/tag/emailpassword-dump/")
        list = UrlScan.scanpage(html,"http://www.leakedin.com/tag/emailpassword-dump/",None)

        for l in list:
            PyMongoUtil.write(l,[""])
        print len(list)


@staticmethod
def trytry():
    PyMongoUtil.clean()
    MemcacheUtil.clean()
    SpiderBloomFilter()
    queue = PyPool.get_queue()
    lock = PyPool.get_lock()
    listener = MyListener()
    r = Regex("[a-z0-9\-\._]+@[a-z0-9\-\.]+\.[a-z]{2,4}[:,\|]*.*")
    s = SpiderStrategy("http://www.leakedin.com/tag/emailpassword-dump/", 2, is_out=False, pattern=None, mode=r)
    Spider(s).get_all_words(queue, lock)
    listener.listen(lock, queue)
    WordCount.calc_count()
    return


Test.testGetUrl()
