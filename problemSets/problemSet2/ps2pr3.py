# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 14:07:08 2019

@author: krado
"""
def flipside(s):
    """switches the first half and second half of a string 
    input: strings"""
    s = s[len(s)//2:]+s[:len(s)//2]
    return s

def adjust(s, length):
    """adjusts the length of string by given input amount
    if too short, then cut the string, if too long, pad the string
    input: string followed by int"""
    if (length>len(s)):
        length = length - len(s)
        s = " "*length + s
    else :
        s = s[:length]
    return s
