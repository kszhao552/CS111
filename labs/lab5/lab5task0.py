#
# Lab 5, Task 0
#

def bitwise_or(b1, b2):
    """ computes and returns the bitwise OR of binary numbers b1 and b2
        inputs: b1 and b2 are strings that represent binary numbers
    """
    if b1 == '' and b2 == '':
        return ''
    elif b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        # implement the recursive case here
        rest = bitwise_or(b1[:-1], b2[:-1])
        if (b1[-1]=='1' or b2[-1]=='1'):
            return rest+'1'
        else:
            return rest+'0'

