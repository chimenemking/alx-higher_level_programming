#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_divisible_ls = [numb % 2 == 0 for numb in my_list]
    return new_divisible_ls
