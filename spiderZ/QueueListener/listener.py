import time

from ProcessPool.pool import PyPool
from SpiderUtils.spider import Spider
from Utils.logFactory import LogFactory


class MyListener:
    __lock = None
    __queue = None
    __wait_cnt = 10
    logger = LogFactory.getlogger("MyListener")

    def __init__(self):
        self.__pool = PyPool.get_pool()

    def listen(self, lock, queue):
        loop_flag = True
        loop_cnt = 0
        while loop_flag:
            try:
                lock.acquire()
                size = queue.qsize()
                size = PyPool.limit if size > PyPool.limit else size
                for num in range(0, size):
                    strategy = queue.get_nowait()
                    self.__pool.apply_async(applySpider, (strategy, queue, lock))
            except Exception, e:
                self.logger.error(e)
            finally:
                lock.release()

            try:
                lock.acquire()
                size = queue.qsize()
                if size == 0:
                    loop_cnt += 1
                else:
                    loop_cnt = 0
                if loop_cnt > 100:
                    loop_flag = False
            except Exception, e:
                self.logger.error(e)
            finally:
                lock.release()
                time.sleep(1)

        self.__pool.close()
        self.__pool.join()


def applySpider(strategy, queue, lock):
    Spider(strategy).get_all_words(queue, lock)
