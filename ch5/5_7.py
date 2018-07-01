# Cracking the Coding Interview: 5.7
# Written by Josh Humphrey
bit_string = "1010101"

def swap_bits(bit_string):
    bit_list = list(bit_string)

    for i in range(len(bit_list)-1):
        temp = bit_list[i+1]
        bit_list[i+1] = bit_list[i]
        bit_list[i] = temp

    print(bit_list)

swap_bits(bit_string)
