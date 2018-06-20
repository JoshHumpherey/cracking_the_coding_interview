# Cracking the Coding Interview: 1.4
# Written by Josh Humphrey
import collections

anagram1 = "ABCDEF"
anagram2 = "ACBDFE"

not1 = "ababab"
not2 = "ababcb"

def is_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    c1 = collections.Counter(string1)
    c2 = collections.Counter(string2)

    return c1 == c2


result1 = is_anagram(anagram1, anagram2)
print(result1)

result2 = is_anagram(not1, not2)
print(result2)
