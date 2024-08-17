#!/usr/bin/python3
"""Exercise 0"""


def rotate_2d_matrix(matrix):
    """Rotate the matrix."""
    length = len(matrix)
    for i in range(length):
        for j in range(i):
            a = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = a
    for i in range(length):
        for j in range(length // 2):
            a = matrix[i][j]
            matrix[i][j] = matrix[i][length - 1 - j]
            matrix[i][length - 1 - j] = a
