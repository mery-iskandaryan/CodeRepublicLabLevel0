def removeElement(nums, val):
    idx = 0
    for num in nums:
        if num != val:
            nums[idx] = num
            idx += 1
    return idx

