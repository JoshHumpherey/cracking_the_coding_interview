# Cracking the Coding Interview: 2.1
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

sample_values = [1, 2, 3, 1, 2, 4, 5, 5]

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

head = create_linked_list()

def remove_duplicates(head):
    node_map = set()
    orig_head = head
    while head.next != None:
        key = head.next.val
        if key in node_map:
            head.next = head.next.next
            head = head.next
        else:
            node_map.add(key)
    print("NodeMap: " + str(node_map))
    return orig_head

test = create_linked_list()
print_linked_list(test)
