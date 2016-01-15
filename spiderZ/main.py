from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from SpiderUtils.enums import Language
from Statics.wordCount import WordCount
from ProcessPool.pool import PyPool
from QueueListener.listener import MyListener
from PyMemcached.memcacheUtil import MemcacheUtil
from SpiderUtils.bloomFilter import Bloom_Filter
from Consts.cacheKeyConstants import const

MemcacheUtil.clean()
MemcacheUtil.add(const.URLPOOLKEY, Bloom_Filter(1000))
queue = PyPool.get_queue()
lock = PyPool.get_lock()
listener = MyListener(lock, queue)
s = SpiderStrategy("http://www.baidu.com", 2, True, None, Language.Chinese)
Spider(s).get_all_words(queue, lock)
listener.listen()
WordCount.calc_count()
