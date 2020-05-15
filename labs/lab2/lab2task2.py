# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 15:36:13 2019

@author: krado
"""

def mysum(x, y):
    """ takes two numbers and returns their sum """
    total = x + y
    return total

def sum_double(x, y):
    """takes two numbers and gets their sum and doubles it if the numbers are the same"""
    if (x==y):
        return 2 *(x+y)
    return (x+y)