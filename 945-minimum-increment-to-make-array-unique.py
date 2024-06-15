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
        total = 0
        count = 0
        seen_set = set()

        for i in range(len(nums)):
            # if num has already been seen, put in repeats
            count = 0
            if nums[i] in seen_set:
                while nums[i] in seen_set:
                    nums[i] += 1
                    count += 1
                seen_set.add(nums[i])
                total += count
            # add to seen
            else:
                seen_set.add(nums[i])

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
