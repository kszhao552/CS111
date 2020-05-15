#
# Lab 4, Task 2 - debugging a recursive function
#

def count(val, values):
    """ returns the number of times that val is found in the list values
        parameters:
            val -- an arbitrary value
            values -- a list of 0 or more arbitrary values
    """
    if len(values) == 1:
        if values[0] == val:
            return 1
        else:
            return 0
    else:
        count_in_rest = count(val, values[1:])
        if values[0] == val:
            return count_in_rest + 1
        else:
            return count_in_rest

def negate_evens(values):
    if (values == []):
        return []
    else:
        val_rest = negate_evens(values[1:])
        if values[0]%2 ==0:
            return [-values[0]]+val_rest
        else:
            return [values[0]]+val_rest
        
def longest_word(wordlist):
    """ returns the longest word from the wordlist passed in as 
        a parameter
    """
    pairs = [[len(w), w] for w in wordlist]
    bestpair = max(pairs)
    return bestpair[1]

def square(value):
    """ a helper function that takes a value
        and returns its square
    """
    sq = value ** 2
    return sq

def process_squares(values, choice):
    squares = [[square(val), val] for val in values]
    best = max(squares)
    if choice == 1:
        return best[0]
    else:
        return best[1]
    
def myslice(values, start, stop):
    if values == []:
        return []
    else:
        slice_rest = myslice(values[1:], (start-1), (stop-1))
        if start <= 0 < stop:
            return [values[0]]+slice_rest
        else:
            return slice_rest
    
        