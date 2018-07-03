# Cracking the Coding Interview: 8.10
# Written by Josh Humphrey

img = [[0,0,0,0,0,0,0,1,0,0,0,0,0],
       [0,0,0,0,0,1,1,0,1,0,0,0,0],
       [0,0,0,0,1,0,0,0,1,0,0,0,0],
       [0,0,0,0,0,1,0,0,0,1,0,0,0],
       [0,0,0,0,0,1,1,1,1,0,0,0,0]]

def paint_fill(img, row, col, fill_value,orig_val):
    if img[row][col] == orig_val:
        img[row][col] = fill_value
        paint_fill(img,row+1,col,fill_value,orig_val)
        paint_fill(img,row-1,col,fill_value,orig_val)
        paint_fill(img,row,col+1,fill_value,orig_val)
        paint_fill(img,row,col-1,fill_value,orig_val)
        return img
    else:
        return img

result = paint_fill(img,3,7,1,0)
print(result)
