class LRUCache(object):

    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}
        self.order = []

    def get(self, key):
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) == self.cap:
            lru = self.order.pop(0)
            del self.cache[lru]
        self.cache[key] = value
        self.order.append(key)
