#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, solutions):
    """Utilize backtracking to solve the N Queens problem"""
    if col == len(board):
        solutions.append([[i, board[i].index(1)] for i in range(len(board))])
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0


def solve_nqueens(n):
    """Solve the N Queens problem and print all solutions"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    for solution in solutions:
        print(solution)
