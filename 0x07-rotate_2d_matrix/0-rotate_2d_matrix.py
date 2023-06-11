#!/usr/bin/env python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """
    Rotate a matrix by 90 degrees clockwise,
    """
    matrix_len = len(matrix)
    for i in range( matrix_len):
        for j in range(i + 1, matrix_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_len):
        for j in range(matrix_len // 2):
            matrix[i][j], matrix[i][matrix_len-1-j] = matrix[i][matrix_len-1-j], matrix[i][j]
    
    return matrix