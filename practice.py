nums = [1,2,3,4]

array = []
j = 0
for i in range(0, len(nums)):
	array.append(sum(nums[:i+1]))
	for j in range(i, len(nums)):
		array.append(sum(nums[:j+1]))


print(sorted(array))