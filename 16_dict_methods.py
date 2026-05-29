import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

d = {'a': 1, 'b': 2}
print(d['a'])                         # Get value: 1
# print(d['c'])                         # KeyError (missing key)
print(d.get('a'))                     # Get value: 1
print(d.get('c', 0))                  # Get with default: 0
d['c'] = 3                     # Set value: {'a': 1, 'b': 2, 'c': 3}
d.update({'d': 4})             # Update: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d)
d.pop('c')                     # Remove and return: 3
print(d)
d.pop('x', -1)                 # Remove with default: -1 (key not found)
print(d)
d.popitem()                    # Remove last: ('d', 4)
print(d)
print(list(d.keys()))                 # View of keys: ['a', 'b']
print(list(d.values()))               # View of values: [1, 2]
print(list(d.items()))                # View of pairs: [('a', 1), ('b', 2)]
d.clear()                      # Clear: {}
d = {'a': 1, 'b': 2}
print('a' in d)                       # Check if key exists: True
d2 = d.copy()                  # Shallow copy: {'a': 1, 'b': 2}
print(d2)
d2['a'] = 500
print(d2)