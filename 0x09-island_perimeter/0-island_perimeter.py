#!/usr/bin/python3
"""
Returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    # Initialize the perimeter to zero
    perimeter = 0

    for i in range(len(grid)):
        # Loop through the columns of the grid
        for j in range(len(grid[i])):
            # If the cell is land
            if grid[i][j] == 1:
                # Check the four adjacent cells
                # If the cell is on the top edge or the cell above is water
                if i == 0 or grid[i - 1][j] == 0:
                    # Add one to the perimeter
                    perimeter += 1
                # If the cell is on the bottom edge or the cell below is water
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    # Add one to the perimeter
                    perimeter += 1
                # If the cell is on the left edge or the cell to the left is
                # water
                if j == 0 or grid[i][j - 1] == 0:
                    # Add one to the perimeter
                    perimeter += 1
                # If the cell is on the right edge or the cell to the right is
                # water
                if j == len(grid[i]) - 1 or grid[i][j + 1] == 0:
                    # Add one to the perimeter
                    perimeter += 1

    # Return the perimeter
    return perimeter
