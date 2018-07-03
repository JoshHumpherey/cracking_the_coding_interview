# Cracking the Coding Interview: 8.11
# Written by Josh Humphrey
coins = [25, 10, 5, 1]

def calculate_coin_perms(amount, coins, index):
    if (index >= len(coins)-1):
        return 1 # smallest denom amount
    coin_amount = coins[index]
    ways = 0
    i = 0
    while(i*coin_amount <= amount):
        remaining_total = amount - (i*coin_amount)
        ways += calculate_coin_perms(remaining_total,coins,index+1)
        i += 1
    return ways

result = calculate_coin_perms(25,coins,0)
print(result)
