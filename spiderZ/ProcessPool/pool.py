from PyMemcached.memcacheUtil import MemcacheUtil
from Const import cacheKeyConstants
from multiprocessing.pool import Pool
from multiprocessing import Manager
import sys
sys.argv=[]
class PyPool:
    limit = 4

    @staticmethod
    def get_instance():
        if __name__ == '__main__':
            m = Manager()
        v = m.dict()
        assert isinstance(v, dict)
        v[cacheKeyConstants.PROCESSPOOLKEY]=Pool(PyPool.limit)
        return v


