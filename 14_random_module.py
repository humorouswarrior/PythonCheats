import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

import random

print(random.random())                # Float in [0.0, 1.0): 0.123456...
print(random.randint(1, 10))           # Integer in [1, 10]: 7 (example)
print(random.randrange(0, 10, 2))     # Even numbers 0-8: 4 (example)
print(random.choice([1, 2, 3, 4]))    # Random element: 3 (example)
print(random.sample([1,2,3,4,5], 3))  # 3 random elements: [2, 5, 1] (example)
arr = [1, 2, 3, 4, 5]
print(random.shuffle(arr))            # Shuffle in-place: arr = [3, 1, 5, 2, 4] (example)
print(random.uniform(1.0, 10.0))      # Float in [1.0, 10.0]: 5.678... (example)