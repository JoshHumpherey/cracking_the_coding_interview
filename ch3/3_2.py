# Cracking the Coding Interview: 3.2
# Written by Josh Humphrey

class Stack():

    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)

    def pop(self):
        return self.storage.pop()

    def min_element(self):
        return min(self.storage)

my_stack = Stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
min_el = my_stack.min_element()
print("Min Element: " + str(min_el))
result = my_stack.pop()
print("Pop: " + str(result) )
