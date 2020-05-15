def num_divisors(s):
    div = [i for i in range (1,s+1) if s%i ==0]
    return len(div)

def most_divisor(lst):
    if lst == []:
        return 0
    else:
        most = most_divisor(lst[1:])
        if num_divisors(most) < num_divisors(lst[0]):
            return lst[0]
        else:
            return most

def count_transitions(s):
    if s == '':
        return 0
    else:
        num = count_transitions(s[1:])
        if len(s)==1:
            return 0
        elif s[1] == s[0]:
            return num
        else:
            return 1 + num
    
def longest_string(lst):
    if lst == []:
        return ''
    else:
        long = longest_string(lst[1:])
        if len(long) < len(lst[0]):
            return lst[0]
        else:
            return long

def cycle(s, n):
    new_s = s[-1:]*n + s[:-1]
    return new_s
