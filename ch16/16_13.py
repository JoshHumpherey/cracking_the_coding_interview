# Cracking the Coding Interview: 16.13
# Written by Josh Humphrey

class Square():

    def __init__(self, middle, side_len):
        self.middle = middle
        self.side_len = side_len
        self.len_to_middle = side_len//2

class Line():

    def __init__(self):
        self.slope = None
        self.start = [None, None]
        self.end = [None, None]

    def calculate_slope(self, s1, s2):
        rise = s2.middle[1] - s1.middle[1]
        run = s2.middle[0] - s1.middle[0]
        self.slope = (rise/run)


s1 = Square([1,1], 3)
s2 = Square([10,5], 3)
line = Line()
line.calculate_slope(s1 ,s2)
