# Cracking the Coding Interview: 8.8
# Written by Josh Humphrey

hashmap = dict()

def get_permutations_no_duplicates(string):
    permutations = []
    if string == None:
        return None
    if len(string) == 0:
        permutations.append("")
        return permutations
    string_list = list(string)
    for i in range(len(string)):
        before = string_list[:i]
        after = string_list[i+1:]
        partials = list(get_permutations_no_duplicates(before + after))

        for character in partials:
            temp = string_list[i] + character
            if temp not in hashmap:
                permutations.append(string_list[i] + character)
                hashmap[temp] = temp
    return permutations

test_string = "aaa"
result = get_permutations_no_duplicates(test_string)
print(result)
