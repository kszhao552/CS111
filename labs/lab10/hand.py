#
# hand.py
#
# CS 111, Boston University
#

from card import *

class Hand:
    """ a class for objects that represent a single hand of cards """

    def __init__(self):
        """ constructor for Hand objects """
        self.cards = []

    def __repr__(self):
        """ returns a string representation of the called Hand object (self) """
        return str(self.cards)

    def add_card(self, card):
        """ add the specified Card object (card) to the list of cards
            for the called Hand object (self)
        """
        self.cards += [card]

    def num_cards(self):
        return len(self.cards)
    
    def get_value(self):
        val = 0
        for i in range(len(self.cards)):
            val += self.cards[i].get_value()
        return val
    
    def has_any(self, n):
        for i in range(len(self.cards)):
            if n == self.cards[i].rank:
                return True
        return False
        
    
class BlackjackHand(Hand):
    def get_value(self):
        val = 0
        for i in range(len(self.cards)):
            val += self.cards[i].get_value()
        if self.has_any('A'):
            val+=10
            if val > 21:
                val-=10
                
        return val