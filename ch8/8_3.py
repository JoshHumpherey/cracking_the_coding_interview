# Cracking the Coding Interview: 8.3
# Written by Josh Humphrey

l1 = [-10,-5,1,2,2,3,4,7,9,12,13]
l2 = [-10,-5,2,2,2,3,4,7,9,12,13]

def find_magic_index(arr):

    for i in range(len(arr)):
        if i == arr[i]:
            return i
    return -1

res1 = find_magic_index(l1)
print("Brute Force: " + str(res1))

def better_find_magic(arr,left,right):
    if (right < left):
        return -1

    mid = (left + right)//2
    if arr[mid] == mid:
        return mid

    if arr[mid] < mid:
        return better_find_magic(arr,mid+1,right)
    else:
        return better_find_magic(arr,left,mid-1)

res2 = better_find_magic(l1,0,len(l1)-1)
print("Binary Search: " + str(res2))
