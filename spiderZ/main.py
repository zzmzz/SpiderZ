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
s = SpiderStrategy("http://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=mswin_oem_dg&wd=whether&oq=weather&rsv_pq=bb20eb2d00102826&rsv_t=33255cebUHcA9emwJid%2FQgpo6%2B4Mkranpw3jkl%2FWwQ2%2B68%2BNfayWpMuST72EGb3RFDB%2B&rsv_enter=1&rsv_sug3=4&rsv_sug1=4&rsv_sug7=100&rsv_sug2=0&prefixsug=weth&rsp=1&inputT=3915&rsv_sug4=3915&rsv_sug=1", 3, True, None, Language.All)
Spider(s).get_all_words(queue, lock)
listener.listen(lock, queue)
WordCount.calc_count()
