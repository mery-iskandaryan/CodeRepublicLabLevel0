def findMedianSortedArrays(arr1, arr2):
    res = arr1 + arr2
    res.sort()
    mid = len(res) // 2
    if len(res) % 2 == 0:
        return (res[mid-1] + res[mid]) / 2
    return res[mid]

nums1 = [1,2]
nums2 = [3,4]
print(findMedianSortedArrays(nums1, nums2))
