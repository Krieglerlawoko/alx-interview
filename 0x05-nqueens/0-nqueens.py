#!/usr/bin/python3
"""
Solution to the N-Queens problem.
"""
import sys


def backtrack(row, n, cols, pos_diags, neg_diags, board):
    """
    Backtrack function to find solutions to the N-Queens problem.
    Args:
        row (int): Current row in the board.
        n (int): Size of the board (n x n).
        cols (set): Columns where queens are placed.
        pos_diags (set): Positive diagonals where queens are placed.
        neg_diags (set): Negative diagonals where queens are placed.
        board (list): 2D list representing the board.
    """
    if row == n:
        result = []
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 1:
                    result.append([r, c])
        print(result)
        return

    for col in range(n):
        if col in cols or (row + col) in pos_diags or (row - col) in neg_diags:
            continue

        cols.add(col)
        pos_diags.add(row + col)
        neg_diags.add(row - col)
        board[row][col] = 1
        backtrack(row + 1, n, cols, pos_diags, neg_diags, board)
        cols.remove(col)
        pos_diags.remove(row + col)
        neg_diags.remove(row - col)
        board[row][col] = 0


def nqueens(n):
    """
    Solves the N-Queens problem and prints all solutions.
    Args:
        n (int): Number of queens. Must be >= 4.
    """
    cols = set()
    pos_diags = set()
    neg_diags = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diags, neg_diags, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
