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
      for row in range((N-1), -1, -1):
         if column == 0:
            rotated_matrix.append([])
            rotated_matrix[copied_row].append(matrix[row][column])
      copied_row += 1
      print(rotated_matrix)
        
   