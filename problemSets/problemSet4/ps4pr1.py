# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 15:32:32 2019

@author: krado
"""

#ps4pr1
#Binary and Decimal problems using recursion

def dec_to_bin(n):
    """converts a number from its decimal form to its binary form
    input: a integer"""
    if n==0:
        return '0'
    if n==1: 
        return '1'
    else:
        rest_bin = dec_to_bin(n>>1)
        if n%2 ==1:
            return rest_bin+'1'
        else:
            return rest_bin +'0'

def bin_to_dec(s):
    """converts a number from its binary form to its decimal form
    input: a string that consists of the characters 1 and 0"""
    if s=='':
        return 0
    else:
        rest_num = bin_to_dec(s>>1)
        if (s[-1]=='1'):
            return (rest_num<<1) + 1
        else:
            return (rest_num<<1)