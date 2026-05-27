import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

from collections import Counter

arr= [1,2,2,3,4,3,3,4]
counts=Counter(arr)
print(counts[4])

print(counts.most_common(1)) #first most common element based on insertion order

print(counts.most_common(10))

print(list(counts.elements()))

counts.update([7,5])
print(list(counts.elements()))

counts.subtract([3,4,9])  #subtracting non existent element does nothing. no error either 
print(list(counts.elements()))


c1 = Counter([1,3,2,2,2,2,2,3,3,4])
c2 = Counter([3,3,1,4,5])

c3 = c1 -c2
print (list(c3.elements()))

c4 = c1 + c2
print (list(c4.elements()))

c5 = c1 & c2    #takes commanality
print (list(c5.elements())) 

c6 = c1 | c2   #takes max occurance of all
print (list(c6.elements())) 


