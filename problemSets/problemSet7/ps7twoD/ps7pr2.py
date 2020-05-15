#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# 2-D Lists
#
# Computer Science 111
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
# 

# IMPORTANT: This file is for your solutions to Problem 2.
# Your solutions to problem 3 should go in ps7pr3.py instead.

import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line

def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid

def inner_grid(height, width):
    """creates and returns a height x width grid in which the cells on the 
    outside are set to 0 and all other cells are 0.
    inputs: height and width are non-negative integers"""
    grid = create_grid(height, width)
    for x in range(1, height-1):
        for y in range (1, width-1):
                grid[x][y] = 1
                
    return grid

def random_grid(height, width):
    """creates and returns a height x width grid in which the cells in the 
    grid are randomly assigned a value of 1 or 0
    inputs: height and width are both non-negative integers"""
    grid = create_grid(height, width)
    
    for x in range(height):
       for y in range(width):
           grid[x][y] = random.choice([0,1])
           
    return grid

def copy(grid):
    """copys and returns a grid with the same dimensions and ibnternals as the orignal grid
    input: grid is a 2d list"""
    new_grid = create_grid(len(grid), len(grid[0]))
    
    for x in range(len(new_grid)):
      for y in range(len(new_grid[0])):
          new_grid[x][y] = grid[x][y]
          
    return new_grid
    
          

def invert(grid):
    """takes a returns a grid with all 1s being turned to 0s and vice versa
    input: grid is a 2d list comprised of 1's and 0's"""
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] ==0:
                grid[x][y] =1
            else:
                grid[x][y]=0
    