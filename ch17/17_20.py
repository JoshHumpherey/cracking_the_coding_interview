# Cracking the Coding Interview: 17.20
# Written by Josh Humphrey
import heapq

class Data():
    def __init__(self):
        self.storage = []

    def get_median(self):
        length = len(self.storage)-1
        mid = length//2
        if len(self.storage) % 2 == 0:
            m1 = mid-1
            m2 = mid
            return (self.storage[m1] + self.storage[m2])/2
        else:
            return self.storage[mid]

    def push(self, data):
        self.storage.append(data)
        self.storage = sorted(self.storage)

my_class = Data()
my_class.push(2)
my_class.push(1)
res1 = my_class.get_median()
my_class.push(3)
res2 = my_class.get_median()
print("Median 1: " + str(res1) + ", Median 2: " + str(res2))
