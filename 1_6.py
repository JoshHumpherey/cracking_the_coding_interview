# Cracking the Coding Interview: 1.6
# Written by Josh Humphrey

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

def rotate_matrix(mat, N):
    for x in range(0, int(N/2)):
        for y in range(0,N-x-1):
            temp = mat[x][y]
            # move values from right to top
            mat[x][y] = mat[N-y-1][x]
            # move values from bottom to right
            mat[N-1-y][x] = mat[N-1-x][N-1-y]
            # move values from left to bottom
            mat[N-1-x][N-1-y] = mat[y][N-x-1]
            # assign temp to left
            mat[y][N-x-1] = temp

    return mat

result = rotate_matrix(mat,3)
print(result)
