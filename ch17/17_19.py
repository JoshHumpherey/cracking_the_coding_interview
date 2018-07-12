# Cracking the Coding Interview: 17.19
# Written by Josh Humphrey

def generate_missing_nums(limit, missing1, missing2):
    missing_numbers = []
    for i in range(limit):
        if i != missing1 and i != missing2:
            missing_numbers.append(i)
    return missing_numbers

def missing_one(arr):
    result = []
    sorted_arr = sorted(arr)
    for i in range(len(arr)-1):
        if arr[i+1] != (arr[i] + 1):
            result.append(arr[i]+1)
    return result

test_list = generate_missing_nums(2500, 1776, 1812)
result = missing_one(test_list)
print("The missing numbers are: " + str(result))
