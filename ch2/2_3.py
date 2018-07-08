# Cracking the Coding Interview: 2.3
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

sample_values = [1, 2, 3, 4, 5]

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

def return_val_3(head):
    while head.val != 3:
        head = head.next
    return head

# ------------- Problem ------------- #

def delete_node(head):
    head.val = head.next.val
    head.next = head.next.next
    return head

orig_head = create_linked_list()
middle_head = return_val_3(orig_head)
updated_head = delete_node(middle_head)
print_linked_list(orig_head)
