'''
Minimum Increment to Make Array Unique
Leetcode # 945
vsulli
14 June 2024

You are given an array nums. In one move, you can pick an index i
where 0 <= i < nums.length and increment nums[i] by 1

Return the minimum number of moves to make every value in nums unique

'''

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        # solution in one pass
        
        total = 0
        # sort array
        nums.sort()
        # loop through entire array starting at 2nd element
        for i in range(1, len(nums)):
            # current num less than or equal prev means duplicate
            if nums[i] <= nums[i-1]:
                newVal = nums[i -1] +1
                total += newVal - nums[i]
                # change current element to new value
                nums[i] = newVal

        return total
            
        


sol = Solution()


print(sol.minIncrementForUnique(nums = [1, 2, 2])) # 1 
# increment 2 at index 2 to 3


print(sol.minIncrementForUnique(nums = [3, 2, 1, 2, 1, 7])) # 6
# [3, 4, 1, 2, 5, 7]
# sorted [1, 1, 2, 2, 3, 7]
# unique set [1, 2, 3, 7]    # repeats [1, 2]
# 1-> 4 = 3
# 2-> 5 = 3
# 6 total
