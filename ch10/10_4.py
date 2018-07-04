# Cracking the Coding Interview: 10.4
# Written by Josh Humphrey

class Listy():

    def __init__(self):
        self.data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

    def access_element(self,index):
        if len(self.data) - 1 < index:
            return -1
        else:
            return self.data[index]

def find_listy_size(listy):
    temp = 1
    while(True):
        if listy.access_element(temp-1) == -1:
            return int(temp/2)
        else:
            temp *= 2

def search_listy(target, length, left, right, listy):
    if right < left:
        return right

    mid = (left + right)//2
    if listy.data[mid] > target:
        return search_listy(target, length, left, mid-1, listy)
    else:
        return search_listy(target, length, mid+1, right, listy)

listy = Listy()
length = find_listy_size(listy)
result = search_listy(5, length, 0, length-1, listy)
print(result)
