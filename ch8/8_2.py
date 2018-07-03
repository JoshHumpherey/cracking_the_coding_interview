# Cracking the Coding Interview: 8.2
# Written by Josh Humphrey
# 1's are walkable while 0's are blockades

grid = [[1,0,1,1,1,0,0],
        [1,1,1,1,1,1,1],
        [1,1,0,1,1,0,1],
        [0,0,0,1,1,1,1]]

def find_path(grid):
    if grid is None or len(grid) == 0:
        return None
    path = list()
    if calc_path(grid, len(grid)-1, len(grid[0])-1, path):
        return path
    return None

def calc_path(grid, row, col, path):
    if row < 0 or col < 0 or not grid[row][col]:
        return False
    is_at_origin = (row == 0) and (col == 0)
    if is_at_origin or calc_path(grid, row-1, col, path) or calc_path(grid, row, col-1, path):
        path.append((row,col))
        return True
    return False

result = find_path(grid)
print("Path: " + str(result))
