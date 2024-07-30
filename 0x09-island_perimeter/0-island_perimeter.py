#!/usr/bin/python3
"""Module for calculating the perimeter of an island in a grid.

This module defines a function to compute the perimeter of an island 
represented in a 2D grid. The grid is composed of 1s (land) and 0s (water). 
The island is surrounded by water, and there are no lakes within the island.
"""


def island_perimeter(grid):
    """Calculate the perimeter of the island in a grid.

    Args:
        grid (List[List[int]]): A 2D list where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    # Determine the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Initialize the perimeter variable to 0
    perimeter = 0

    # Loop through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the top edge
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the bottom edge
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the left edge
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the right edge
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    # Return the total perimeter
    return perimeter
