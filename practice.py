# 704 Binary Search


class Solution:
    def search(self, nums: list[int], target: int)-> int:
        
        def binary_search(data, target, left, right):
            # left pointer has passed right pointer
            if left > right:
                return -1
            else:
                mid = (left + right) // 2
                if target == data[mid]:
                    return mid
                elif target < data[mid]:
                    return binary_search(data, target, left, mid - 1)
                else:
                    return binary_search(data, target, mid + 1, right)
                
        l, h = 0, len(nums) - 1

        return binary_search(nums, target, l, h)





sol = Solution()
print(sol.search(nums = [-1,0,3,5,9,12], target = 9)) # 4

print(sol.search(nums = [-1,0,3,5,9,12], target = 2)) # -1


