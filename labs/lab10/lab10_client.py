#
# lab10_client.py
#
# CS 111, Boston University
#

from card import *
from hand import *

c1 = Card(7, 'Hearts')
c2 = Card('Ace', 'Diamonds')

h1 = Hand()
h1.add_card(c1)
h1.add_card(c2)
print('first hand: ', h1)
print('number of cards:', h1.num_cards())
print('total value:', h1.get_value())
print('has at least one 7:', h1.has_any(7))
print('has at least one Ace:', h1.has_any('A'))
print('has at least one Queen:', h1.has_any('Q'))

print()
h2 = BlackjackHand()
h2.add_card(c1)
h2.add_card(c2)
print('second hand:', h2)
print('number of cards:', h2.num_cards())
print('total value:', h2.get_value())
print() 
print('adding a card to h2...')
c3 = Card(4, 'C')
h2.add_card(c3)
print('updated second hand:', h2)
print('number of cards:', h2.num_cards())
print('total value:', h2.get_value())