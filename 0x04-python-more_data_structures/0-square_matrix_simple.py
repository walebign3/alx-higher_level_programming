#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = matrix.copy()
    return ([[y**2 for y in x] for x in matrix2])
