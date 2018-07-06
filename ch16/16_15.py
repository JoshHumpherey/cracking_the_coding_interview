# Cracking the Coding Interview: 16.15
# Written by Josh Humphrey
guess  = "YRGB"
actual = "RGGB"

def get_mastermind_hits(guess, actual):
    if len(guess) != 4 or len(actual) != 4:
        return None
    hitmap = dict()

    guess_list = list(guess)
    actual_list = list(actual)
    hits = 0
    for i in range(len(guess_list)):
        if guess_list[i] == actual_list[i]:
            hits += 1
    print("Number of hits: " + str(hits))
    pseudo_hits = 0
    for color in guess_list:
        if color in actual_list:
            pseudo_hits += 1
            actual_list.remove(color)
    pseudo_hits = pseudo_hits-hits
    print("Number of pseudo-hits: " + str(pseudo_hits))

get_mastermind_hits(guess,actual)
