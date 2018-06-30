# Cracking the Coding Interview: 4.4
# Written by Josh Humphrey

def check_if_balanced(root):
    if max_height == None:
        return None
    height_diff = find_height(root.left) - find_height(root.right);
    if (abs(height_diff) > 1):
        return False
    else:
        return check_if_balanced(root.left) and check_if_balanced(root.right)




def find_height(root):
    if root == None:
        return -1
    else:
        return max(find_height(root.left), find_height(root.right)) + 1
