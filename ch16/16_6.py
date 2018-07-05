# Cracking the Coding Interview: 16.6
# Written by Josh Humphrey
import math

l1 = [1,3,15,11,2]
l2 = [23,127,235,19,8]

def find_smallest_diff(l1,l2):
    sort1 = sorted(l1)
    sort2 = sorted(l2)
    len1 = len(l1)
    len2 = len(l2)
    ptr1 = 0
    ptr2 = 0
    best_min = math.inf
    best_pair = [None, None]
    while(ptr1 < len1-1 and ptr2 < len2-1):
        difference = abs(sort1[ptr1]-sort2[ptr2])
        if difference < best_min:
            best_min = difference
            best_pair = [sort1[ptr1],sort2[ptr2]]
        if sort1[ptr1+1] < sort2[ptr2+1]:
            ptr1 += 1
        else:
            ptr2 += 2
    return best_pair

result = find_smallest_diff(l1,l2)
print(result)
