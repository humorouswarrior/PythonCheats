import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


import itertools

print(list(itertools.combinations([1,2,3], 2)))      # [(1,2), (1,3), (2,3)]
print(list(itertools.combinations_with_replacement([1,2], 2)))  # [(1,1), (1,2), (2,2)]
print(list(itertools.permutations([1,2], 2)))        # [(1,2), (2,1)]
print(list(itertools.product([1,2], [3,4])))         # [(1,3), (1,4), (2,3), (2,4)]
# print(list(itertools.cycle([1,2,3]))[:7])            # [1,2,3,1,2,3,1] (first 7)
print(list(itertools.repeat(5, 3)))                  # [5, 5, 5]
print(list(itertools.chain([1,2], [3,4], [5])))      # [1, 2, 3, 4, 5]
print(list(itertools.accumulate([1,2,3,4])))        # [1, 3, 6, 10] (cumulative sum)
print(list(itertools.accumulate([1,2,3,4], lambda x,y: x*y)))  # [1, 2, 6, 24]
groups = itertools.groupby([1,1,2,2,2,3])
print([(k, list(g)) for k, g in groups])            # [(1, [1,1]), (2, [2,2,2]), (3, [3])]
