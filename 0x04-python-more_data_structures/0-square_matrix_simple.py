#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    ans = []
    for i in new_matrix:
        ans.append(list(map((lambda x: x ** 2), i)))
    return ans
