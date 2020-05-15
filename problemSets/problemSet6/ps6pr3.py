# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 17:09:17 2019

@author: krado
"""
#problem set 6 problem 3
#
#Functions with loops

def double(s):
    """takes an arbitrary string and constructs a new string 
    with each character being doubled"""
    new_string =''
    for l in range(len(s)):
        new_string += s[l]*2
    return new_string


def weave(s1, s2):
    """takes two arbitrary strings and weaves them together"""
    result = ''
    len_shorter = min(len(s1), len(s2))
    for i in range(len_shorter):
        result += s1[i]+s2[i]
    if (len(s1)>len(s2)):
        result += s1[len_shorter:]
    else:
        result += s2[len_shorter:]
    return result

def index(elem, seq):
    """uses a loop to find first occurance of the element in the sequence"""
    for i in range(len(seq)):
        if seq[i]==elem:
            return i
    return -1