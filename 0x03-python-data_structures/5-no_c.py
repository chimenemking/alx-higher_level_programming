#!/usr/bin/python3

def no_c(my_string):
    newer_strng = ""
    for v in range(len(my_string)):
        if my_string[v] != 'c' and my_string[v] != 'C':
            newer_strng += my_string[v]
    return newer_strng
