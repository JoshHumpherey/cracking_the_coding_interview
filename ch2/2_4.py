# Cracking the Coding Interview: 2.4
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

my_list = [3, 5, 8, 5, 10, 2, 1]

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
def partition(my_list):
    sorted_list = sorted(my_list)
    orig = ListNode(None)
    head = orig
    for i in range(len(sorted_list)-1):
        head.val = sorted_list[i]
        head.next = ListNode(sorted_list[i+1])
        head = head.next
    return orig




head = create_linked_list(my_list)
result = partition(my_list)
print_linked_list(result)
