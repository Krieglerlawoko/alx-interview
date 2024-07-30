#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of an island described in a grid.
    
    grid: A list of lists of integers where:
        0 represents water
        1 represents land
    
    Returns the perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with a perimeter of 4 for each land cell
                cell_perimeter = 4
                
                # Check the top cell
                if i > 0 and grid[i - 1][j] == 1:
                    cell_perimeter -= 1
                
                # Check the bottom cell
                if i < rows - 1 and grid[i + 1][j] == 1:
                    cell_perimeter -= 1
                
                # Check the left cell
                if j > 0 and grid[i][j - 1] == 1:
                    cell_perimeter -= 1
                
                # Check the right cell
                if j < cols - 1 and grid[i][j + 1] == 1:
                    cell_perimeter -= 1
                
                perimeter += cell_perimeter
    
    return perimeter
