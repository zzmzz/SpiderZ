from Queue import Queue
from ProcessPool.pool import PyPool
from SpiderUtils.spider import Spider
import time


class MyListener:
    __lock = None
    __queue = None
    __wait_cnt = 10

    def __init__(self):
        self.__pool = PyPool.get_pool()

    def listen(self, lock, queue):
        loop_flag = True
        loop_cnt = 0
        while (loop_flag):
            lock.acquire()
            size = queue.qsize()
            size = PyPool.limit if size > PyPool.limit else size
            loop_cnt = loop_cnt + 1 if size == 0 else 0
            for num in range(0, size):
                strategy = queue.get_nowait()
                self.__pool.apply_async(Spider(strategy).get_all_words, (queue, lock))
            lock.release()
            if (loop_cnt > 10):
                loop_flag = False
            else:
                time.sleep(1)
        self.__pool.close()
        self.__pool.join()
