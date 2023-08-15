#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for val in my_string:
        if val != "c" and val != "C":
            new_str += val
    return new_str
