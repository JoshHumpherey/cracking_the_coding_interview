# Cracking the Coding Interview: 16.8
# Written by Josh Humphrey

map_1s = {0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
map_10s = {0:"",1:"ten",2:"twenty",3:"thirty",4:"fourty",5:"fifty",6:"sixty",7:"sevnty",8:"eighty",9:"ninety"}
map_100s = {0:"",1:"one hundred",2:"two hundred",3:"three hundred",4:"four hundred",5:"five hundred",6:"six hundred",7:"seven hundred",8:"eight hundred",9:"nine hundred"}
map_1000s = {0:"",1:"one thousand",2:"two thousand",3:"three thousand",4:"four thousand",5:"five thousand",6:"six thousand",7:"seven thousand",8:"eight thousand",9:"nine thousand"}

def num_to_text(number):
    output_arr = []
    number_list = list(str(number))
    number_list.reverse()
    if len(number_list) != 4:
        print("ERROR: Number wrong length")
        return

    for i in range(len(number_list)):
        number_list[i] = int(number_list[i])

    for i in range(len(number_list)):
        key = number_list[i]
        if i == 0:
            output_arr.append(map_1s[key])
        if i == 1:
            output_arr.append(map_10s[key])
        if i == 2:
            output_arr.append(map_100s[key])
        if i == 3:
            output_arr.append(map_1000s[key])
    output_arr.reverse()
    output_string = ""
    print(output_arr)
    for phrase in output_arr:
        if phrase != '':
            output_string += (" " + phrase)
    print(output_string)

num_to_text(2018)
