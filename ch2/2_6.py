# Cracking the Coding Interview: 2.6
# Written by Josh Humphrey

class ListNode(object):

    def __init__(self, value):
        self.val = value
        self.next = None

my_list = [1, 2, 4, 2, 1]

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

def is_LL_palindrome(head):
    val_array = []
    while head != None:
        temp = str(head.val)
        val_array.append(temp)
        head = head.next
    before = val_array
    val_array.reverse()
    return val_array == before

head = create_linked_list(my_list)
result = is_LL_palindrome(head)
print(result)
