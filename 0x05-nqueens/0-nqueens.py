#!/usr/bin/python3
"""
Module for N queens solution finder.
"""
import sys


def get_input():
    """
    Retrieve and validate the program's argument.
    Returns:
        int: Chessboard size.
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
    return n


def is_attacking(pos0, pos1):
    """
    Check whether the positions of two queens are in an attacking mode.
    Args:
        pos0 (list or tuple): 1st queen's position.
        pos1 (list or tuple): 2nd queen's position.
    Returns:
        bool: True if the queens are in an attacking position, else False.
    """
    if pos0[0] == pos1[0] or pos0[1] == pos1[1]:
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def group_exists(group, solutions, n):
    """
    Check whether a group exists in the list of solutions.
    Args:
        group (list of integers): Group of possible positions.
        solutions (list): List of all possible solutions.
        n (int): Chessboard size.
    Returns:
        bool: True if the group exists in the solutions, else False.
    """
    for sol in solutions:
        if all(any(pos0 == pos1 for pos1 in sol) for pos0 in group):
            return True
    return False


def build_solution(row, group, pos, solutions, n):
    """
    Build a solution for the N queens problem.
    Args:
        row (int): Current row in the chessboard.
        group (list of lists of integers): Group of valid positions.
        pos (list): List of possible positions on the chessboard.
        solutions (list): List of all possible solutions.
        n (int): Chessboard size.
    """
    if row == n:
        if not group_exists(group, solutions, n):
            solutions.append(group.copy())
    else:
        for col in range(n):
            index = row * n + col
            if not any(is_attacking(pos[index], grp_pos) for grp_pos in group):
                group.append(pos[index])
                build_solution(row + 1, group, pos, solutions, n)
                group.pop()


def get_solutions(n):
    """
    Get solutions for the given chessboard size.
    Args:
        n (int): Chessboard size.
    Returns:
        list: List of all possible solutions.
    """
    pos = [[i // n, i % n] for i in range(n ** 2)]
    solutions = []
    build_solution(0, [], pos, solutions, n)
    return solutions


def main():
    """
    Main function to run the N queens solution finder.
    """
    n = get_input()
    solutions = get_solutions(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
