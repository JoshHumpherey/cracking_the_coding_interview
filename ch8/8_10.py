# Cracking the Coding Interview: 8.10
# Written by Josh Humphrey
import time

img = [[0,0,0,0,0,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,1,0,0,0,0],
       [0,0,0,0,0,0,0,0,1,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,1,0,0,0],
       [0,0,0,0,0,1,0,0,0,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,0,0,0,0]]

def paint_fill(img, r, c, ncolor, ocolor):
    if (r < 0) or (c < 0) or (r >= len(img)) or (c >= len(img[0])):
        return False

    if img[r][c] == ocolor:
        img[r][c] = ncolor
        print_matrix(img)
        time.sleep(1)
        paint_fill(img, r+1, c, ncolor, ocolor)
        paint_fill(img, r-1, c, ncolor, ocolor)
        paint_fill(img, r, c+1, ncolor, ocolor)
        paint_fill(img, r, c-1, ncolor, ocolor)

    return True


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("")

paint_fill(img,3,7,1,0)
