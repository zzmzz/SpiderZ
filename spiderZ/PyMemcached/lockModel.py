import time
from abc import ABCMeta, abstractmethod

from Utils.logFactory import LogFactory
from memcacheUtil import MemcacheUtil

logger = LogFactory.getlogger("LockModel")

class LockModel:
    __metaclass__ = ABCMeta

    __lock_key = "WRITEKEY"

    def __init__(self, key):
        self.__lock_key = key

    def lock_and_do(self):
        is_loop = True
        while (is_loop):
            # print "loop",self.__lock_key
            if (MemcacheUtil.get(self.__lock_key) is None):
                if (MemcacheUtil.add(self.__lock_key, True)):
                    logger.debug("get memcache lock: " + self.__lock_key)
                    result = None
                    try:
                        result = self.do()
                    except Exception as e:
                        logger.error(e)
                    finally:
                        MemcacheUtil.delete(self.__lock_key)
                        logger.debug("release memcache lock: " + self.__lock_key)
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
