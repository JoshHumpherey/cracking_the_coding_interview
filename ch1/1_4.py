# Cracking the Coding Interview: 1.4
# Written by Josh Humphrey

def is_palindrome(a_str, full_length):
    fwd = list(a_str)
    bwd = fwd
    bwd.reverse()
    return (fwd == bwd) and full_length == len(fwd)

def get_permutations(string, orig_len):
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
        partials = list(get_permutations((before + after), orig_len))

        for character in partials:
            the_string = string_list[i] + character
            print(the_string)
            if is_palindrome(the_string, orig_len) == True:
                permutations.append(the_string)
    return permutations

test = "abba"
result = get_permutations(test, len(test))
print(result)
