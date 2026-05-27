import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


arr= [5,6,1,3,8]
print(list(enumerate(arr)))

for i, val in list(enumerate(arr)):
    print(i, val)