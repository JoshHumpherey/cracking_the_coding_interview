# Cracking the Coding Interview: 5.4
# Written by Josh Humphrey

def get_next_nums(decimal_num):
    bin_num = bin(decimal_num)
    bin_list = list(bin_num)
    target = find_ones_amount(bin_list)
    temp = decimal_num + 1
    while(True):
        if target == find_ones_amount(bin(temp)):
            print("Larger: " + str(temp))
            break
        else:
            temp += 1

    temp = decimal_num-1
    while(temp > 0):
        if target == find_ones_amount(bin(temp)):
            print("Smaller: " + str(temp))
            break
        else:
            temp -= 1
    return

def find_ones_amount(bin_list):
    number_of_ones = 0
    for bit in bin_list:
        if bit == "1":
            number_of_ones += 1
    return number_of_ones


get_next_nums(4)
