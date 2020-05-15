# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 00:15:47 2019

@author: krado
"""

def bitwise_and(b1, b2):
    """takes two binary numbers and ands them together. If one is shorter than the other, the longer one gets compared to 0's for blanks
    input: two strings consisting of 1's and 0's"""
    if b1 =='' and b2 =='':
        return ''
    elif b1 =='':
        return '0'*len(b2)
    elif b2 =='':
        return '0'*len(b1)
    else:
        bit_rest = bitwise_and(b1[:-1], b2[:-1])
        if b1[-1]=='1' and b2[-1]=='1':
            return bit_rest + '1'
        else:
            return bit_rest +'0'
        

def add_bitwise(b1, b2):
    """Takes two binary numbers and adds them togethers.
    input: two strings consisting of 1's and 0's"""
    if b1=='':
        return b2
    elif b2 =='':
        return b1
    else:
        bit_rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1]=='1' and b2[-1]=='1':
            return add_bitwise(bit_rest,'1')+ '0'
        else:
            if b1[-1]=='1':
                return bit_rest + '1'
            elif b2[-1]=='1':
                return bit_rest + '1'
            else:
                return bit_rest+ '0'
            
