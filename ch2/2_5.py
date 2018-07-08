# Cracking the Coding Interview: 2.5
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

l1 = [3, 2, 1]
l2 = [4, 1, 9]

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
# Assuming both linked lists are the same size.. #

def add_lists(l1, l2):
    orig = ListNode(0)
    head = orig
    carry = 0
    while (l1 != None):
        sum = carry + l1.val + l2.val
        print(sum)
        if sum >= 10:
            head.val = 1
            carry = sum - 9
        else:
            head.val = sum

        head.next = ListNode(0)
        head = head.next
        l1 = l1.next
        l2 = l2.next
    return orig

l1 = create_linked_list(l1)
l2 = create_linked_list(l2)

result = add_lists(l1, l2)
print_linked_list(result)
