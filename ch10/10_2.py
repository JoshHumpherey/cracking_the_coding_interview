# Cracking the Coding Interview: 10.2
# Written by Josh Humphrey

# Group string anagrams together.
from collections import defaultdict
anagram_list = ['hello', 'world', 'doggo', 'holel', 'googd', 'rldwo', 'lasdasd']

def group_anagrams(anagram_list):
    mapping = defaultdict(list)
    output = []
    for item in anagram_list:
        key = ''.join(sorted(item))
        mapping[key].append(item)

    for key in mapping:
        for item in mapping[key]:
            output.append(item)
    return output



result = group_anagrams(anagram_list)
print(result)
