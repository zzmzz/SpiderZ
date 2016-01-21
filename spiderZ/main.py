from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from SpiderUtils.enums import Language
from Statics.wordCount import WordCount
from ProcessPool.pool import PyPool
from QueueListener.listener import MyListener
from PyMemcached.memcacheUtil import MemcacheUtil
from SpiderUtils.bloomFilter import Bloom_Filter
from Consts.cacheKeyConstants import const
from PyIO.writeWords import Write
Write.clean()
MemcacheUtil.clean()
MemcacheUtil.add(const.URLPOOLKEY, Bloom_Filter(10000))
queue = PyPool.get_queue()
lock = PyPool.get_lock()
listener = MyListener()
s = SpiderStrategy("http://www.360doc.com/", 5, True, None, Language.All)
Spider(s).get_all_words(queue, lock)
listener.listen(lock, queue)
WordCount.calc_count()
