# Cracking the Coding Interview: 17.10
# Written by Josh Humphrey

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
