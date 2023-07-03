#!/usr/bin/python

"""A function that generates a Pascal triangle"""


def pascal_triangle(n):
    pascalt = []

    if n > 0:
        for i in range(n):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    value = pascalt[i - 1][j - 1] + pascalt[i - 1][j]
                    row.append(value)
            pascalt.append(row)
    return pascalt
