#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cp_matrix = []
    for i in matrix:
        cp_matrix.append(list(map((lambda x: x * x), i)))
    return cp_matrix
