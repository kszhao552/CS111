# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 19:15:32 2019

@author: krado
"""

def mirror(s):
    """returns the input as string twice as long and is mirrored
    input: strings"""
    new = s[:]+s[-1:0:-1]+s[0]
    return new

def is_mirror(s):
    """returns true or false depending on if the string could be made from teh mirror function
    input:strings"""
    new = s[:(len(s)//2)]
    if (mirror(new)==s):
        return True
    return False

def replace_end(values, new_end_vals):
    """returns the current list with the last values being replaced by the values in the second string
    input: lists"""
    if (len(new_end_vals)>=len(values)):
        return new_end_vals
    values = values[:-len(new_end_vals)] + new_end_vals
    return values

def repeat_elem(values, index, num_times):
    """ repeats the given index num_times in the given list values
    input: list and numbers"""
    values = values[0:index] + values[index:index+1]*num_times + values[index+1:]
    return values