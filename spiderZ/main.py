from Consts.cacheKeyConstants import const
from ProcessPool.pool import PyPool
from PyIO.writeWords import Write
from PyMemcached.memcacheUtil import MemcacheUtil
from QueueListener.listener import MyListener
from SpiderUtils.bloomFilter import Bloom_Filter
from SpiderUtils.enums import Language
from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from Statics.wordCount import WordCount
from Utils.logFactory import LogFactory

logger = LogFactory.getlogger("main")
Write.clean()
MemcacheUtil.clean()
MemcacheUtil.delete("URLWRITEKEY")
MemcacheUtil.add(const.URLPOOLKEY, Bloom_Filter(10000))
queue = PyPool.get_queue()
lock = PyPool.get_lock()
listener = MyListener()
s = SpiderStrategy("http://www.baidu.com/", 2, True, None, Language.All)
Spider(s).get_all_words(queue, lock)
listener.listen(lock, queue)
WordCount.calc_count()
