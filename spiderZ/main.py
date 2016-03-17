from Consts.cacheKeyConstants import const
from ProcessPool.pool import PyPool
from PyIO.writeWords import Write
from PyMemcached.memcacheUtil import MemcacheUtil
from QueueListener.listener import MyListener
from SpiderUtils.bloomFilter import SpiderBloomFilter
from SpiderUtils.enums import Language
from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from Statics.wordCount import WordCount
from Utils.logFactory import LogFactory

logger = LogFactory.getlogger("main")
Write.clean()
MemcacheUtil.clean()
SpiderBloomFilter()
queue = PyPool.get_queue()
lock = PyPool.get_lock()
listener = MyListener()
s = SpiderStrategy("http://www.163.com/", 4, True, None, Language.All)
Spider(s).get_all_words(queue, lock)
listener.listen(lock, queue)
WordCount.calc_count()
