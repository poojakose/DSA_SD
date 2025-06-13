def twoSum(nums, target):
    tmp = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in tmp:
            return [tmp[diff], i]
        
        tmp[n] = i
    return []

nums = [3,2,4]
target = 6
result = twoSum(nums, target)
print(result)
