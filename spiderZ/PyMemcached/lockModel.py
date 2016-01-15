from abc import ABCMeta, abstractmethod
from memcacheUtil import MemcacheUtil
import time


class LockModel:
    __metaclass__ = ABCMeta

    __lock_key = "WRITEKEY"

    def lock_and_do(self):
        is_loop = True
        while (is_loop):
            if (MemcacheUtil.get(self.__lock_key) is None and MemcacheUtil.add(self.__lock_key, True)):
                result = None
                try:
                    result = self.do()
                except Exception as e:
                    print(e)
                finally:
                    MemcacheUtil.delete(self.__lock_key)
                return result
            else:
                time.sleep(0.1)
                continue


@abstractmethod
def do(self):
    pass
