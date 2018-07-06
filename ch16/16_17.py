# Cracking the Coding Interview: 16.17
# Written by Josh Humphrey

arr = [2, 20, -1000, 1000, 2, 0, -10]

def get_max_sum(arr):
    max_sum = 0
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if (sum > max_sum):
            max_sum = sum
        elif sum < 0:
            sum = 0
    return max_sum

result = get_max_sum(arr)
print(result)
