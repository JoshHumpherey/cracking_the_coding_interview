# Cracking the Coding Interview: 8.1
# Written by Josh Humphrey

def routes_up_stairs(step_num):
    dynamic = dict()
    dynamic[1] = 1
    dynamic[2] = 2
    dynamic[3] = 3

    if step_num <= 3:
        print(dynamic[step_num])
        return

    count = 4
    while count != step_num + 1:
        dynamic[count] = dynamic[count-1] + dynamic[count-2] + dynamic[count-3]
        count += 1

    print(dynamic[step_num])
    return

routes_up_stairs(10)
