''' 
Sort an Array
Leetcode # 912
vsulli
25 July 2024

Given an array of integers 
nums, sort the array in 
ascending order and return it.

You must solve the problem 
without using any built-in 
functions in O(nlog(n)) time 
complexity and with the smallest 
space complexity possible.
'''
def heapify(array, size, i):
       largest = i
       l = 2 * i + 1
       r = 2 * i + 2

       # check if left child of root is greater than root
       if l < size and array[largest] < array[l]:
        largest = l

        # see if right child exists and is greater than root
        if r < size and array[largest] < array[r]:
          largest = r

        if largest != i:
          array[i], array[largest]  = array[largest], array[i]

          heapify(array, size, largest)

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        size = len(nums)

        # build maxheap
        for i in range(size // 2 - 1, -1, -1):
            heapify(nums, size, i)

        for i in range(size -1, 0, -1):
           nums[i], nums[0] = nums[0], nums[i]
           heapify(nums, i, 0)

        return nums

sol = Solution()

print(sol.sortArray(nums = [5,2,3,1])) # [1,2,3,5] 
# positions of some numbers aren't changed (2,3)
# 1 and 5 swapped

