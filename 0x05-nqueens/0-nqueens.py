#!/usr/bin/python3
"""
N queens problem
"""

import sys


def isSafe(board, row, col, n):
    """
    Check if a queen can be placed on board[row][col]
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row + 1
    j = col - 1
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solveNQueens(board, col, n, solutions):
    """
    Solve the N queens problem using backtracking
    """
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    for row in range(n):
        if isSafe(board, row, col, n):
            board[row][col] = 1
            solveNQueens(board, col + 1, n, solutions)
            board[row][col] = 0


def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    solutions = []

    solveNQueens(board, 0, n, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
