from PyMemcached import lockModel
from Const import cacheKeyConstants
from PyMemcached.memcacheUtil import MemcacheUtil
from ProcessPool.pool import Pool
class ThreadPoolLock(lockModel):
    def __init__(self):
        self.__lock_key = cacheKeyConstants.PROCESSPOOLWRITEKEY
        
    def do(self):
        cache = MemcacheUtil.get(cacheKeyConstants.PROCESSPOOLCOUNTKEY)
        if(Pool.pool_limit(cache)==False):
            return False
        else:
            MemcacheUtil.set(cacheKeyConstants.PROCESSPOOLCOUNTKEY,cache+1)
            return MemcacheUtil.get(cacheKeyConstants.PROCESSPOOLKEY)