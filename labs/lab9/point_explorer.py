#
# point_explorer.py
#
# The beginnings of a client program for Point objects
#
# CS 111
#

from point import *

p1 = Point(7, 24)
p2 = Point(0, -7)

print('p1 has coordinates', p1)   # calls __repr__
print('p2 has coordinates', p2)   # calls __repr__

dist1 = p1.distance_from_origin()
dist2 = p2.distance_from_origin()
print(p1, 'is', dist1, 'away from the origin')
print(p2, 'is', dist2, 'away from the origin')

print('moving p1 down 7 units...')
p1.move_down(7)
print('p1 now has coordinates', p1)


x = int(input("input an x value: "))
y = int(input("input a y value: "))
p3 = Point(x,y)
dist3 = p3.distance_from_origin()
print(p3, 'is', dist3, 'away from the origin')
print('flipping p3...')
p3.flip()
print('p3 now has coordinates', p3)
quad = p3.quadrant()
if quad ==0:
    print("p3 is on an axis")
else:
    print("p3 is now in quadrant", quad)