#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    cp_mylist = my_list[:]
    i = 0
    while i < len(cp_mylist):
        if cp_mylist[i] % 2 == 0:
            cp_mylist[i] = True
        else:
            cp_mylist[i] = False
        i += 1
    return cp_mylist
