# Cracking the Coding Interview: 17.21
# Written by Josh Humphrey

structure = [0,0,4,0,0,6,0,0,3,0,5,0,1,0,0]

def find_water_volume(structure):
    start = 0
    end = len(structure)-1
    max_index = find_max_index(structure, start, end)
    left_volume = subsection_volume(structure, start, max_index, True)
    right_volume = subsection_volume(structure, max_index, end, False)
    return (left_volume + right_volume)

def subsection_volume(structure, start, end, is_left):
    if (start >= end):
        return 0
    sum = 0
    if is_left:
        max_index = find_max_index(structure, start, end-1)
        sum += bordered_volume(structure, max_index, end)
        sum += subsection_volume(structure, start, max_index, is_left)
    else:
        max_index = find_max_index(structure, start+1, end)
        sum += bordered_volume(structure, start, max_index)
        sum += subsection_volume(structure, max_index, end, is_left)
    return sum


def find_max_index(structure, start, end):
    max_height = structure[start]
    max_index = start
    for i in range(start, end):
        if structure[i] > max_height:
            max_height = structure[i]
            max_index = i
    return max_index

def bordered_volume(structure, start, end):
    if structure[start] < structure[end]:
        my_min = structure[start]
    else:
        my_min = structure[end]
    sum = 0
    for i in range(start+1, end):
        sum += (my_min - structure[i])
    return sum

water = find_water_volume(structure)
print("Total Water Volume: " + str(water))
