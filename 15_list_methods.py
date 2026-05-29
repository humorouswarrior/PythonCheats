import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

lst = [1, 2, 3]
lst.append(4)                  # Add to end: [1, 2, 3, 4]
lst.extend([5, 6])             # Extend: [1, 2, 3, 4, 5, 6]
lst.insert(0, 0)              # Insert at index 0: [0, 1, 2, 3, 4, 5, 6]
lst.remove(3)                  # Remove first 3: [0, 1, 2, 4, 5, 6]
lst.pop()                      # Remove last: returns 6, lst = [0, 1, 2, 4, 5]
lst.pop(0)                     # Remove at index 0: returns 0, lst = [1, 2, 4, 5]
lst.index(2)                   # Index of 2: 1
lst.count(2)                   # Count of 2: 1
lst.sort()                     # Sort: [1, 2, 4, 5]
lst.sort(reverse=True)         # Sort descending: [5, 4, 2, 1]
lst.reverse()                  # Reverse: [1, 2, 4, 5]
lst.clear()                    # Clear: []
lst = [1, 2, 3]
lst2 = lst.copy()              # Shallow copy: [1, 2, 3]

lst2[0] = 500
print(lst2)
print(lst)