#!/usr/bin/python3
"""Module for calculating the perimeter of an island in a grid.

This module defines a function to compute the perimeter of an island 
represented in a 2D grid. The grid is composed of 1s (land) and 0s (water). 
The island is surrounded by water, and there are no lakes within the island.
"""

from typing import List

def island_perimeter(grid: List[List[int]]) -> int:
    """Calculate the perimeter of the island in a grid.

    Args:
        grid (List[List[int]]): A 2D list where 1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Add to perimeter for each edge that is either on the boundary or adjacent to water
                perimeter += (i == 0 or grid[i - 1][j] == 0)  # Top edge
                perimeter += (i == rows - 1 or grid[i + 1][j] == 0)  # Bottom edge
                perimeter += (j == 0 or grid[i][j - 1] == 0)  # Left edge
                perimeter += (j == cols - 1 or grid[i][j + 1] == 0)  # Right edge

    return perimeter
