#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
# Computer Science 111  
#

# IMPORTANT: this file is for your solutions to Problem 3.
# Your solutions to Problem 2 should go in ps7pr2.py instead.

from ps7pr2 import *
from gol_graphics import *
import random

def count_neighbors(cellr, cellc, grid):
    """takes a position in a 2d list and returns how many of its 'neighbors' are 1's
    input: cellr, and cellc are integers that are within the dimensions of grid and grid is a 2d list"""
    count=0
    
    for x in range(cellr-1, cellr+2):
        for y in range(cellc-1, cellc+2):
            if grid[x][y] == 1:
                count+=1
    if grid[cellr][cellc]==1:
        count-=1
    return count

def next_gen(grid):
    """creates a new grid that is next generation based off the rules in the game of life
    input: grid is a 2d list that is comprised of 0's and 1's"""
    new_grid = copy(grid)
    count = 0
    for x in range(1, len(grid)-1):
        for y in range (1, len(grid[0])-1):
            count = count_neighbors(x, y, grid)
            
            if count <2:
                new_grid[x][y] = 0
            elif count ==3:
                new_grid[x][y] = 1
            elif count > 3:
                new_grid[x][y] = 0
                
    return new_grid