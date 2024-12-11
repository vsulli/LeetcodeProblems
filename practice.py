#303 Range Sum Query - Immutable
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.sum = 0
        for i in range(len(self.nums)):
            self.nums[i] = self.sum + self.nums[i]
            self.sum = self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # if left is not 0, have to subtract that off?
        if left != 0:
            return self.nums[right] - self.nums[left]
        return self.nums[right]
        

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
# -2, -2, 1, -4, -2, -3 
print(obj.sumRange(0, 2)) # 1

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(2, 5)) # -1 WRONG

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 5)) # -3