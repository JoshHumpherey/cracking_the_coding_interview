# Cracking the Coding Interview: 4.3
# Written by Josh Humphrey

class ListNode():

    def __init__(self,data):
        self.data = data
        self.next = None

class TreeNode():

    def __init(self,data):
        self.data = data
        self.left = None
        self.right = None

def list_of_depths(root, depth=0, depth_list=[]):
	if len(depth_list) <= depth:
		depth_list += [SinglyLinkedList()]
	depth_list[depth].append_to_tail(root.data)
	if root.left != None:
         list_of_depths(root.left, depth+1, depth_list)
	if root.right != None:
         list_of_depths(root.right, depth+1, depth_list)
    return depth_list
