nums = [2,2,3,1,1,0]
p = 0
k = 3
for n in range(k):
    nums[p+n] -= 1
print(nums)

p = 2
for n in range(k):
    nums[p+n] -= 1
print(nums)