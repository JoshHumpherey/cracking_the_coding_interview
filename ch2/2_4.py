# Cracking the Coding Interview: 2.4
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

list1 = [3, 1, 5]
list2 = [5, 9, 2]

def create_linked_list(the_list):
    creation_node = ListNode(0)
    old_node = creation_node
    for value in the_list:
        new_node = ListNode(value)
        old_node.next = new_node
        old_node = old_node.next
    print("Original Node Values: " + str(the_list))
    return creation_node.next

def print_linked_list(head):
    head_vals = []
    while head != None:
        head_vals.append(head.val)
        head = head.next
    print("Printed values: " + str(head_vals))

# ------------- Problem ------------- #

def add_lists(l1,l2,carry, head):
    if l1 == None and l2 == None:
        return None
    node_val = carry
    if l1 != None:
        node_val += l1.val
    if l2 != None:
        node_val += l2.val

    if node_val > 10:
        carry = 1

    head.val = node_val % 10
    head.next = ListNode(0)
    add_lists(l1.next,l2.next,carry,head.next)

    return head






master = create_linked_list([0])
l1 = create_linked_list(list1)
l2 = create_linked_list(list2)
result = add_lists(l1,l2,0,master)
print_linked_list(result)
