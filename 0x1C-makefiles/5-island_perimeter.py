#!/usr/bin/python3


def island_perimeter(grid):
    """ Function that returns detail of a grid
    """

    if not isinstance(grid, list) or not len(grid):
        return 0
    y = len(grid) - 1
    x = len(grid[0]) - 1

    prim = 0

    for i in range(y):
        for j in range(x):
            if grid[i][j] == 1:
                prim += check_surround(grid, i, j)
    return prim


def check_surround(grid, row, idx):
    """ Function that checks the surroundings of a given tile
    """
    height = len(grid)
    length = len(grid[0])
    sur = [0, 0, 0, 0]

    if row - 1 >= 0:  # up
        if not grid[row - 1][idx]:
            sur[0] = 1

    if row + 1 < height:  # down
        if not grid[row + 1][idx]:
            sur[1] = 1

    if idx - 1 >= 0:  # left
        if not grid[row][idx - 1]:
            sur[2] = 1

    if idx + 1 < length:  # right
        if not grid[row][idx + 1]:
            sur[3] = 1

    return sum(sur)
