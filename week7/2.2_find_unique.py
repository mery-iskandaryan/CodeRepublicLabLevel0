def find_unique(nums):
    res = 0
    for i in nums:
        res ^= i
    return res


nums = [4,1,2,1,2]
print(find_unique(nums))
