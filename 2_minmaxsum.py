import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

arr = [-15,6,8,7]

print(max(arr))
print(max(arr, key = lambda x:abs(x)))

print(sum(arr))  # 0+ -15 +6+8+7

print(sum(arr, start=10)) # 10+ -15 +6+8+7


import math
print(math.prod(arr))


arr = [True,False,True]
print(any(arr)) # if atleast 1 (any) in array is true then true
print(all(arr)) #if all are true then true


print(arr.count(True))