# 0x08. Rotate 2D Matrix

## Description

This project contains a function that rotates a square matrix 90 degrees clockwise in place.

## Requirements

- Python 3.4 or higher
- PEP8 style

## Usage

The function is defined as follows:

```python
def rotate_2d_matrix(matrix):
    # rotate the matrix in place
```

The parameter `matrix` is a list of lists representing a square matrix. The function does not return anything, but modifies the matrix in place.

For example:

```python
>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> rotate_2d_matrix(matrix)
>>> matrix
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```

## Algorithm

The algorithm is based on the following steps:

1. Transpose the matrix, which means swapping the rows and columns. This can be done by looping over the matrix and swapping the elements at (i, j) and (j, i) for all i and j.
2. Reverse each row of the transposed matrix, which means swapping the elements at (i, j) and (i, n - 1 - j) for all i and j, where n is the size of the matrix. This can be done by looping over the matrix and using a temporary variable to swap the elements.

## Complexity

The time complexity of the algorithm is O(n^2), where n is the size of the matrix. This is because we need to loop over all the elements of the matrix twice.

The space complexity of the algorithm is O(1), because we do not use any extra space to store or manipulate the matrix elements. We only use a temporary variable to swap the elements in place.
