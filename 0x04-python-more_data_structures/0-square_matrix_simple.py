#!/usr/bin/bash
def square_matrix_simple(matrix=[]):
    sqmat = []
    sqmat = [list(map(lambda x: x**2, m)) for m in matrix]
    return sqmat
