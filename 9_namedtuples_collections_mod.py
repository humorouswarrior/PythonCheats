import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import namedtuple

Point= namedtuple("Point", ["First", "Second"])
val1 = Point(2,9)
print(val1)

# these are immutable since tuples are mutable


# can be implemented in mutable way with the help of custom class
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second

var = Pair(2,5)
print(var.first, var.second)

var.first = 7
print(var.first, var.second)
