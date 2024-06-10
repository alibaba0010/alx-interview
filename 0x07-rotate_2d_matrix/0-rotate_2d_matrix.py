#!usr/bin/python3

"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    # intialize roatated matrix
    rotated_matrix = []
    copied_row = 0
    N = len(matrix)
    for column in range(N):
        for row in range((N - 1), -1, -1):
            if column == 0:
                rotated_matrix.append([])
                rotated_matrix[copied_row].append(matrix[row][column])
        copied_row += 1

        # copy contents of matrix_copy into matrix
        # since matrix is NxN, do not need to resize matrix for rotation
    for row in range(N):
        for column in range(N):
            matrix[row][column] = rotated_matrix[row][column]
