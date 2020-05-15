# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:00:15 2019

@author: krado
"""

#ps3pr4
#algorithm design problems

def index(elem, seq):
    """returns the index of an element in a string or list
    input: a character and a string or any value and a list"""
    if (seq==''):
        return -1
    elif (seq ==[]):
        return -1
    else:
        rest=index(elem,seq[1:])
        if (elem == seq[0]):
            return 0
        elif (rest<0):
            return rest
        else:
            return rest+1
            
def index_last(elem, seq):
    """returns the last occurence of an index of an element in a string or list
    input: a character and a string or any value and a list"""
    if (seq==''):
        return -1
    elif (seq ==[]):
        return -1
    else:
        rest=index_last(elem,seq[:-1])
        if (elem == seq[-1]):
            return len(seq)-1
        else:
            return rest
        
def jscore(s1, s2):
    """returns the jotto score of the two words, s1 compared to s2
    input: two strings"""
    if (s1=='' or s2==''):
        return 0
    else:
        if (s1[0] in s2):
            rest_score = jscore(s1[1:], rem_first(s1[0], s2))
            return rest_score+1
        else:
            rest_score = jscore(s1[1:], s2)
            return rest_score
        

def rem_first(elem, values):
    """ removes the first occurrence of elem from the list values
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        result_rest = rem_first(elem, values[1:])
        return values[0] + result_rest