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
        # sort array
        # get indices of nums that aren't unique
            # create a seen_hashmap
            # repeat_hashmap
        # loop through indices that aren't unique, incrementing 
        # the indices until they're all unique
        total = 0
        count = 0
        seen_set = set()
        repeat_list= []
        sorted_nums = sorted(nums)
        print(sorted_nums)

        for i in range(len(sorted_nums)):
            # if num has already been seen, put in repeats
            if sorted_nums[i] in seen_set:
                repeat_list.append(sorted_nums[i])
            # add to seen
            else:
                seen_set.add(sorted_nums[i])
        
        # need to loop through repeat_hashmap keys
        # increment them and add to seen_hashmap

        # while repeat_hashmap isn't empty
        while repeat_list:
            count = 0
            key = repeat_list[0]
            # increment key and check if it is in seen set
            while key in seen_set:
                key += 1
                count+=1
            # if it is not, add it, remove from repeat list
            seen_set.add(key)
            del repeat_list[0]
            total += count
        return count
            
        


sol = Solution()

print(sol.minIncrementForUnique(nums = [1, 2, 2])) # 1 
# increment 2 at index 2 to 3

'''
print(sol.minIncrementForUnique(nums = [3, 2, 1, 2, 1, 7])) # 6
# [3, 4, 1, 2, 5, 7]
# sorted [1, 1, 2, 2, 3, 7]
'''