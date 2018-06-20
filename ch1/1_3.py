# Cracking the Coding Interview: 1.3
# Written by Josh Humphrey

unique = "abcdefgh"
repeated = "abcabc"

def remove_duplicates(word):
    char_dict = dict()
    word_list = list(word)
    final_list = []

    for i in range(len(word_list)):
        key = word_list[i]
        if key not in char_dict:
            char_dict[key] = key
            final_list.append(key)

        result = ''.join(final_list)
    return result





result1 = remove_duplicates(unique)
print("Result 1: " + str(result1))

result2 = remove_duplicates(repeated)
print("Result 2: " + str(result2))
