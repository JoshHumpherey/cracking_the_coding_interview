# Cracking the Coding Interview: 1.4
# Written by Josh Humphrey

def is_palindrome(a_str):
    fwd = list(a_str)
    bwd = fwd
    bwd.reverse()
    return fwd == bwd

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
            the_string = string_list[i] + character
            if is_palindrome(the_string) == True:
                permutations.append(the_string)
    return permutations

result = get_permutations("tacocat")
print(result)
