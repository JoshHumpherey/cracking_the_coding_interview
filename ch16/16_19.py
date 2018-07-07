# Cracking the Coding Interview: 16.19
# Written by Josh Humphrey

land = [[0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]]

def survey_land(land):
    rows = len(land)
    columns = len(land[0])
    pond_sizes = []
    for r in range(rows):
        for c in range(columns):
            if land[r][c] == 0:
                size = get_pond_size(land, r, c)
                pond_sizes.append(size)
    return pond_sizes

def get_pond_size(land, r, c):
    if r < 0 or c < 0 or r >= len(land) or c >= len(land[0]) or land[r][c] != 0:
        return 0
    size = 1
    land[r][c] = -1
    size += get_pond_size(land,r+1,c)
    size += get_pond_size(land,r-1,c)
    size += get_pond_size(land,r,c+1)
    size += get_pond_size(land,r,c-1)
    return size



result = survey_land(land)
print("Pond Sizes: " + str(result))
