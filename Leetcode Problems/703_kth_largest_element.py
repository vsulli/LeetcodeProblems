'''
Kth Largest Element in a Stream
Leetcode # 703
vsulli
13 July 2024

Design a class to find the kth largest 
element in a stream. Note that it is the 
kth largest element in the sorted order, 
not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) 
Initializes the object with the integer 
k and the stream of integers nums.
int add(int val) Appends the integer 
val to the stream and returns the element 
representing the kth largest element in 
the stream.
'''

import bisect
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)



# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
# sorted = [2, 4, 5, 8]
print(obj.add(3)) # 4 is the 3rd number after inserting
# sorted = [2, 3, 4, 5, 8]

print(obj.add(5))  # 5
# sorted = [2, 4, 4, 5, 8]