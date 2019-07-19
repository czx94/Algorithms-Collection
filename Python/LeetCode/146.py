from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.size = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        v = self.cache.pop(key)
        self.cache[key] = v
        return v

    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        else:
            if self.size > 0:
                self.size -= 1
            else:
                self.cache.popitem(last=False)
        self.cache[key] = value
