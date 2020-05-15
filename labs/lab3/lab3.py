#
# Name: CS 111 Staff
#
# lab3.py
#

def num_consonants(s):
    """ returns the number of consonants in s
        parameter: s is a string of lower-case letters
    """
    if s == ' ':
        return 0
    else:
        num_in_rest = num_consonants(s[1:])
        if s[0] not in 'aeiou':
            return num_in_rest
        else:
            return num_in_rest + 1
    
    
def remove_spaces(s):
    if (s ==''):
        return s
    else:
        rest_string = remove_spaces(s[1:])
        if s[0] == ' ':
            return rest_string
        return s[0] + rest_string
    
def min_val(s):
    if (len(s)==1):
        return s[0]
    else:
        rest_min = min_val(s[1:])
        if (s[0] < rest_min):
            return s[0]
        return rest_min