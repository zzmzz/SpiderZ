from multiprocessing.pool import Pool
from multiprocessing import Manager
class PyPool:
    limit = 4

    @staticmethod
    def get_queue():
        m = Manager()
        q = m.Queue()
        return q

    @staticmethod
    def get_pool():
        return Pool(PyPool.limit)

    @staticmethod
    def get_lock():
        m = Manager()
        l = m.Lock()
        return l

