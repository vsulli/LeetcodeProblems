''' # TODO WIP
Frequency of the Most Frequent Element
Leetcode # 1838
vsulli
18 July 2024

The frequency of an element is the 
number of times it occurs in an array.

You are given an integer array 
nums and an integer k. In one 
operation, you can choose an index 
of nums and increment the element 
at that index by 1.

Return the maximum possible frequency 
of an element after performing at 
most k operations.

'''

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        # want to create max frequency possible by incrementing k times (on different indices)
        # first need to initalize hashmap with frequencies
        # nums already sorted, need to calculate how far away numbers are to see which one can be incremented
        # return max frequency

        max = 1
        num_hashmap = {}

        for i in range(len(nums)):
            if nums[i] in num_hashmap:
                num_hashmap[nums[i]] += 1
            else:
                num_hashmap[nums[i]] = 1

        # don't necessarily need hashmap?
        # start at index 0
        # say that is the number to reach, max_count = 1
        # move to next index, is there anything you can add to make it nums[0] ?
        

        # should calculate max here if there is one?
        # how do you calculate which number you need to make?
        inc = 0
        i = 0
        while inc < k:
            added = nums[i]
            while added not in nums[i+1:] and not inc > k:
                inc += 1
                added = nums[i] + inc
            
                # once you've found which number to reach, 
            i += 1
        
        print(num_hashmap)
        return max



sol = Solution()

print(sol.maxFrequency(nums = [1,2,4], k = 5)) # 3

print(sol.maxFrequency(nums = [1,4,8,13], k = 5)) # 2

print(sol.maxFrequency(nums = [3,9,6], k = 2)) # 1
