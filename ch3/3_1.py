# Cracking the Coding Interview: 3.1
# Written by Josh Humphrey

the_list = [1,2,3,4,5,6,7,8,9]

def three_stacks(the_list, n):
    master_stack = [None]*n
    stack1 = master_stack[0:n/3]
    stack2 = master_stack[n/3:2*n/3]
    stack3 = master_stack[2*n/3:n]
    return stack1,stack2,stack3
