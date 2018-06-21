# Cracking the Coding Interview: 3.5
# Written by Josh Humphrey

class MyQueue():

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,value):
        if len(self.stack1) != 0:
            for i in range(len(self.stack1)):
                temp = self.stack1.pop()
                self.stack2.append(temp)
        self.stack1.append(value)
        if len(self.stack2) != 0:
            for i in range(len(self.stack2)):
                temp = self.stack2.pop()
                self.stack1.append(temp)

    def pop(self):
        if len(self.stack1) != 0:
            return self.stack1.pop()
        else:
            return None

my_queue = MyQueue()
my_queue.push(1)
print(my_queue.stack1)
my_queue.push(2)
print(my_queue.stack1)
my_queue.push(3)
print(my_queue.stack1)
my_queue.push(4)
print(my_queue.stack1)
my_queue.push(5)
print(my_queue.stack1)
result1 = my_queue.pop()
print(result1)
