# reviewing problem

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):
            print("l: " + str(l))
            print("r: " + str(r))
            print("------")
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1
                print("     l: " + str(l))
                print("     r: " + str(r))


        return 0 if res == float("inf") else res

            
sol = Solution()

'''

print(sol.minSubArrayLen(target = 8, nums = [7])) # 0

print(sol.minSubArrayLen(target = 8, nums = [8])) # 1
'''

print(sol.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])) # 2

'''
print(sol.minSubArrayLen(target = 4, nums = [1,4,4])) # 1

print(sol.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])) # 0
'''
