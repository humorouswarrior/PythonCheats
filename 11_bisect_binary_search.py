import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


import bisect
#ARRAY MUST BE SORTED TO USE THIS

arr = [1, 3, 3, 3, 5, 7]
print(bisect.bisect_left(arr, 3))      # Leftmost position for new insertion: 1
print(arr)
print(bisect.bisect_left(arr, 4))      # Position to insert 4 if you had to: 4
print(bisect.bisect_right(arr, 3))     # Rightmost position for new insertion: 4
print(bisect.bisect(arr, 3))           # Same as bisect_right: 4
arr = [1, 3, 5]
bisect.insort_left(arr, 2)      # Insert at leftmost: [1, 2, 3, 5]
print(arr)
bisect.insort_right(arr, 3)     # Insert at rightmost: [1, 2, 3, 3, 5]
print(arr)
bisect.insort(arr, 4)           # Same as insort_right: [1, 2, 3, 3, 4, 5]
print(arr)