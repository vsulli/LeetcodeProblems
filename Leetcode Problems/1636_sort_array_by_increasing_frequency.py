''' 
Sort Array by Increasing Frequency
Leetcode # 1636
vsulli
23 July 2024

Given an array of integers nums, sort 
the array in increasing order based on 
the frequency of the values. If multiple 
values have the same frequency, sort them 
in decreasing order.

Return the sorted array.
'''

class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:

        num_map = {} # num: frequency

        # get count for each num in nums
        # could be replaced by count = Counter(nums)
        for i in range(len(nums)):
            if nums[i] in num_map:
                num_map[nums[i]] += 1
            else:
                num_map[nums[i]] = 1

        def custom_sort(n):
            return (num_map[n], -n)

        nums.sort(key = custom_sort)

        return nums


sol = Solution()

print(sol.frequencySort(nums = [1,1,2,2,2,3]))

print(sol.frequencySort(nums = [2,3,1,3,2]))

print(sol.frequencySort(nums = [-1,1,-6,4,5,-6,1,4,1]))