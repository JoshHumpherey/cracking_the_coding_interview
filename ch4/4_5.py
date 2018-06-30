# Cracking the Coding Interview: 4.5
# Written by Josh Humphrey

last_data = None

def is_BST(root):
    if root == None:
        return True

    if (is_BST(root.left) == False):
        return False
    if last_data != None and root.data <= last_data:
        return False
    last_data = root.data
    if (is_BST(root.right) == False):
        return False
    return True
