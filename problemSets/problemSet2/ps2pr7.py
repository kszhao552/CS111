# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:07:33 2019

@author: krado
"""

def letter_score(letter):
    """returns the score of a letter based off the game scrabble
    input: string"""
    assert(len(letter) == 1)
    if letter in 'aeilnorstu':
        return 1
    elif letter in 'dg':
        return 2
    elif letter in 'bcmp':
        return 3
    elif letter in 'fhvwy':
        return 4
    elif letter in 'k':
        return 5
    elif letter in 'jx':
        return 8
    elif letter in 'qz':
        return 10
    else:
        return 0
    
def scrabble_score(word):
    """returns the score of a word in terms of points for scrabble
    input: string"""
    if (len(word)==0):
        return 0
    else:
        rest_score = scrabble_score(word[1:])
        return letter_score(word[0])+rest_score
    
def add(vals1, vals2):
    """returns the addition of each element within a new list
    input: two list containing any numbers"""
    if len(vals1) ==0:
        return vals1+vals2
    else:
        rest_list = add(vals1[1:], vals2[1:])
        return [vals1[0]+vals2[0]]+ rest_list
    
def weave(s1, s2):
    """returns a new string that goes in order of a then b for each letter
    input: two strings"""
    if (s1 =='' or s2 ==''):
        return s1+s2
    else:
        rest_s = weave(s1[1:],s2[1:])
        return s1[0] + s2[0] + rest_s