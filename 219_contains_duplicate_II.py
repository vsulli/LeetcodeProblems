'''
Contains Duplicate II
Leetcode # 219
vsulli
11 June 2024

Given an integer array nums and an integer k, 
return true if there are two distinct indices, i and j
in the array such that nums[i] == nums[j] and abs(i - j) <= k
'''

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        # looking for number appearing twice in array
        # difference between indices is less than or equal to k
        # will need to loop through all numbers in nums
        # will need a dict, check if number already exists in dict
        # if it does, calculate difference in index
        # if that difference = k, return True, else add to dict num:[indices]

        hm = {}

        for i in range(len(nums)):
            # if num not already in hashmap add it
            if nums[i] not in hm:
                hm[nums[i]] = i
                continue
            else:
                # if difference in indices <= k return True
                if abs(i - hm[nums[i]])<=k:
                    return True
                # otherwise add to hashmap
                hm[nums[i]]=i
        return False

sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3)) # true (index 3 - 0 = 3)

print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1)) # true (index 3 - 2 = 1)
# if there are multiple duplicates, how to store that info?

print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2)) # false (all indices are 3 apart)

print(sol.containsNearbyDuplicate(nums = [99, 99], k = 2)) # true because difference just needs to be less than
# or equal to k