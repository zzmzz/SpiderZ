import memcache


class MemcacheUtil:
    @staticmethod
    def get(key):
        mc = memcache.Client(['127.0.0.1:11211'])
        return mc.get(key)

    @staticmethod
    def add(key, value):
        mc = memcache.Client(['127.0.0.1:11211'])
        return mc.add(key, value)

    @staticmethod
    def set(key, value):
        mc = memcache.Client(['127.0.0.1:11211'])
        return mc.set(key, value)

    @staticmethod
    def delete(key):
        try:
            mc = memcache.Client(['127.0.0.1:11211'])
            mc.delete(key)
        except Exception as e:
            print e

    @staticmethod
    def clean():
        mc = memcache.Client(['127.0.0.1:11211'])
        return mc.flush_all()
