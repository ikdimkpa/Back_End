#!/usr/bin/python3
is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class


x = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(x, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(x, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(x, object.__name__))
