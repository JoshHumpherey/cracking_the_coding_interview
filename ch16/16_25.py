# Cracking the Coding Interview: 16.25
# Written by Josh Humphrey
from datetime import datetime

class LRUCache():

    def __init__(self, size):
        self.storage = []
        self.size = size

    class Cache_Obj():

        def __init__(self, key, value, timestamp):
            self.key = key
            self.value = value
            self.timestamp = timestamp
            #print(str(self.key) + " has a timestamp of: " + str(self.timestamp))

    def push(self, key, value):
        if len(self.storage) == self.size:
            current = datetime.now()
            lru_time = current
            lru_item = None
            for cache_item in self.storage:
                if (cache_item.timestamp < lru_time):
                    lru_time = cache_item.timestamp
                    lru_item = cache_item
                    print("Updating cache")
                else:
                    print("LRU Time: " + str(lru_time) + " --- Cache Item Time: " + str(cache_item.timestamp))
            self.storage.remove(lru_item)

        cache_item = self.Cache_Obj(key, value, datetime.now())
        self.storage.append(cache_item)
        self.print_cache()

    def get(self, key):
        for cache_item in self.storage:
            if cache_item.key == key:
                cache_item.timestamp = datetime.now()
                return cache_item.value

    def print_cache(self):
        print("Current Cache: ")
        for item in self.storage:
            print("Cache Item: " + str(item.key) + " --- " + str(item.value) + " --- " + str(item.timestamp))
        print()

my_lru = LRUCache(3)
my_lru.push("1", "Ollie")
my_lru.push("2", "Fluffy")
my_lru.push("3", "Max")
