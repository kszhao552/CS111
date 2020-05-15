# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:47:56 2019

@author: krado
"""

def copy(s, n):
    """cops a given string by a given input amount of times
    input: string followed by int"""
    if (n<=0):
        return ''
    else:
        curs = copy(s,n-1)
        return curs + s
    
def compare(list1, list2):
    """returns the number of index in which list 1 elements are smaller than the list 2 element at the same index
    input: two lists"""
    if (len(list1) == 0 or len(list2)==0):
        return 0
    else:
        num = compare(list1[1:], list2[1:])
        if (list1[0]<list2[0]):
            return num + 1
        return num
        
def double(s):
    """doubles each character within a string
    input: string"""
    if (s == ""):
        return s
    else:
        rest_string = double(s[1:])
        return s[0]*2 + rest_string
    
