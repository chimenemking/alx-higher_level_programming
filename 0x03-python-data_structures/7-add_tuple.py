#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    x1, x2 = tuple_a[:2]
    y1, y2 = tuple_b[:2]
    return x1 + y1, x2 + y2
