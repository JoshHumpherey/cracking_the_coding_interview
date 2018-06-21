# Cracking the Coding Interview: 2.5
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

circle = [1,2,3,4,5,6,7,8,9]

def create_linked_list(the_list):
    creation_node = ListNode(0)
    old_node = creation_node
    for value in the_list:
        new_node = ListNode(value)
        old_node.next = new_node
        old_node = old_node.next
    print("Original Node Values: " + str(the_list))
    # Modified to return a circular linked list
    old_node = creation_node.next
    return creation_node.next

def print_linked_list(head):
    head_vals = []
    while head != None:
        head_vals.append(head.val)
        head = head.next
    print("Printed values: " + str(head_vals))

# ------------- Problem ------------- #

def detect_large_cycle(head):
    slowptr = head
    fastptr = head
    # Could sub in length of list if given option from LL class
    for i in range(100):
        if slowptr == fastptr:
            return slowptr.val
        else:
            slowptr = slowptr.next
            fastptr = fastptr.next.next

circularLL = create_linked_list(circle)
meeting = detect_large_cycle(circularLL)
print(meeting)
