# Cracking the Coding Interview: 5.6
# Written by Josh Humphrey

def bits_to_flip(num1, num2):
    bin1 = list("{0:#032b}".format(num1))
    bin2 = list("{0:#032b}".format(num2))
    flip_count = 0
    for i in range(len(bin1)):
        if bin1[i] != bin2[i]:
            flip_count += 1
    return flip_count

result = bits_to_flip(29,15)
print(result)
