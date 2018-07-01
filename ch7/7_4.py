# Cracking the Coding Interview: 7.4
# Written by Josh Humphrey

class Parking_Lot():

    def __init__(self):
        self.floors = []

    class Floor():

        def __init__(self, capacity, level):
            self.capacity = capacity
            self.level = level

my_lot = Parking_Lot()
floor1 = my_lot.Floor(100,1)
floor2 = my_lot.Floor(100,2)
floor3 = my_lot.Floor(100,3)
my_lot.floors.append(floor1)
my_lot.floors.append(floor1)
my_lot.floors.append(floor1)
