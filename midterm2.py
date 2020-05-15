# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 17:10:51 2019

@author: krado
"""

def years_needed(principal, rate, target):
    count =0
    while(True):
        if principal>=target:
            break
        principal *= rate
        count+=1
    return count

def count_vowels(s):
    count =0
    for x in s:
        if x in 'AEIOUaeiou':
            count+=1
    return count

def stars(n):
    for i in range(n+1):
        for j in range(i):
            print('*', end  ='')
        print()
  
def all_perfect(lst):
    for i in lst:
        if i != 100:
            return False
    return True

def index_nearest(n, lst):
    cdist = abs(lst[0]-n)
    cindex = 0
    for i in range(len(lst)):
        if abs(lst[i]-n)<cdist:
            cindex = i
            cdist = abs(lst[i]-n)
    return cindex

def num_appearances(substring, s):
    count=0
    for i in range(len(s)):
        if substring == s[i:i+2]:
            count += 1
    return count
        
def most_common_pair(s):
    mcount=0
    mpair = s[0:2]
    for i in range(len(s)):
        if num_appearances(s[i:i+2], s)> mcount:
            mcount = num_appearances(s[i:i+2], s)
            mpair = s[i:i+2]
    return mpair

def longest_dna(s):
    longest = ''
    current = ''
    for c in s:
        if c in 'ACGT':
            current += c
            if len(current) > len(longest):
                longest = current
        else:
            current = ''
    return longest