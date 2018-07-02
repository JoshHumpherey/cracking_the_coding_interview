# Cracking the Coding Interview: 1.2
# Written by Josh Humphrey

import collections

string1 = "abcad"
string2 = "baadc"
string3 = "bacdd"

def is_permutation(string1, string2):
    c1 = collections.Counter(string1)
    c2 = collections.Counter(string2)
    return c1 == c2

res1 = is_permutation(string1,string2)
print(res1)

res2 = is_permutation(string1, string3)
print(res2)
