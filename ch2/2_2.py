# Cracking the Coding Interview: 2.2
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

sample_values = [1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8]

def create_linked_list():
    creation_node = ListNode(0)
    old_node = creation_node
    for value in sample_values:
        new_node = ListNode(value)
        old_node.next = new_node
        old_node = old_node.next
    print("Original Node Values: " + str(sample_values))
    return creation_node.next

def print_linked_list(head):
    head_vals = []
    while head != None:
        head_vals.append(head.val)
        head = head.next
    print("Printed values: " + str(head_vals))

# ------------- Problem ------------- #

def get_linked_length(head):
    length = 0
    while (head.next != None):
        length += 1
        head = head.next
    return length

def get_nth_node(head, n):
    linked_length = get_linked_length(head)
    target = (linked_length-n)
    index = 0
    while (index <= target):
        head = head.next
        index += 1
    return head.val

head = create_linked_list()
result = get_nth_node(head,2)
print(result)
