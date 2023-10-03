def find_unique_element(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if mid % 2 == 0:
            if arr[mid] ^ arr[mid + 1] == 0:
                start = mid + 2
            else:
                end = mid
        else:
            if arr[mid] ^ arr[mid - 1] == 0:
                start = mid + 1
            else:
                end = mid - 1
    return arr[start]


ls = [1,1,2,2,6,6,8,8,9,9,10]
print(find_unique_element(ls))
