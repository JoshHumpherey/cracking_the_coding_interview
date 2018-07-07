# Cracking the Coding Interview: 16.24
# Written by Josh Humphrey

l1 = [2, 4, 6, 7, 8, 3, 9, 11, -1]

def brute_sum(l1, target):
    results = []
    for i in range(len(l1)):
        for j in range(i+1, len(l1)):
            if l1[i] + l1[j] == target:
                results.append([l1[i], l1[j]])
    return results

result = brute_sum(l1, 10)
print(result)
