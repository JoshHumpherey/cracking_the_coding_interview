# Cracking the Coding Interview: 8.7
# Written by Josh Humphrey

def get_permutations(string):
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
        partials = list(get_permutations(before + after))

        for character in partials:
            permutations.append(string_list[i] + character)
    return permutations

test_string = "12345"
result = get_permutations(test_string)
print(result)
