nums = [1,5,0,3,5]

print(sum(nums[:]))
x = min(n for n in nums if n != 0)
print(x)

for i in range(len(nums)):
    if nums[i] > 0:
        nums[i] = nums[i] - x

print(nums)