#303 Range Sum Query - Immutable
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        sum = 0
        for i in range(1, len(self.nums)):
            sum = self.nums[i - 1]
            self.nums[i] = sum + self.nums[i]

    def sumRange(self, left: int, right: int) -> int:
        print(self.nums)
        # if left is not 0, have to subtract off everything left of that index
        if left != 0:
            return self.nums[right] - self.nums[left-1]
        return self.nums[right]
        

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
# -2, -2, 1, -4, -2, -3 
print(obj.sumRange(0, 2)) # 1

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(2, 5)) # -1

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 5)) # -3