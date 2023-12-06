#!/usr/bin/python3
""" Recreating the pascal's triangle, but with code, let's have fun """


def pascal_triangle(n):
    """ Function that returns the computed pascal triangle """
    if n <= 0:
        return []
    outer = []
    first_list = [1]
    outer.append(first_list)
    for i in range(n - 1):
        inner = []
        previous_list = outer[-1]
        inner.append(1)
        for x in range(len(previous_list) - 1):
            next = previous_list[x] + previous_list[x + 1]
            inner.append(next)
        inner.append(1)
        outer.append(inner)
    return outer
