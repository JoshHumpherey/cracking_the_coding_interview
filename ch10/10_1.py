# Cracking the Coding Interview: 10.1
# Written by Josh Humphrey

# Not finished -- space at end of array A is unclear?
A = [1,3,5,7,9,10,11,0,0,0,0,0]
B = [2,4,6,8,12]

def merge_into(A, B, last_A, last_B):
    index_A = last_A-1 # Last index of array A
    index_B = last_B-1 # Last index of array B
    index_merged = last_A + last_B -1 # Last index of merged array

    while (index_B >= 0):
        if (index_A >= 0 and A[index_A] > B[index_B]):
            A[index_merged] = A[index_A]
            index_A -= 1
        else:
            print("meged index: " + str(index_merged))
            A[index_merged] = B[index_B]
            index_B -= 1
        index_merged -= 1
    return A

result = merge_into(A, B, len(A), len(B))
print(result)
