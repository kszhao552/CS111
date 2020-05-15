#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b


def process_move(p,b):
     '''processs which move is being made at the time'''
     print(str(p) + '\'s turn')
     col = p.next_move(b)
     print(col)
     b.add_checker(p.checker, col)
     print()
     print(b)
     if b.is_win_for(p.checker):
         print(p, 'wins in', p.num_moves, 'moves.')
         print('Congratulations!')
         return True
     elif b.is_full():
         print('It\'s a tie!')
         return True
     else:
         return False
        
        
class RandomPlayer(Player):
    def next_move(self, b):
        '''randomly chooses a collumn that can be played in'''
        options = [x for x in range(b.width) if b.can_add_to(x)]
        move = random.choice(options)
        self.num_moves += 1
        return move