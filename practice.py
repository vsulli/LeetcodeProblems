# Daily Practice Sheet for use with ANKI

nums = [1,2,3,1]
k = 3

nearby_duplicate = False
nums_seen = {}
for i in range(len(nums)):
    curr_num = nums_seen.get(nums[i], 0)
    if curr_num:
        pass
    else:
        nums_seen[nums[i]] = [i]

print(nums_seen)