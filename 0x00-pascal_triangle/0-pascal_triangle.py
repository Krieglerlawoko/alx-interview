#!/usr/bin/python3
"""pascal triangle funtion"""

def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list of list of int: A list of lists of integers representing Pascal's triangle.
            Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row

    for i in range(1, n):
        row = [1]  # First element in each row is always 1
        for j in range(1, i):
            # Calculate element based on the previous row
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
