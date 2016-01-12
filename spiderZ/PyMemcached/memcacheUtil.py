import memcache

mc = memcache.Client(['127.0.0.1:11211'], debug=True)


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
        return mc.delete(key)


a = MemcacheUtil.get("a")
b = MemcacheUtil.add("a", 1)
c = MemcacheUtil.delete("a")
d = MemcacheUtil.set("a","1")
e = 1