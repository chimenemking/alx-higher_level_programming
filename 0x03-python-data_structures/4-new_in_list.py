#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if not my_list or idx < 0 or idx >= len(my_list):
        return my_list.copy()

    newly_done_list = my_list.copy()
    newly_done_list[idx] = element

    return newly_done_list
