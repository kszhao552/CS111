# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below


def cube(x):
    """returns teh cube of its input
       input x: any number (int or float)
    """
    return x**3


def convert_to_inches(yards, feet):
    "returns the length of the yards and feet in inches"""
    inches = 0
    if (yards >=0):
        inches = inches + yards*36
    if (feet>= 0):
        inches = inches + feet*12
    return inches

def area_sq_inches (height_yds, height_ft, width_yds, width_ft):
    """returns the area of a rectangle in square inches
    input: any four numbers"""
    height = convert_to_inches(height_yds, height_ft)
    width = convert_to_inches(width_yds, width_ft)
    area = height*width
    return area

def median (a,b,c):
    """returns the median of three numbers
    input is three numbers"""
    if (a>b>c) :
        return b
    elif (c>b>a):
        return b
    elif (c<a<b):
        return a
    elif (b<a<c):
        return a
    return c
# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))

    # optional but encouraged: add test calls for your functions below
