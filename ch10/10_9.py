# Cracking the Coding Interview: 10.9
# Written by Josh Humphrey

matrix = [[1, 2, 3, 4, 5, 6, 7, 8 ],
          [10,12,15,16,18,19,20,21],
          [22,23,24,27,28,30,31,34],
          [35,36,37,38,39,40,44,47]]

def search_matrix(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])
    row_to_search = None
    for i in range(rows-1):
        if matrix[i][0] <= target and matrix[i+1][0] > target:
            row_to_search = i
            break
    for j in range(columns):
        if matrix[row_to_search][j] == target:
            return [row_to_search, j]
    return None



result = search_matrix(matrix, 30)
print(result)
