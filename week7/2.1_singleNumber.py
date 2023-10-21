def singleNumber(nums):
    res = 0
    for i in nums:
        res ^= i

    s = set(nums)
    ls = []
    for i in s:
        if res ^ i in s:
            return [i, res ^ i]


def singleNumber(nums):
    res = []
    for num in nums:
        if num not in res:
            res.append(num)
        else:
            res.remove(num)
    return res

nums = [8, 9, 5, 5, 6, 6, 9, 7]
print(singleNumber(nums))
