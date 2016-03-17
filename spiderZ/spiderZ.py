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
logger = LogFactory.getlogger("main")
PyMongoUtil.clean()
MemcacheUtil.clean()
SpiderBloomFilter()
queue = PyPool.get_queue()
lock = PyPool.get_lock()
listener = MyListener()
r = Regex("(?i)([a-z0-9\-\._]+@[a-z0-9\-\.]+\.[a-z]{2,4}[:,\|]*.*)")
s = SpiderStrategy("http://www.leakedin.com/tag/emailpassword-dump/", 2, False, None, r)
Spider(s).get_all_words(queue, lock)
listener.listen(lock, queue)
WordCount.calc_count()
