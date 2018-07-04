# Cracking the Coding Interview: 10.3
# Written by Josh Humphrey

input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
normal = [1, 3, 4, 5, 7, 10, 14, 15, 16, 19, 20, 25]

def brute_force_lookup(input, target_num):
    for i in range(len(input)):
        if input[i] == target_num:
            return i
    return None

result = brute_force_lookup(input, 5)
print(result)
