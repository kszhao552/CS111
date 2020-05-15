#
# lab1task2.py
#
# name: CS 111 course staff
# email: cs111-staff@cs.bu.edu
#se)

course = 111
print('congratulations on taking CS', course

course = course + 1 #takes the current course number and sets it as the next number
print('maybe you will take CS', course, 'next semester') #prints out the line stating that you'll maybe you'll take the next course next semester
print()

days = 40
print('the first midterm is in fewer than', days, 'days')

weeks = days // 7
print('that is approximately', weeks, 'weeks')
#a). weeks is a variable that contains an int inside it and will print the number stored while 'weeks' is a string and will print out as the word
#b). It prints 5 because it is integer division and not float division, meaning that the new number will always be an int
#       When int division occurs, it automatically truncates after the decimal so the number will always round down, in this case 5.7... rounds down to 5
#c). In order to print out a more precise number of weeks, you can change the int division into a float division by removing one of the /
print()
print('Go Terriers!')
print('pi is approximately', (22 / 7))