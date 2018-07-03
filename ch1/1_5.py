# Cracking the Coding Interview: 1.5
# Written by Josh Humphrey
import collections

string1 = "pale"
string2 = "pal"

def find_one_away(string1, string2):
    l1 = len(string1)
    l2 = len(string2)
    if abs(l1-l2) > 1:
        return False

    if l1 > l2:
        max_string = string1
        min_string = string2
    else:
        max_string = string2
        min_string = string1

    max_c = collections.Counter(max_string)
    min_c = collections.Counter(min_string)

    for key in min_c:
        if key not in max_c:
            return False
    return True



res = find_one_away(string1,string2)
print(res)
