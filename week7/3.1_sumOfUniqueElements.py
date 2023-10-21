def sumOfUniqueelements(nums):
    return sum([num for num in nums if nums.count(num) == 1])


nums = [1,2,3,2]
nums = [1,2,3,4,5]
print(sumOfUniqueelements(nums))
