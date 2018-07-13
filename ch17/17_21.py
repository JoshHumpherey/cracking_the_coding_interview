# Cracking the Coding Interview: 17.21
# Written by Josh Humphrey

structure = [0,0,4,0,0,6,0,0,3,0,5,0,1,0,0]

def find_water_volume(structure):
    original = []
    for i in range(len(structure)-1):
        temp = find_valley(structure, i+1, structure[i])
        original = temp
    print(original)


def find_valley(structure, index, target_height):


water = find_water_volume(structure)
print("Total Water Volume: " + str(water))
