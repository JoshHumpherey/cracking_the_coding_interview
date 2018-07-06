# Cracking the Coding Interview: 16.7
# Written by Josh Humphrey

def my_max(num1, num2):
    k = sign(num1-num2)
    q = flip(k)
    return (num1*k + num2*q)

def flip(bit):
    return 1 ^ bit

def sign(bit):
    return flip((bit >> 31) & 0x1)

res = my_max(-5, 6)
print(res)
