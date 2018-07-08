# Cracking the Coding Interview: 4.3
# Written by Josh Humphrey

class TreeNode():

    def __init(self,data):
        self.data = data
        self.left = None
        self.right = None

def listOfDepths(root):
    if not root:
        return []

    level_list = []
    current_level = 0
    queue = []
    queue.append((root, current_level))

    while queue:
        (node, current_level) = queue.pop(0)

        if len(level_list) == current_level:
            level_list.append([])
        level_list[current_level].append(node.data)
        current_level += 1

        if node.left:
            queue.append((node.left, current_level))
        if node.right:
            queue.append((node.right, current_level))
    return level_list
