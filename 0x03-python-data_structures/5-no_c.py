#!/usr/bin/python3

def no_c(my_string):
    updated_str = ''
    for n in my_string:
        if n != 'c' and n != 'C':
            updated_str += n
    return (updated_str)
