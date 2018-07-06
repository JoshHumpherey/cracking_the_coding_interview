# Cracking the Coding Interview: 16.11
# Written by Josh Humphrey

def get_lengths(k, total, shorter, longer, hashlengths):
    if k == 0:
        hashlengths.add(total)
        return
    get_lengths(k-1, total + shorter, shorter, longer, hashlengths)
    get_lengths(k-1, total + longer, shorter, longer, hashlengths)
    return hashlengths

result = get_lengths(13, 0, 1, 2, set())
print(result)
