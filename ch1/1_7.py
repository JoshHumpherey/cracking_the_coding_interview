# Cracking the Coding Interview: 1.7
# Written by Josh Humphrey

mat = [[1,2,0],[4,5,6],[0,8,9]]

def set_to_zero(matrix):
    xzeros = []
    yzeros = []
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            if y == 0:
                xzeros.append(x)
                yzeros.append(y)

    print(xzeros)
    print(yzeros)
    
    for x in xzeros:
        matrix[x][0] = 0

    return matrix

result = set_to_zero(mat)
print(result)
