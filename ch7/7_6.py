# Cracking the Coding Interview: 7.6
# Written by Josh Humphrey

# Assume a 5x5 Jigsaw Puzzle -- 25 pieces
# Piece Types: Inner, Outer, Corner
class Puzzle():

    def __init__(self, length, area):
        self.length = length
        self.area = area


    class Piece():

        def __init__(self, fits_with, edge_amount, type):
            self.fits_with = fits_with
            self.edge_amount = edge_amount
            self.type = type

my_puzzle = Puzzle(5,25)
