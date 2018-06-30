# Cracking the Coding Interview: 5.1
# Written by Josh Humphrey

N = 10000000000
M = 10011
i = 2
j = 6

def insert_number(N,M,i,j):
    N_list = list(str(N))
    N_list.reverse()
    M_list = list(str(M))
    M_list.reverse()
    N_list[i:j] = M_list
    N_list.reverse()
    result = ''.join(N_list)
    print(result)

insert_number(N,M,i,j)
