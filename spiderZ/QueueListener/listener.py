import time

from ProcessPool.pool import PyPool
from SpiderUtils.spider import Spider
from Utils.logFactory import LogFactory
from PyMemcached.Locks.processCntLock import ProcessCntReduce, ProcessCntIncrease
from PyMemcached.memcacheUtil import MemcacheUtil
from Consts.cacheKeyConstants import const
from Utils.logFactory import LogFactory

logger = LogFactory.getlogger("MyListener")


class MyListener:
    __lock = None
    __queue = None
    __wait_cnt = 10

    def __init__(self):
        self.__pool = PyPool.get_pool()

    def listen(self, lock, queue):
        loop_flag = True
        while loop_flag:
            try:
                lock.acquire()
                size = queue.qsize()
                size = PyPool.limit if size > PyPool.limit else size
                for num in range(0, size):
                    strategy = queue.get_nowait()
                    ProcessCntIncrease().lock_and_do()
                    self.__pool.apply_async(apply_spider, (strategy, queue, lock))
            except Exception, e:
                logger.error(e)
            finally:
                lock.release()

            try:
                lock.acquire()
                length = MemcacheUtil.get(const.PROCESSCNTKEY)
                size = queue.qsize()
                if size == 0 and length == 0:
                    loop_flag = False
                else:
                    time.sleep(3)
            except Exception, e:
                logger.error(str(e))
            finally:
                lock.release()

        self.__pool.close()
        logger.info("start to wait for all processes")
        self.__pool.join()
        return


def apply_spider(strategy, queue, lock):
    try:
        Spider(strategy).get_all_words(queue, lock)
    except BaseException, e:
        logger.error(str(e))
    finally:
        run_after_end()
    return


def run_after_end():
    ProcessCntReduce().lock_and_do()
    return
