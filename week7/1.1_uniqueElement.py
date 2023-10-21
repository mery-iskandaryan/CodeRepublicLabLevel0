def unique_element(lst, start, end):
    start = 0
    end = len(lst) -1
    while start < end:
        mid = (start + end) // 2
        if mid % 2 == 0:
            if lst[mid] ^ lst[mid + 1] == 0:
                start = mid + 2
            else:
                end = mid
        else:
            if lst[mid] ^ lst[mid +1] == 0:
                end = mid - 1
            else:
                start = mid + 1
    return lst[start]

