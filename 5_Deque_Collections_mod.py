import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import deque

dq =deque([2,3,1])
dq.append(5)
print (dq)

dq.appendleft(7)
print (dq)

print(dq.pop())
print (dq)

print(dq.popleft())
print(dq)

dq.extend([10,19]) # add multiple elements
print (dq)

dq.extendleft([89, "striver"])
print(dq)

dq.rotate(1)
print(dq)

dq.rotate(3)
print (dq)