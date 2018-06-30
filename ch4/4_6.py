# Cracking the Coding Interview: 4.6
# Written by Josh Humphrey

def successor(node):
	if node.right != None:
		successor = node.right
		while successor.left != None:
			successor = successor.left
			return successor
	elif node.parent:
		while node.parent != None:
			if node.parent.left == node:
				return parent
			else:
				node = node.parent
		return None

	else:
        return None
