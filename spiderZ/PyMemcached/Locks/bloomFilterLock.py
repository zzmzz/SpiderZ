from PyMemcached.lockModel import LockModel
from Consts.cacheKeyConstants import const
from PyMemcached.memcacheUtil import MemcacheUtil
from Utils.logFactory import LogFactory
from SpiderUtils.bloomFilter import SpiderBloomFilter
logger = LogFactory.getlogger("BloomFilterLock")

class BloomFilterLock(LockModel):
    __url = None

    def __init__(self, url):
        self.__url = url
        super(BloomFilterLock, self).__init__(const.URLWRITEKEY)

    def do(self):
        if SpiderBloomFilter.exists(self.__url):
            logger.debug("dup url: "+self.__url)
            return False
        else:
            logger.debug("access url: "+self.__url)
            return True
