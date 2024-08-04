# Review
# 347 - Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            # get count for numbers, 0 default
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
        # add number to list at index of its frequency
            frequency[c].append(n)
        
        res = []
        # iterate list in descending order
        for i in range(len(frequency) - 1, 0, -1):
            # iterate through every number at that index
            for n in frequency[i]:
                res.append(n)
                # return res when it's length of k
                if len(res) == k:
                    return res
	

    

    
sol = Solution()
print(sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2)) # [1, 2]

print(sol.topKFrequent(nums = [1], k = 1)) # [1]