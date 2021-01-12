#!/usr/bin/python3
def no_c(my_string):
    del_chr = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            del_chr += i
    return del_chr
