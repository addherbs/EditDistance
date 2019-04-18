class LRUCache (object):
    def __init__(self, capacity):
        import sys
        self.capacity = capacity
        self.d = {}
        self.p = {}
        self.count = 0
        self.low_priority = [0, 0]

    def get(self, key):
        if (key not in self.d): return -1
        # print ("get => d:{}, p:{}, lp:{}, c:{} ".format(self.d, self.p , self.low_priority, self.count))
        val = self.d[key]
        print ("val:", val)
        del self.d[key]
        del self.p[val[1]]
        self.generate_low_priority ()
        self.put (key, val[0], True)
        return val[0]

    def put(self, key, value, get_check=False):
        if (len (self.d) == self.capacity):
            del self.d[self.low_priority[1]]
            del self.p[self.low_priority[0]]
        self.count += 1
        print ("put1 => d:{}, p:{}, lp:{}, c:{} ".format (self.d, self.p, self.low_priority, self.count))
        self.d[key] = [value, self.count]
        print ("put1 => d:{}, p:{}, lp:{}, c:{} ".format (self.d, self.p, self.low_priority, self.count))
        self.p[self.count] = key
        print ("put2 => d:{}, p:{}, lp:{}, c:{} ".format (self.d, self.p, self.low_priority, self.count))
        if (not get_check): self.generate_low_priority ()

    def generate_low_priority(self):
        low_count = min (self.p.keys ())
        low_key = self.p[low_count]
        self.low_priority = [low_count, low_key]


        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)

cache = LRUCache( 2  )

cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)