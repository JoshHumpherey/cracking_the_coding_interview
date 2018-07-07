# Cracking the Coding Interview: 4.2
# Written by Josh Humphrey

class Node():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


test_array = [1,2,3,4,5,6,7,8,9,10]

def create_min_tree(test_array, left, right):
    if (right < left):
        return None
    mid = (left + right)//2
    root = Node(test_array[mid])
    root.left = create_min_tree(test_array, left, mid-1)
    root.right = create_min_tree(test_array, mid+1, right)
    return root

result = create_min_tree(test_array, 0, len(test_array)-1)
