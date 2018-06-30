# Cracking the Coding Interview: 5.2
# Written by Josh Humphrey


def num_to_binary(decimal_num):
    fraction_amt = float(0.5)
    counter = 0
    output = [0] * 32
    while decimal_num > 0:
        if counter > 31:
            print("ERROR")
            return
        if decimal_num < fraction_amt:
            output[counter] = 0
        else:
            output[counter] = 1
            decimal_num -= fraction_amt

        fraction_amt /= 2
        counter += 1

    result = ''.join(str(output))
    print(result)

num_to_binary(0.5)
num_to_binary(0.75)
num_to_binary(0.666666)
