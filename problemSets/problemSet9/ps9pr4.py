#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """initializes the ai player with what checker they are, how they break ties, and how far they lookahead"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        super().__init__(checker)
        
    def __repr__(self):
        """prints out the ai player's atributes"""
        s = 'Player '+ self.checker
        s += ' (' + self.tiebreak +', ' + str(self.lookahead) +')'
        return s
    
    def max_score_column(self, scores):
        """determine which index has the highest number in a list"""
        m = max(scores)
        l = []
        for i in range(len(scores)):
            if scores[i] >= m:
                l += [i]
        if self.tiebreak == 'LEFT':
            col = l[0]
        elif self.tiebreak == 'RIGHT':
            col =l[-1]
        else:
            col = random.choice(l)
        return col
    
    def scores_for(self, b):
        '''determines the scores for each collumn with the amount of lookahead they have'''
        scores = [0]*7
        for i in range(len(scores)):
            if b.can_add_to(i) == False:
                scores[i] = -1
            elif b.is_win_for(self.checker):
                scores[i] = 100
            elif b.is_win_for(self.opponent_checker()):
                scores[i] = 0
            else:
                if self.lookahead ==0:
                    scores[i] =50
                else:
                    b.add_checker(self.checker, i)
                    temp_p = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                    temp_scores = temp_p.scores_for(b)
                    if max(temp_scores) == 100:
                        scores[i] = 0
                    elif max(temp_scores) == 0:
                        scores[i] = 100
                    elif max(temp_scores) == 50:
                        scores[i] = 50
                    else:
                        scores[i]= -1
                    '''win = False
                    lose = False
                    for j in temp_scores:
                        if j == 100:
                            lose = True
                            break
                        elif j == 0:
                            win = True
                    if lose:
                        scores[i] = 0
                    elif win:
                        scores[i] = 100
                    else:
                        scores[i] = 50'''
                    b.remove_checker(i)
        return scores
    
    def next_move(self, b):
        '''gives the next move that the ai player will make'''
        scores = self.scores_for(b)
        move = self.max_score_column(scores)
        self.num_moves +=1
        return move