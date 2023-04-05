#!/usr/bin/python3
"""
This module contains a program that solves the N queens problem.
"""

import sys


def print_board(board):
    """
    Print the board in a specific format.
    """
    for row in board:
        print("[", end="")
        for i, col in enumerate(row):
            if col == 1:
                print("{}{}".format(i, "" if i == len(row) - 1 else ", "), end="")
        print("]")


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, col):
    """
    Solve the N queens problem using backtracking.
    """
    # Base case: all queens are placed
    if col == len(board):
        print_board(board)
        return True
    # Recursive case: try to place a queen in each row of this column
    for row in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve(board, col + 1)
            board[row][col] = 0
    return False


if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    # Solve the N queens problem
    board = [[0 for j in range(N)] for i in range(N)]
    solve(board, 0)
