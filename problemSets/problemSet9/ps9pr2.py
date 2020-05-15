#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below

class Player(Board):
    def __init__(self, checker):
        """initializes the player with the given checker and 0 moves"""
        assert(checker =='X' or checker =='O')
        self.checker = checker
        self.num_moves = 0
        
    def __repr__(self):
        """returns the text with the player and their checker"""
        text = 'Player '+ self.checker
        return text
    
    def opponent_checker(self):
        """returns text with the opposing player and their checker"""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'
        
    def next_move(self, b):
        """returns the col that the user whats to move into next
        checks to see if they can before adding it"""
        while True:
            col = int(input("Enter a column: "))
            if b.can_add_to(col):
                break
            else:
                print('Try again!')
        self.num_moves += 1
        return col