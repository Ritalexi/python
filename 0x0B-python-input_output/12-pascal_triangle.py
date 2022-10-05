#!/usr/bin/python3
"""
Module for pascal_triangle method.
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
        Args:
            n (int): number of lists and digits
        Returns: list of lists
    """

    if n <= 0:
        return ([""])
    ans = [[0 for j in range(i + 1)] for i in range(n)]
    for i in range(5):
        for j in range(i + 1):
            if j == 0:
                ans[i][j] = 1
            elif j == i:
                ans[i][j] = 1
            else:
                ans[i][j] = ans[i -1][j] + ans[i - 1][j - 1]
    return ans
