# Cracking the Coding Interview: 16.4
# Written by Josh Humphrey

board = [["o",None, "o"],
         ["x","o",None],
         ["x",None, "o"]]

def has_won(board, p1, p2):

    for row in range(len(board)):
        hcount = 0
        hchar = ""
        for column in range(len(board)):
            if column == 0:
                hcount += 1
                hchar = board[row][column]
            else:
                if hchar == board[row][column]:
                    hcount += 1
                else:
                    hcount = 0
            if hcount == 3:
                return hchar

    for column in range(len(board)):
        vcount = 0
        vchar = ""
        for row in range(len(board)):
            if row == 0:
                vcount += 1
                vchar = board[row][column]
            else:
                if vchar == board[row][column]:
                    vcount += 1
                else:
                    vcount = 0
            if vcount == 3:
                return vchar

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != None:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != None:
        return board[0][0]

    return "Nobody"

result = has_won(board, "x", "o")
print("Result: " + str(result) + " has won!")
