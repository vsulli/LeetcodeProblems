# Review
# 347 - Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ans = []
        res = [0] * (max(nums)+1)
        for n in set(nums):
            count = nums.count(n)
            res[n] = count
		
        # need to return indices for k most frequent
        print(res)
        for i in range(k):
            index = res.index(max(res))
            ans.append(index)
            res[index] = 0
            
        return ans
	

    

    
sol = Solution()
sol.topKFrequent(nums = [1,1,1,2,2,3], k = 2) # [1, 2]

sol.topKFrequent(nums = [1], k = 1) # [1]