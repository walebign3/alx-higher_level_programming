#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        result = " ".join(map(str, row))
        print("{}".format(result))
