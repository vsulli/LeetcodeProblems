''' 
Sum of Distances
Leetcode # 2615
vsulli
8 August 2024

You are given a 0-indexed integer 
array nums. There exists an array 
arr of length nums.length, where 
arr[i] is the sum of |i - j| over 
all j such that nums[j] == nums[i] 
and j != i. If there is no such j, 
set arr[i] to be 0.

Return the array arr.
 
'''
class Solution:
    def distance(self, nums: list[int]) -> list[int]:
        # answer array to return
        arr = []

        indices = []

        for i in range(0, len(nums)):
            # arr at index will equal the sum of differences
            # in locations of that index value
            sum = 0
            for j in range(0, len(nums)):
                if nums[j] == nums[i]:
                    indices.append(j)
            for k in indices:
                sum += abs(i - k)
            arr.append(sum)
        return arr

sol = Solution()

print(sol.distance(nums = [1,3,1,1,2])) # [5, 0, 3, 4, 0]

print(sol.distance(nums = [0,5,3])) # [0, 0, 0]