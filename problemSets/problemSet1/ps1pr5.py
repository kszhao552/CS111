# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:00:40 2019

@author: krado
"""

def first_and_last(values):
    """Returns the first and last value of a list"""
    first = values[0]
    last = values[-1]
    return [first, last]

def longer_len(s1, s2):
    """takes two strings and returns the length of the longer one
    input: strings"""
    if (len(s1) > len(s2)):
        return len(s1)
    return len(s2)

def move_to_end(s,n):
    new = s[n:] + s[:n]
    if (n > len(s)):
        return s
    return new