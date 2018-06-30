# Cracking the Coding Interview: 5.3
# Written by Josh Humphrey
bit_string = "11011101111"

def flip_to_win(bit_string):
    bit_streak = 0
    for i in range(len(bit_string)):
        temp_streak = 0
        temp_list = list(bit_string)
        if temp_list[i] == "0":
            temp_list[i] = "1"
            for j in range(len(temp_list)):
                if temp_list[j] == "1":
                    temp_streak += 1
                    if j == len(temp_list)-1 and bit_streak < temp_streak:
                        bit_streak = temp_streak
                        temp_streak = 0
                else:
                    if bit_streak < temp_streak:
                        bit_streak = temp_streak
                    temp_streak = 0

    return bit_streak


test = flip_to_win(bit_string)
print(test)
