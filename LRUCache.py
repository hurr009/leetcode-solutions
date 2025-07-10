class LRUCache:
    """Least Recently Used Cache"""

    def __init__(self, capacity: int):
        if capacity > 0 and capacity <= 3000:
            self.capacity = capacity
        self.cache = dict()
        self.cache2 = dict()
        self.usage = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            self.usage += 1
            self.cache2[key] = self.usage
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.usage += 1
        size = len(self.cache)
        
        if size < self.capacity:
            self.cache[key] = value
            self.cache2[key] = self.usage
        else:
            if key in self.cache:
                self.cache[key] = value
                self.cache2[key]=self.usage
                return            
            least_used = min(self.cache2, key=self.cache2.get)
            del self.cache[least_used]
            del self.cache2[least_used]
            self.cache[key] = value
            self.cache2[key] = self.usage
