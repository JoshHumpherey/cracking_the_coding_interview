# Cracking the Coding Interview: 10.7
# Written by Josh Humphrey
import collections

def create_massive_list(limit, missing_bit):
    if missing_bit > limit:
        return None
    counter = 0
    very_large_array = []
    while (counter < limit):
        if counter != missing_bit-1:
            very_large_array.append(counter)
        counter += 1
    return very_large_array

massive_list = create_massive_list((2000000), 2789)

def generate_unique_bit(massive_list):
    bit_collection = collections.Counter(massive_list)
    index = 0
    while(True):
        if index not in bit_collection:
            return index
        else:
            index += 1

unique = generate_unique_bit(massive_list)
print("Unique Bit: " + str(unique))
