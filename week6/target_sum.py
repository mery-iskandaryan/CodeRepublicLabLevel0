def twoSum(nums, target: int):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j and nums[i] + nums[j] == target:
                return i, j


lst = [2,7,11,15]
print(twoSum(lst, 9))



