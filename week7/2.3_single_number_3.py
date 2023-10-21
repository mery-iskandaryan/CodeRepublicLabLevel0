def single_number(nums):
    return (sum(set(nums)) * 3 - sum(nums)) // 2


nums = [2, 2, 3, 2]  # 9

def uniue_3(nums):
    d = dict()
    for num in nums:
        if num not in d:
            d[num] = 1
        else:
            d[num] = d[num] + 1
    for i in d:
        if d[i] == 1:
            return i

nums = [0, 1, 0, 1, 0, 1, 99]  # 102
print(uniue_3(nums))
