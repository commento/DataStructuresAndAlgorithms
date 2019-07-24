import collections

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.ordDictionary = collections.OrderedDict()
        self.capacity = capacity
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            return self.ordDictionary[key]
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at full capacity remove the oldest item.
        if len(self.ordDictionary) == 5:
            # FIFO approach, if LIFO is required, change to last=True
            self.ordDictionary.popitem(last=False)
        self.ordDictionary[key] = value


our_cache = LRU_Cache(5)


# Test 1
print("# Test 1: Normal Scenario")

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
our_cache.set('6', '6')
print(our_cache.get(1)   )   # returns -1
print(our_cache.get(2)   )   # returns 2
print(our_cache.get(3)   )   # return  3
print(our_cache.get(5)   )   # return  5
print(our_cache.get('6')   )   # return  6


# Test 2
print("# Test 2: Empty Cache")
our_cache2 = LRU_Cache(1)

print(our_cache2.get(1)   ) # returns -1


# Test 3
print("# Test 3: OverWritten Data")
our_cache.set(6, 6)
our_cache.set(7, 7)
our_cache.set(8, 8)
our_cache.set(9, 9)
our_cache.set(10, 10)
print(our_cache.get(1)   )   # returns -1
print(our_cache.get(2)   )   # returns -1
print(our_cache.get(3)   )   # return  -1
print(our_cache.get(5)   )   # return  -1
print(our_cache.get(10)   )   # return  10
