from PyMemcached.lockModel import LockModel
from Consts.cacheKeyConstants import const
from PyMemcached.memcacheUtil import MemcacheUtil


class BloomFilterLock(LockModel):
    __url = None

    def __init__(self, url):
        self.__lock_key = const.URLWRITEKEY
        self.__url = url

    def do(self):
        pool = MemcacheUtil.get(const.URLPOOLKEY)
        if (pool.exists(self.__url)):
            return False
        else:
            pool.mark_value(self.__url)
            MemcacheUtil.set(const.URLPOOLKEY, pool)
            return True
