# Cracking the Coding Interview: 10.8
# Written by Josh Humphrey
import random

def generate_list_with_duplicates(size):
    index = 0
    duplicates_list = [None] * size
    while (index < size):
        duplicates_list[index] = random.randint(0,size-1)
        index += 1
    return duplicates_list

duplicates_list = generate_list_with_duplicates(250000)

def print_duplicates(duplicates_list):
    hashmap = dict()
    count = 0
    for item in duplicates_list:
        if item in hashmap:
            print(item)
            count += 1
        else:
            hashmap[item] = item
    print("A total of %d duplicates were found!" % (count))

print_duplicates(duplicates_list)
