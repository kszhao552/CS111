#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) Find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return prices
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

def avg_price(values):
    """returns the average price in a list of prices
    input: values is a list of 1 or more numbers"""
    avg = 0
    for i in values:
        avg += i
    avg/=len(values)
    return avg

def std_dev(values):
    """returns the standard deviation in a list of prices
    input: values is a list of 1 or more numbers"""
    avg = avg_price(values)
    var = 0
    for i in values:
        var += (i-avg)**2
    var /= len(values)
    std = math.sqrt(var)
    return std

def max_day(values):
    """returns the index of the highest element in a list of prices
    input: values is a list of 1 or more numbers"""
    max = 0
    for i in range(len(values)):
        if values[i] > values[max]:
            max = i
    return max

def any_below(values, n):
    """returns if there are any numbers in a list of prices below n
    input: values is a list of one or more numbers and n is a number"""
    for i in values:
        if i < n:
            return True
    return False

def find_plan(values):
    """returns the index of the days that create the largest difference
    of the prices and that difference
    input: values is a list of one or more numbers"""
    day1 = 0
    day2 = 0
    dif = 0
    for i in range(len(values)):
        for j in range (i, len(values)):
            if (values[j]-values[i])>dif:
                day1= i
                day2 = j
                dif = values[j]-values[i]
    return [day1, day2, dif]
            

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice ==3:
            average = avg_price(prices)
            print("The average price is", average)
        elif choice ==4:
            std = std_dev(prices)
            print("The standard deviation is", std)
        elif choice ==5:
            max = max_day(prices)
            print("The max price is", prices[max], "on day", max)
        elif choice ==6:
            val = int(input("Enter the threshold: "))
            below = any_below(prices, val)
            if below == True:
                print("There is at leas one price below", val)
            else:
                print("There are no prices below", val)
        elif choice ==7:
            best = find_plan(prices)
            print("Buy on day", best[0], "at price", prices[best[0]])
            print("Sell on day", best[1], "at price", prices[best[1]])
            print("Total profit:", best[2])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
