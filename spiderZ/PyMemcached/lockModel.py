from abc import ABCMeta, abstractmethod
from memcacheUtil import MemcacheUtil
from ProcessPool.pool import Pool
import time
import memcache


class LockModel:
    __metaclass__ = ABCMeta

    __lock_key = "WRITEKEY"

    def lock_and_do(self):
        is_loop = True
        while (is_loop):
            if (MemcacheUtil.get(self.__lock_key) is None and MemcacheUtil.add(self.__lock_key, True)):
                count = MemcacheUtil.get(Pool.cache_key)
                if (Pool.pool_limit(count)):
                    MemcacheUtil.set(Pool.cache_key, count + 1)
                    result = self.do()
                    MemcacheUtil.delete(self.__lock_key)

                    if(result!=False):
                        return result
                else:
                    time.sleep(0.1)
                    continue
            else:
                time.sleep(0.1)
                continue


    @abstractmethod
    def do(self):
        pass

