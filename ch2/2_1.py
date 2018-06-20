# Cracking the Coding Interview: 2.1
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

def remove_duplicates(head):
    node_map = set()
    orig_head = head
    trail = None
    while head != None:
        key = head.val
        if key in node_map:
            tail.next = head.next
            head = head.next
        else:
            node_map.add(key)
            tail = head
            head = head.next

    print("NodeMap: " + str(node_map))
    return orig_head

head = create_linked_list()
result = remove_duplicates(head)
print_linked_list(result)
