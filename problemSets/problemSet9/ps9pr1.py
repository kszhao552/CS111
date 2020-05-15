# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:35:34 2019

@author: krado
"""

class Board:
    
    def __init__(self, height, width):
        """initializes a board with a given width and height"""
        self.width = width
        self.height = height
        self.slots = []
        for rows in range(height):
            row = [' '] * width     # a row containing width 0s
            self.slots += [row]
            
    def __repr__(self):
        """ Returns a string representation for a Board object.
        """
        s = ''         # begin with an empty string
        
        # add one row of slots at a time
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row
            
            for col in range(self.width):
                s += self.slots[row][col] + '|'
                
            s += '\n'  # newline at the end of the row
            
        s += '-' * (2*self.width +1)
        s+='\n'
        s+= ' '
        for i in range(0, self.width):
            s += str(i%10) + ' '
            
        return s
    
    def add_checker(self, checker, col):
        """adds the given checker to the inputed collumn at the first available row"""
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        row = self.height -1
        while True:
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break
            else:
                row-=1
                
    def reset(self):
        """resets the board completely"""
        for rows in range(self.height):
            for col in range(self.width):
                self.slots[rows][col] = ' '
            
    def add_checkers(self, colunms):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colunms:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
                
    def can_add_to(self, col):
        """checks to see if a checker can be addes to the inputed collumn"""
        if col < 0 or col >= self.width:
            return False
        else :
            for r in range(self.height):
                if self.slots[r][col] == ' ':
                    return True
            return False
        
    def is_full(self):
        """Checks to see if there are any availalbe places to put a checker"""
        for i in range(self.width):
            if self.can_add_to(i) == True:
                return False
        return True
    
    def remove_checker(self, col):
        """removes the top checker from a collumn"""
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                self.slots[r][col] = ' '
                break
            
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                    return True
                
        # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker):
        """checks for a vertical win for the specified checker"""
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                self.slots[row+1][col] == checker and \
                self.slots[row+2][col] == checker and \
                self.slots[row+3][col] == checker:
                    return True
        return False
    
    def is_down_diagonal_win(self, checker):
        """checks for a down diagonal win for the specified checker"""
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                self.slots[row+1][col+1] == checker and \
                self.slots[row+2][col+2] == checker and \
                self.slots[row+3][col+3] == checker:
                    return True
        return False
    
    def is_up_diagonal_win(self, checker):
        """checks for a up diagonal win for the specified checker"""
        for row in range(3, self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                self.slots[row-1][col+1] == checker and \
                self.slots[row-2][col+2] == checker and \
                self.slots[row-3][col+3] == checker:
                    return True
        return False
    
    def is_win_for(self, checker):
        """checks to see if the specified checker has won"""
        assert(checker == 'X' or checker == 'O')
        if self.is_vertical_win(checker) or\
        self.is_down_diagonal_win(checker) or\
        self.is_up_diagonal_win(checker) or\
        self.is_horizontal_win(checker):
            return True
        return False