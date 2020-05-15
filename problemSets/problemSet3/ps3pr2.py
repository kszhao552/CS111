# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 16:15:31 2019

@author: krado
"""

#ps2pr3
#algorithm design problems



#list comprehension problem

def cube_all_lc(values):
    """returns the cube of all values wihtin a list using list comprehension
    input: a list comprised of any numbers"""
    cubes = [n**3 for n in values]
    return cubes

#recursion problem
def cube_all_rec(values):
    """cubes all the values within a list using recursion
    input: a list comprised of numbers"""
    if values == []:
        return []
    else:
        cube_rest = cube_all_rec(values[1:])
        current = [values[0]**3]
        return current + cube_rest
    
def num_larger(threshold, values):
    """returns the number of elements that have values larger than a threshold
    input: a num follwed by a list comprised of numbers"""
    num = sum([1 for n in values if (n>threshold)])
    return num

def num_vowels(s):
    """ returns the number of vowels in the string s
        input: s is a string of 0 or more lowercase letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_vowels(s[1:])
        if s[0] in 'aeiou':
            return 1 + num_in_rest
        else:
            return 0 + num_in_rest

def most_consonants(words):
    """returns the string with the most amount of cosonants in the list
    input: a list containing strings comprised of letters"""
    cos = [[len(x)-num_vowels(x),x] for x in words]
    best_pair = max(cos)
    return best_pair[1]

def price_string(cents):
    """returns the amount of cost of the item in dollars and cents
    input: a postive integer"""
    
    d = cents//100
    c = cents%100
    price = ''
    
    
    if d!=0:
        if d==1:
            price = str(d) + ' dollar'
        else:
            price = str(d) + ' dollars'
        if c!=0:
            if c==1:
                price = price + ', ' + str(c) + ' cent'
            else:
                price =price + ', ' + str(c) + ' cents'
    else:
         if c!=0:
            if c==1:
                price = str(c) + ' cent'
            else:
                price = str(c) + ' cents'
    return price