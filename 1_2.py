# Cracking the Coding Interview: 1.2
# Written by Josh Humphrey

null_string  = "abcdef" + '\0'

def reverse_null_string(nullstring):
    null_char = '\x00'
    string = nullstring.strip(null_char)
    string_list = list(string)
    string_list.reverse()
    final = ''.join(string_list)
    return final


result = reverse_null_string(null_string)
print(result)
