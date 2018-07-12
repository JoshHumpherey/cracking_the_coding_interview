# Cracking the Coding Interview: 17.10
# Written by Josh Humphrey

<<<<<<< HEAD
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
=======
list1 = [1,2,5,9,5,5,5]
list = [1,2,3,4]

def get_majority_element(mylist):
    hashmap = dict()
    for i in range(len(mylist)):
        key = mylist[i]
        if key in hashmap:
            hashmap[key] += 1
        else:
            hashmap[key] = 0
    max_key = -1
    max_val = 0
    for key in hashmap:
        if hashmap[key] > max_val:
            max_val = hashmap[key]
            max_key = key
    return max_key

result = get_majority_element(list)
print("Majority Element: " + str(result))
>>>>>>> d64094ccbdbd55ab4c27e332761ec30b1f36283d
