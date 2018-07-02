# Cracking the Coding Interview: 1.3
# Written by Josh Humphrey

string1 = "Mr John Smith"

def urlify(string):
    REPLACEMENT = "%20"
    string_list = list(string)
    for i in range(len(string_list)):
        if string_list[i] == " ":
            string_list[i] = REPLACEMENT

    return ''.join(string_list)

res = urlify(string1)
print(res)
