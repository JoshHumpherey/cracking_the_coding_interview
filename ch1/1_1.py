# Cracking the Coding Interview: 1.1
# Written by Josh Humphrey

unique_string = "abcdefg"
duplicate_string = "abbcdefgg"

def contains_duplicates(string):
    hashmap = dict()
    string_list = list(string)
    for i in range(len(string)):
        if string_list[i] not in hashmap:
            key = string_list[i]
            hashmap[key] = key
        else:
            return True
    return False

res1 = contains_duplicates(unique_string)
print(res1)
res2 = contains_duplicates(duplicate_string)
print(res2)
