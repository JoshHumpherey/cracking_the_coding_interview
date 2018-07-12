# Cracking the Coding Interview: 17.10
# Written by Josh Humphrey

arr = [1,2,4,7,7,7,4,4,1,4]

def brute_maj(arr):
    maj_count = 0
    maj_element = None
    for element in range(len(arr)):
        temp_count = 0
        temp_el = arr[element]
        for i in range(len(arr)):
            if arr[i] == temp_el:
                temp_count += 1
        if temp_count > maj_count:
            maj_count = temp_count
            maj_element = temp_el
    return maj_element

result1 = brute_maj(arr)
print("Brute Force Result: " + str(result1))
