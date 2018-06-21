# Cracking the Coding Interview: 3.3
# Written by Josh Humphrey

class SetOfStacks():

    def __init__(self, stack_size):
        self.stack1 = []
        self.stack2 = []
        self.stack3 = []
        self.stack_size = stack_size

    def push(self,value):
        if len(self.stack1) > self.stack_size:
            self.stack1.append(value)
        elif len(self.stack2) > self.stack_size:
            self.stack2.append(value)
        else:
            self.stack3.append(value)

    def pop(self):
        if len(self.stack3) != 0:
            return self.stack3.pop()
        elif len(self.stack2) != 0:
            return self.stack2.pop()
        elif len(self.stack1) != 0:
            return self.stack1.pop()
        else:
            return None


my_stack = SetOfStacks(3)
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.push(7)
print(my_stack.stack1 + my_stack.stack2 + my_stack.stack3)
my_stack.pop()
my_stack.pop()
print(my_stack.stack1 + my_stack.stack2 + my_stack.stack3)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack.stack1 + my_stack.stack2 + my_stack.stack3)
