class Pool:
    cache_key = 'POOLCOUNT'
    limit = 4

    @staticmethod
    def pool_limit(count):
        if (count + 1 > Pool.limit):
            return False
        else:
            return True
