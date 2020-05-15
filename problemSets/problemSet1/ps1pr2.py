# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:10:53 2019

@author: krado
"""

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]
b = 'boston'
u = 'university'
t = 'terriers'


#puzzle 0:
#Creating the list [2,5,9]
answer0 = e[0:1] + pi[4:]
#puzzle 1:
#Creating the list [7,1] from pi and e
answer1 = e[1:3]
#puzzle 2
#Creating the list [9, 1, 1]
answer2 = pi[::-2]
#puzzle 3
#Creating the list [1,2,3,4,5]
answer3 = e[-1::-2] + pi[::2]


# Example puzzle (puzzle 4)
# Creating the string 'bossy'
answer4 = b[:3] + t[-1] + u[-1]
#puzzle 5
#Creating the string 'stone'
answer5 = b[2:] + t[1] 
#puzzle 6
#Creating the string 'nonononono'
answer6 = b[-1:3:-1]*5
#puzzle 7
#Creating the string 'bestever'
answer7 = b[0] + u[4:9:2] + u[4:2:-1] +u[4:6]
#puzzle 8
#Creating the string 'serenity'
answer8 = b[2] + u[4:6] + u[4:0:-3] + u[-3:]