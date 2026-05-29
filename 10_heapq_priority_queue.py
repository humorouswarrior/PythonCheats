import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


import heapq
#minimum comes leftmost (minheap, rest order we do not care)

#by default its minheap
heap = []
heapq.heappush(heap, 3)         # Push: heap = [3]
heapq.heappush(heap, 1)         # Push: heap = [1, 3]
heapq.heappush(heap, 2)         # Push: heap = [1, 2, 3]
print(heap)
heapq.heappop(heap)             # Pop smallest: returns 1, heap = [2, 3]
print(heap)
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)              # Convert to heap: arr = [1, 1, 4, 3, 5]
print(arr)
heapq.heappushpop(heap, 0)      # Push 0 then pop: returns 0
print(heap)
heapq.heapreplace(heap, 5)       # Pop then push 5: returns 2
print(heap)
print(heap[0])                         # Get smallest: 3 (without removing)
heapq.nlargest(3, [1,2,3,4,5])   # 3 largest: [5, 4, 3]
heapq.nsmallest(2, [3,1,4,1,5])  # 2 smallest: [1, 1]


#maxheap trick - negation karke value of numbers go upside down
max_heap = []
#maximum comes leftmost (maxheap, rest order we do not care)
heapq.heappush(max_heap, -10)   # Push negated: [-10]
heapq.heappush(max_heap, -5)    # Push negated: [-10, -5]
max_val = -heapq.heappop(max_heap)  # Pop and negate: returns 10

print(max_val)