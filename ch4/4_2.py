# Cracking the Coding Interview: 4.2
# Written by Josh Humphrey

class Node():

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


test_array = [1,2,3,4,5,6,7,8,9,10]

def create_minimal_tree(arr, left, right):
    if (right < left):
        return None
    mid = len(arr)//2
    root = Node(arr[mid])
    root.left = create_minimal_tree(arr, left, mid-1)
    root.right = create_minimal_tree(arr, mid+1, right)
    return root
