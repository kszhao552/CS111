# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:32:54 2019

@author: krado
"""

#
# Lab 7
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('0) Input new goal lists')
    print('1) Get the latest score')
    print('2) Find the max number of goals')
    print('3) Find the number of wins')
    print('4) Print the results')
    
    ## Add any new menu options here.
    print("5) Find the full record")

    print('7) Quit')
    print()

def latest_score(terriers, opponents):
    """ returns the score of the latest (i.e., most recent) game
        inputs: terriers - a list of goals scored by the Terriers in a 
                  set of games
                opponents - a list of goals scored by their opponents
        We assume that both lists contain the same number of integers,
        and that they each contain at least one integer.
    """
    score = str(terriers[-1]) + '-' + str(opponents[-1])
    return score

## Add your helper functions for the remaining options below.
            
def find_max_goals(goals):
    """ returns the largest number of goals in the specified 
        list of goals, which we assume contains at least one integer
    """
    maxg = goals[0]

    for g in goals:
        if g > maxg:
            maxg = g

    return maxg

def find_num_wins(terriers, opponents):
    """returns the number of wins for the terriers"""
    wins = 0
    for i in range(len(terriers)):
        if terriers[i] >opponents[i]:
            wins += 1
    return wins

def print_results(terriers, opponents):
    """prints the results for each game"""
    state = ""
    for i in range(len(terriers)):
        if terriers[i]>opponents[i]:
            state = "win"
            print(state, str(terriers[i])+'-'+str(opponents[i]))
        elif terriers[i]==opponents[i]:
            state = "tie"
            print(state, str(terriers[i])+'-'+str(opponents[i]))
        else:
            state = "lose"
            print(state, str(terriers[i])+'-'+str(opponents[i]))
        
def get_record(terriers, opponents):
    record = [0,0,0]
    for i in range(len(terriers)):
        if terriers[i]>opponents[i]:
            record[0]+=1
        elif terriers[i]==opponents[i]:
            record[2]+=1
        else:
            record[1]+=1
    return record

def main():
    """ the main user-interaction loop
    """
    terriers = []
    opponents = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            terriers = eval(input('Enter the Terriers list of goals: '))
            opponents = eval(input('Enter their opponents list of goals: '))
            if len(terriers) != len(opponents):
                print('The lists must have the same length.')
                print('Please select menu option 0 to try again.')
                terriers = []
                opponents = []
        elif choice == 7:
            break
        elif choice < 7 and len(terriers) == 0:
            print('You need to first enter the goal lists.')
            print('Please select menu option 0 to do so.')
        elif choice == 1:
            score = latest_score(terriers, opponents)
            print('The score of the latest game was', score)
        ## add code to process the other choices here
        elif choice ==2:
            maxgoals = find_max_goals(terriers)
            print (maxgoals)
        elif choice == 3:
            wins = find_num_wins(terriers, opponents)
            print (wins)
        elif choice ==4:
            print_results(terriers, opponents)
        elif choice ==5:
            record = get_record(terriers, opponents)
            print(record)
        else:
            print('Invalid choice. Please try again.')

    print('Goodbye!')

