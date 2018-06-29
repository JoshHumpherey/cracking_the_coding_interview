# Cracking the Coding Interview: 4.1
# Written by Josh Humphrey

class Node():

    def __init__(self,data,adjacents):
        self.data = data
        self.adjacents = adjacents
        self.visited = False

def find_path(node1, node2):
    queue = []
    queue.append(node1)
    while(queue != []):
        current = queue.pop()
        for adjacent in current.adjacents:
            if adjacent.visited == False:
                if adjacent == node2:
                    return True
                else:
                    queue.append(adjacent)
        current.visited == True

    return False
