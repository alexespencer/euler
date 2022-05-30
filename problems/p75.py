import sys, os, time
sys.path.insert(0, os.getcwd())

from euler import is_square

triangles = {}

# For a right angled triangle with integer sides there are a number of properties we might be able to use:
# a + b + c % 6 == 9
# a * b * c % 60 == 0
# We could try iterating x 60, 120, 180 etc - and finding triangles that have a * b * c = x

max_length = 150000
for x in range(60, 1000, 60):
    pass