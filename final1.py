def create_2d(h, w):
    lis= []
    for r in range(h):
        lis += [[0]*w]
    for r in range(len(lis)):
        for c in range(len(lis[0])):
            lis[r][c] = r*c
    return lis
        
def add_one(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            grid[r][c] += 1

class Phonebook:
    def __init__(self):
        self.entries = {}

    def add_entry(self, name, number):
        self.entries[name]=number

    def contains(self, name):
        if name in self.entries:
            return True
        return False

    def number_for(self, name):
        if self.contains(name):
            return self.entries[name]
        return -1

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        area = self.base*self.height/2
        return area

    def __repr__(self):
        s = 'triangle with base ' + str(self.base) + ' and height ' + str(self.height)
        return s

    def __eq__(self, other):
        if self.base == other.base and self.height == other.height:
            return True
        return False
def main():
    tri1 = Triangle(3, 4)
    tri2 = Triangle(6,6)
    tri3 = Triangle(3,4)
    print('tri1:', tri1)
    print('tri2:', tri2)
    print('tri3:', tri3)
    if tri1 == tri2:
        print('tri1 and tri2 are equal')
    else:
        print('tri1 and tri2 are not equal')
    if tri1 ==tri3:
        print('tri1 and tri3 are equal')
    else:
        print('tri1 and tri3 are not equal')


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        height = side *.866
        super().__init__(side, height)

    def __repr__(self):
        t = 'equalateral triangle with side ' + str(self.base)
        return t


def merge(list1, list2):
    if list1 == []:
        return list2
    elif list2 ==[]:
        return list1
    else:
        newList = merge(list1[1:], list2[1:])
        if list1[0] < list2[0]:
            newList = [list1[0]] + [list2[0]] + newList
            return newList
        else:
            newList = [list2[0]] + [list1[0]] + newList
            return newList


def count_ones(s):
    total=0
    for c in s:
        if c == '1':
            total+=1
    return total

def swap_bits(s):
    new = ''
    for c in s:
        if c == '0':
            new+= '1'
        else:
            new+='0'
    return new

def num_divisors(n):
    total =0
    for i in range(1,n):
        if n%i == 0:
            total +=1
    return total

def most_divisors(lst):
    high = lst[0]
    highf = num_divisors(lst[1])
    for i in lst:
        if num_divisors(i)>highf:
            high = i
            highf = num_divisors(i)
    return high

def count_transitions(s):
    cur = s[0]
    count = 0
    for i in s:
        if i != cur:
            cur =i
            count += 1
    return count

def longest_string(lst):
    cur = lst[0]
    length = len(cur)
    for i in lst:
        if len(i) >length:
            cur = i
            length = len(i)
    return cur

def cycle(s,n):
    new = ''
    new+= s[-n:]
    new+= s[:-n]
    return new
            
