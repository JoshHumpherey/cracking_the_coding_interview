# Cracking the Coding Interview: 8.5
# Written by Josh Humphrey

def recursive_mult(num1,num2):
    base_num = num1
    depth_counter = num2
    if num2 < 1:
        return 0

    return base_num + recursive_mult(base_num, num2-1)



result = recursive_mult(5,3)
print(result)

result = recursive_mult(15,7)
print(result)
