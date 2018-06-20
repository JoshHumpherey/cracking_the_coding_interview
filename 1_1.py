# Cracking the Coding Interview: 1.1
# Written by Josh Humphrey

unique = "abcdefgh"
repeated = "abcdefagh"

def is_string_unique(word):
    char_dict = dict()
    word_list = list(word)
    for i in range(len(word)):
        key = word_list[i]
        if key in char_dict:
            return False
        else:
            char_dict[key] = key
    return True





result1 = is_string_unique(unique)
result2 = is_string_unique(repeated)
print("Result 1: " + str(result1))
print("Result 2: " + str(result2))
