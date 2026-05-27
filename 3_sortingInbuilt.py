import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

arr= [1,3,2,6,5,4]
print (sorted(arr))
print (arr)

arr.sort(reverse= True)
print (arr)


arr2 = [-6,-2,4,9,1]
print(sorted(arr2, reverse =True))
print(sorted(arr2, key =lambda x:abs(x)))


fruits_list = ["pineapple", "banana", "apple", "oranges"]
print(sorted(fruits_list, key = lambda x:len(x)))


print(list(reversed(arr2)))