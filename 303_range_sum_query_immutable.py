'''
Range Sum Query - Immutable
Leetcode # 303
vsulli
27 June 2024

Given an integer array nums, handle multiple 
queries of the following type:

Calculate the sum of the elements of 
nums between indices left and right inclusive where 
left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with 
the integer array nums.
int sumRange(int left, int right) Returns the sum 
of the elements of nums between indices left and 
right inclusive (i.e. nums[left] + nums[left + 1] 
+ ... + nums[right]).
 
'''

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2)) # 1
print(obj.sumRange(2, 5)) # -1
print(obj.sumRange(0, 5)) # -3