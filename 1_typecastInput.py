import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


num = int(input())
num2 = int(input())
num3 = num + num2
print(num3)