# Cracking the Coding Interview: 1.6
# Written by Josh Humphrey

test_string1 = "aabcccccaaabbbbbbbbcde"
test_string2 = "abcdeffff"

def compress_string(long_string):
    orig_len = len(long_string)
    if orig_len == 0:
        return None

    long_list = list(long_string)
    temp_char = long_list[0]
    temp_count = 1
    output = []
    for i in range(1, len(long_list)):
        if long_list[i] == temp_char:
            temp_count += 1
            if len(long_list)-1 == i:
                output.append(str(temp_char)+str(temp_count))

        else:
            output.append(str(temp_char)+str(temp_count))
            temp_count = 1
            temp_char = long_list[i]
            if len(long_list)-1 == i:
                output.append(str(temp_char)+str(temp_count))

    result = ''.join(output)
    if len(output)*2 > orig_len:
        return long_string
    else:
        return result

result1 = compress_string(test_string1)
print(result1)
result2 = compress_string(test_string2)
print(result2)
