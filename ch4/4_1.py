# Cracking the Coding Interview: 4.1
# Written by Josh Humphrey

class Node():

    def __init__(self,data,adjacents):
        self.data = data
        self.adjacents = adjacents
        self.visited = False

def find_path(Node1, Node2):
    if Node1 == None or Node2 == None or Node1.visited == True:
        return False
    Node1.visited = True
    if Node1 == Node2:
        return True
    exit_var = False
    for adj in Node1.adjacents:
        exit_var = find_path(adj, Node2)
        if exit_var == True:
            return True
    return False
