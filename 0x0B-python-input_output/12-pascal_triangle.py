#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """ pascal try angle """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        tr = tri[-1]
        tmp = [1]
        for i in range(len(tr) - 1):
            tmp.append(tr[i] + tr[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
