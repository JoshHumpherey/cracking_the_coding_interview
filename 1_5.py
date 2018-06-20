# Cracking the Coding Interview: 1.5
# Written by Josh Humphrey

test_string = "The Lazy Brown Fox Jumped Over The Log"

def fill_spaces(test_string):
    fill_char = '%20'
    test_list = list(test_string)
    for i in range(len(test_list)):
        if test_list[i] == " ":
            test_list[i] = fill_char
    result = ''.join(test_list)
    return result


result = fill_spaces(test_string)
print(result)
