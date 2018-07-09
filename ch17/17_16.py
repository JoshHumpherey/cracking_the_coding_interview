# Cracking the Coding Interview: 17.6
# Written by Josh Humphrey

def find_num_of_twos(number):
    counter = 1
    for i in range(1, number):
        clist = list(str(i))
        for c in clist:
            if c == "2":
                counter += 1
    return counter

res = find_num_of_twos(25)
print("Number of 2's: " + str(res))
