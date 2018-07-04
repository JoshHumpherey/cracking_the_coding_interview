# Cracking the Coding Interview: 10.5
# Written by Josh Humphrey
# This works assuming that both endpoints are populated with a non-empty string

search_array = ["at","","","","ball","","","car","","","dad","","egg","fluffy"]

def brute_sparse(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

res1 = brute_sparse(search_array, "ball")
print("Brute Force: " + str(res1))

def faster_sparse(arr, target, left, right):
    if right <= left:
        return right
    temp = (left + right)//2
    midpoint = find_midpoint(arr, temp)
    if target == arr[midpoint]:
        return midpoint
    elif target < arr[midpoint]:
        return faster_sparse(arr, target, left, midpoint-1)
    else:
        return faster_sparse(arr, target, midpoint+1, right)

def find_midpoint(arr, index):
    if arr[index] != "":
        return index
    else:
        return find_midpoint(arr, index-1)

res2 = faster_sparse(search_array, "egg", 0, len(search_array)-1)
print("Modified Binary Search: " + str(res2))
