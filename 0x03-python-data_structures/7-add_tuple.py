#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
     if len(tuple_a) >= 1:
        x1 = tuple_a[0]
    else:
        x1 = 0
    if len(tuple_a) >= 2:
        x2 = tuple_a[1]
    else:
        x2 = 0

    if len(tuple_b) >= 1:
        y1 = tuple_b[0]
    else:
        y1 = 0
    if len(tuple_b) >= 2:
        y2 = tuple_b[1]
    else:
        y2 = 0

    return x1 + y1, x2 + y2
