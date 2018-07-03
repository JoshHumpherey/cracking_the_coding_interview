# Cracking the Coding Interview: 1.9
# Written by Josh Humphrey
import collections

s1 = "waterbottle"
s2 = "bottlewater"

def is_rotation(s1, s2):
    c1 = collections.Counter(s1)
    c2 = collections.Counter(s2)
    return c1 == c2


res = is_rotation(s1,s2)
print(res)
