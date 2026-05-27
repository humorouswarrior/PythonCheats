import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import OrderedDict

od= OrderedDict([(1,"raj"), (3,"vaibhav"), (2, "msd")])
print(od)
print(od[1])

if 10 in od:
    print(od[10])
else:
    print("10 not in dict")

od[10] = "kohli"
print (od)

od.move_to_end(3)
print(od)

od.move_to_end(3, False)
print(od)

print(od.popitem())
print (od)

print(od.pop(2))
print(od)