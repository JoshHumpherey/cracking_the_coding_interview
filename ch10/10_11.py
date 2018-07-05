# Cracking the Coding Interview: 10.11
# Written by Josh Humphrey

arr = [0, 4, 3, 5, 7, 2, 9]

def brute_format(arr):
    sorted_arr = sorted(arr)
    for i in range(len(sorted_arr)):
        if (i % 2 == 1):
            temp = sorted_arr[i]
            sorted_arr[i] = sorted_arr[i-1]
            sorted_arr[i-1] = temp
    return   (sorted_arr)

res1 = brute_format(arr)
print("Brute Force Result: " + str(res1))
