import memcache
from Utils.config import Config
class MemcacheUtil:
    url = Config.getProperty("memcached","addr")
    @staticmethod
    def get(key):
        mc = memcache.Client([MemcacheUtil.url])
        return mc.get(key)

    @staticmethod
    def add(key, value):
        mc = memcache.Client([MemcacheUtil.url])
        return mc.add(key, value)

    @staticmethod
    def set(key, value):
        mc = memcache.Client([MemcacheUtil.url])
        return mc.set(key, value)

    @staticmethod
    def delete(key):
        try:
            mc = memcache.Client([MemcacheUtil.url])
            mc.delete(key)
        except Exception as e:
            print e

    @staticmethod
    def clean():
        mc = memcache.Client([MemcacheUtil.url])
        return mc.flush_all()
