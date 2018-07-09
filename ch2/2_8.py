# Cracking the Coding Interview: 2.7
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

l1 = [1, 2, 4, 2, 1, 9, 7]
l2 = [1, 5, 7, 2]

def create_linked_list(the_list):
    creation_node = ListNode(0)
    old_node = creation_node
    for value in the_list:
        new_node = ListNode(value)
        old_node.next = new_node
        old_node = old_node.next
    print("Original Node Values: " + str(the_list))
    return creation_node.next

def join_linked_lists(l1, l2, target):
    orig1 = l1
    orig2 = l2
    while (l1 != None and l2 != None):
        if l1.val == target and l2.val == target:
            l2.next = l1.next
        l1 = l1.next
        l2 = l2.next
    return orig1, orig2

def print_linked_list(head):
    head_vals = []
    while head != None:
        head_vals.append(head.val)
        head = head.next
    print("Printed values: " + str(head_vals))
# ------------- Problem ------------- #

def do_lists_intersect(l1, l2):
    nodemap = set()
    while (l1 != None):
        nodemap.add(l1)
        l1 = l1.next
    while (l2 != None):
        if l2 in nodemap:
            return True
        l2 = l2.next
    return False

l1 = create_linked_list(l1)
l2 = create_linked_list(l2)
l1, l2 = join_linked_lists(l1, l2, 2)
print_linked_list(l1)
print_linked_list(l2)
result = do_lists_intersect(l1, l2)
print(result)
