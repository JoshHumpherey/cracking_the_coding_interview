# Cracking the Coding Interview: 16.1
# Written by Josh Humphrey

arr = [-1000, 1]

def swap_in_place(arr, index1, index2):
    arr[index1] = arr[index1] - arr[index2]
    arr[index2] = arr[index1] + arr[index2]
    arr[index1] = arr[index2] - arr[index1]
    print("In-Place Swap: " + str(arr))

swap_in_place(arr,0,1)
