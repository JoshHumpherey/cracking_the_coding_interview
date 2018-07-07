# Cracking the Coding Interview: 16.22
# Written by Josh Humphrey

import random

def rand5():
    return random.randint(0,4)

def rand7():
    while(True):
        num = 5 * rand5() + rand5()
        if (num < 21):
            return num % 7

def simulate_rand7(number):
    hashmap = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}
    for i in range(number):
        key = rand7()
        hashmap[key] += 1
    return hashmap

sim_result = simulate_rand7(100000)
print(sim_result)
