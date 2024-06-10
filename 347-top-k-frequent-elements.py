'''
Top K Frequent Elements
Leetcode # 347
vsulli
10 June 2024

Given an integer array nums and an integer k, 
return the k most frequent elements. 

You may return the answer in any order
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        num_dict = {} # num: frequency

        for n in nums:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1
        
        # sort dictionary by value
        sorted_num_dict = {k: v for k, v in sorted(num_dict.items(), key=lambda item: item[1], reverse=True)}
        print(sorted_num_dict)


sol = Solution()
print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2)) # [1, 2] returns the two numbers that occur most frequently

print(sol.topKFrequent(nums = [1], k = 1)) # [1]