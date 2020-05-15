# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 16:03:17 2019

@author: krado
"""

#ps4pr2

from ps4pr1 import *

def add(b1, b2):
    """takes two binary numbers and returns the sum of the numbers in binary
    input: two strings consisting of 1's and 0's"""
    n1=bin_to_dec(b1)
    n2 = bin_to_dec(b2)
    b_sum = dec_to_bin(n1+n2)
    return b_sum

def increment(b1):
    """increments a binary number by 1, goes to 00000000 if overflown
    input: string consisting of 1's and 0's and has a length of 0 or less"""
    if (b1=='11111111'):
        return '00000000'
    else:
        num = bin_to_dec(b1)
        num = num+1
        b_new = dec_to_bin(num)
        return '0'*(8-len(b_new))+b_new