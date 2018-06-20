# Cracking the Coding Interview: 1.8
# Written by Josh Humphrey

def is_rotation(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 != l2:
        return False
    else:
        double_s1 = s1 + s1
        return isSubstring(double_s1, s2)
        
