# Cracking the Coding Interview: 16.3
# Written by Josh Humphrey

start1 = [1,1]
start2 = [3,5]
end1 = [3,8]
end2 = [1, 9]

def do_lines_intersect(start1, start2, end1, end2):
    x = 0
    y = 1
    rise1 = (end1[y]-start1[y])
    run1 = (end1[x]-start1[x])
    slope1 = (rise1/run1)
    rise2 = (end2[y]-start2[y])
    run2 = (end2[x]-start2[x])
    slope2 = (rise2/run2)
    if slope1 == slope2:
        print("ERROR: The lines do not intersect")
        return
    print(slope1)
    print(slope2)


do_lines_intersect(start1, start2, end1, end2)
