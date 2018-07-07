# Cracking the Coding Interview: 16.21
# Written by Josh Humphrey

l1 = [4,1,2,1,1,2]
l2 = [3,6,3,3]

def compute_list_sum(a_list):
    total = 0
    for i in range(len(a_list)):
        total += a_list[i]
    return total

def brute_force_sum(l1, l2):
    sum1 = compute_list_sum(l1)
    sum2 = compute_list_sum(l2)
    for elem1 in l1:
        for elem2 in l2:
            new_sum1 = sum1-elem1+elem2
            new_sum2 = sum2-elem2+elem1
            if new_sum1 == new_sum2:
                return [elem1, elem2]
    return None

res1 = brute_force_sum(l1,l2)
print("Brute Force Result: " + str(res1))

def elegant_sum(l1, l2):
    sum1 = compute_list_sum(l1)
    sum2 = compute_list_sum(l2)
    diff = abs(sum1-sum2)
    for elem1 in l1:
        elem2 = diff - elem1
        if elem2 in l2:
            return [elem1, elem2]
    return None

res2 = elegant_sum(l1, l2)
print("Elegant Result: " + str(res2))
