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
        # get prefix sum
        self.prefix_sum = [0] * len(nums) + 1
        for i in range(len(nums)):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # why right + 1?
        return self.prefix_sum[right+1] - self.prefix_sum_left


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2)) # 1
print(obj.sumRange(2, 5)) # -1
print(obj.sumRange(0, 5)) # -3
print(obj.sumRange(0, 0)) # -2