# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:56:39 2019

@author: krado
"""

def log(b, n):
    """finds the log of n with base b
    input: two integer numbers"""
    div = 0
    while(True):
        if n<=1 :
            break
        div+=1
        print("dividing", str(n), "by", str(b), "gives", str(n//b))
        n//=b
    return div
            

def add_powers(m, n):
    """finds the sum of the first m powers of n
    input: two integer numbers"""
    sum =0
    for i in range(m):
        print(str(n), "**", str(i), "=", str(n**i))
        sum += n**i
    return sum    

def square_evens(values):
    """takes all of the elements that are even in a list and squares it
    input: a list comprised of numbers"""
    for i in range(len(values)):
        if values[i]%2==0:
            values[i] **= 2
            