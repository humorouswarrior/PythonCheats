import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


s = {1, 2, 3}

s.add(4)                        # Add element: {1, 2, 3, 4}
print(s)
s.remove(2)                    # Remove: {1, 3, 4}
print(s)
# s.remove(5)                     # KeyError (not found)
print(s)
s.discard(3)                    # Remove: {1, 4}
print(s)
s.discard(5)                    # No error (not found): {1, 4}
print(s)
s.pop()                         # Remove arbitrary: returns 1, s = {4}
print(s)
s.clear()                       # Clear: set()
s = {1, 2, 3}
print(s)
s2 = s.copy()                   # Shallow copy: {1, 2, 3}
print(s2)


s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)                         # Union: {1, 2, 3, 4, 5}
print(s1 & s2)                         # Intersection: {3}
print(s1 - s2)                         # Difference: {1, 2}
print(s1 ^ s2)                         # Symmetric difference: {1, 2, 4, 5}
print({1, 2} <= s1)                    # Subset: True
print(s1 >= {1, 2})                    # Superset: True