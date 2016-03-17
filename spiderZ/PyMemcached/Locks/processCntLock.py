from PyMemcached.lockModel import LockModel
from Consts.cacheKeyConstants import const
from PyMemcached.memcacheUtil import MemcacheUtil
from Utils.logFactory import LogFactory

logger = LogFactory.getlogger("ProcessCnt")

class ProcessCntIncrease(LockModel):

    def __init__(self):
        super(ProcessCntIncrease, self).__init__(const.PROCESSWRITEKEY)

    def _do(self):
        cnt = MemcacheUtil.get(const.PROCESSCNTKEY)
        if cnt is None:
            cnt = 1
        else:
            cnt += 1
        MemcacheUtil.set(const.PROCESSCNTKEY, cnt)
        logger.debug("process cnt:"+str(cnt))
        return True


class ProcessCntReduce(LockModel):

    def __init__(self):
        super(ProcessCntReduce, self).__init__(const.PROCESSWRITEKEY)

    def _do(self):
        cnt = MemcacheUtil.get(const.PROCESSCNTKEY)
        cnt -= 1
        MemcacheUtil.set(const.PROCESSCNTKEY, cnt)
        logger.debug("process cnt:"+str(cnt))
        return True
