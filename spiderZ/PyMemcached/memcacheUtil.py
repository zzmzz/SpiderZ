import memcache

mc = memcache.Client(['127.0.0.1:11211'])


class MemcacheUtil:
    @staticmethod
    def get(key):
        return mc.get(key)

    @staticmethod
    def add(key, value):
        return mc.add(key, value)

    @staticmethod
    def set(key, value):
        return mc.set(key, value)

    @staticmethod
    def delete(key):
        try:
            mc.delete(key)
        except Exception as e:
            print e

    @staticmethod
    def clean():
        return mc.flush_all()
